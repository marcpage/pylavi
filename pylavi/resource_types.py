"""
    LabVIEW resource data
"""


import hashlib

from pylavi.data_types import Structure, Array, Bytes, UInt32, UInt16
from pylavi.data_types import PString, Version, Path


class TypePATH(Path):
    """path"""


class TypeDLLP(Path):
    """executable dll path"""


class TypeHLPP(Path):
    """help path"""


class TypeRTMP(Path):
    """VI runtime menu path"""


class TypeLPTH(Array):
    """32-bit-integer-length-prefixed list of paths"""

    def __init__(self):
        super().__init__(Path)

    def size(self) -> int:
        """Get the size of the bytes representation"""
        assert self.length() >= 0
        return UInt32().size() + super().size()

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        data_count = UInt32().from_bytes(data, offset)
        offset += data_count.size()
        self.set_length(data_count.value)
        super().from_bytes(data, offset)
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return UInt32(self.length()).to_bytes() + super().to_bytes()

    def __repr__(self):
        return f"TypeLPTH({', '.join(repr(v) for v in self.value)})"


class TypeBDPW(Array):
    """handles 'BDPW' resources types"""

    EMPTY_PASSWORD = "d41d8cd98f00b204e9800998ecf8427e"
    PASSWORD_MD5_INDEX = 0
    MD5_SIZE = 16

    def __init__(self):
        super().__init__(Bytes)

    def __password_hash(self):
        return self.value[TypeBDPW.PASSWORD_MD5_INDEX].value

    def has_password(self):
        """Determines if a password was set"""
        return self.__password_hash().hex().lower() != TypeBDPW.EMPTY_PASSWORD

    def password_matches(self, password: str) -> bool:
        """checks the password to see if it matches"""
        return hashlib.md5(password.encode("ascii")).digest() == self.__password_hash()

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        assert (len(data) - offset) % TypeBDPW.MD5_SIZE == 0
        md5_count = int((len(data) - offset) / TypeBDPW.MD5_SIZE)
        self.value = [Bytes(byte_count=TypeBDPW.MD5_SIZE) for _ in range(0, md5_count)]
        return super().from_bytes(data, offset)

    def from_value(self, description: any):
        self.value = [Bytes(bytes.fromhex(v)) for v in description]
        assert all(len(b.value) == TypeBDPW.MD5_SIZE for b in self.value)
        return self

    def to_value(self) -> any:
        return [v.value.hex().lower() for v in self.value]

    def __repr__(self) -> str:
        return f"TypeBDPW({self.to_string()})"


# pylint: disable=no-member
class TypeLVSR(Structure):
    """handles 'LVSR' resource types"""

    SUSPEND_ON_RUN = (0, 0x00001000)
    LOCKED = (0, 0x00002000)
    RUN_ON_OPEN = (0, 0x00004000)
    SAVE_FOR_PREVIOUS = (1, 0x00000004)
    SEPARATE_CODE = (1, 0x00000400)
    CLEAR_INDICATORS = (1, 0x01000000)
    AUTO_ERROR_HANDLING = (1, 0x20000000)
    BREAKPOINTS_SET = (5, 0x20000000)
    DEBUGGABLE = (5, 0x40000200)
    BREAKPOINT_COUNT_INDEX = 28

    def __init__(self):
        super().__init__(
            "version",
            Version(),
            "flags",
            Bytes(),
        )

    def __get_flag_set(self, flag: int) -> int:
        value = UInt32()

        if flag * value.size() + value.size() > self.flags.size():
            return None

        return value.from_bytes(self.flags.value, flag * value.size()).value

    def __set_flag_set(self, flag: int, new_value: int):
        value = UInt32(new_value)

        if flag * value.size() + value.size() <= self.flags.size():
            prefix = self.flags.value[: flag * value.size()]
            suffix = self.flags.value[(flag + 1) * value.size() :]
            self.flags.value = prefix + value.to_bytes() + suffix

    def __flag_value(self, flag: int, mask: int, new_value: bool) -> bool:
        flag_value = self.__get_flag_set(flag)
        old_value = None if flag_value is None else (flag_value & mask != 0)

        if new_value is not None:
            if new_value:
                flag_value |= mask
            else:
                flag_value &= ~mask

            self.__set_flag_set(flag, flag_value)

        return old_value

    def breakpoint_count(self):
        """returns the number of breakpoints or None if not supported"""
        return self.__get_flag_set(TypeLVSR.BREAKPOINT_COUNT_INDEX)

    def debuggable(self, value: bool = None) -> bool:
        """VI was marked as debuggable"""
        return self.__flag_value(*TypeLVSR.DEBUGGABLE, value)

    def clear_indicators(self, value: bool = None) -> bool:
        """When run the unwired indicators will be cleared"""
        return self.__flag_value(*TypeLVSR.CLEAR_INDICATORS, value)

    def run_on_open(self, value: bool = None) -> bool:
        """Was this VI marked as run-on-open"""
        return self.__flag_value(*TypeLVSR.RUN_ON_OPEN, value)

    def suspend_on_run(self, value: bool = None) -> bool:
        """Was this VI marked as suspend on run"""
        return self.__flag_value(*TypeLVSR.SUSPEND_ON_RUN, value)

    def locked(self, value: bool = None) -> bool:
        """Was this VI locked (possibly with password)"""
        return self.__flag_value(*TypeLVSR.LOCKED, value)

    def auto_error_handling(self, value: bool = None) -> bool:
        """Was this VI saved with auto error handling turned on"""
        return self.__flag_value(*TypeLVSR.AUTO_ERROR_HANDLING, value)

    def saved_for_previous(self, value: bool = None) -> bool:
        """Was this VI saved for previous version"""
        return self.__flag_value(*TypeLVSR.SAVE_FOR_PREVIOUS, value)

    def has_breakpoints(self, value: bool = None) -> bool:
        """Was this VI saved for previous version"""
        return self.__flag_value(*TypeLVSR.BREAKPOINTS_SET, value)

    def separate_code(self, value: bool = None) -> bool:
        """Was this VI saved with code separate"""
        return self.__flag_value(*TypeLVSR.SEPARATE_CODE, value)

    # pylint: disable=attribute-defined-outside-init
    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        self.flags = Bytes(byte_count=len(data) - offset - self.version.size())
        return super().from_bytes(data, offset)

    def __repr__(self) -> str:
        return f"TypeLVSR({self.to_string()})"


class Typevers(Structure):
    """handles 'vers' resource types"""

    ENGLISH = 0
    FRENCH = 1
    GERMAN = 3
    JAPANESE = 14
    KOREAN = 23
    CHINESE = 33
    LANGUAGES = [0, 1, 3, 14, 23, 33]

    def __init__(
        self,
        version: any = None,
        language: int = None,
        text: bytes = None,
        name: bytes = None,
    ):
        super().__init__(
            "version",
            version if isinstance(version, Version) else Version(version),
            "language",
            UInt16(language or Typevers.ENGLISH),
            "text",
            PString(text or b""),
            "name",
            PString(name or b""),
        )
        assert self.language in Typevers.LANGUAGES

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        super().from_bytes(data, offset)
        assert self.language in Typevers.LANGUAGES
        return self

    def to_string(self):
        """Get a string representation of the vers resource information"""
        return (
            "{"
            + f"version={self.version.to_string()}, "
            + f"language={self.language}, "
            + f"text='{self.text}', "
            + f"name='{self.name}'"
            + "}"
        )

    def __repr__(self) -> str:
        return f"Typevers({self.to_string()})"

    def from_value(self, description: any):
        super().from_value(description)
        assert self.language in Typevers.LANGUAGES
        return self

    def __lt__(self, other):
        if isinstance(other, Typevers):
            return self.version < other.version

        return self.version < other

    def __eq__(self, other):
        if isinstance(other, Typevers):
            return self.version == other.version

        return self.version == other
