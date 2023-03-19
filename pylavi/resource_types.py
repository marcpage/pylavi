"""
    LabVIEW resource data
"""


import ctypes
import struct
import hashlib

from pylavi.data_types import Structure, Version, PString, Integer, IntSize


class TypeBDPW:
    """handles 'BDPW' resources types"""

    EMPTY_PASSWORD = "d41d8cd98f00b204e9800998ecf8427e"
    MD5_SIZE = 16

    def __init__(self):
        self.password_md5 = None
        self.extra = None

    def has_password(self):
        """Determines if a password was set"""
        return self.password_md5.hex().lower() != TypeBDPW.EMPTY_PASSWORD

    def password_matches(self, password: str) -> bool:
        """checks the password to see if it matches"""
        return hashlib.md5(password.encode("ascii")).digest() == self.password_md5

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        self.password_md5 = data[offset : offset + TypeBDPW.MD5_SIZE]
        self.extra = data[offset + TypeBDPW.MD5_SIZE :]
        return self

    def to_bytes(self) -> bytes:
        """Convert to resource data"""
        return self.password_md5 + self.extra

    def size(self) -> int:
        """Get the number of bytes for this vers resource"""
        return len(self.password_md5) + len(self.extra)

    def to_string(self):
        """Get a string representation of the vers resource information"""
        return (
            "{"
            + f"password_md5={self.password_md5.hex()}, "
            + f"extra={self.extra.hex()}"
            + "}"
        )

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"TypeBDPW({self.to_string()})"

    # pylint: disable=unused-argument
    def to_dict(self, encoder=None) -> dict:
        """Create a dictionary of basic types of the BDPW"""
        return {
            "password_md5": self.password_md5.hex(),
            "extra": self.extra.hex(),
        }

    # pylint: disable=unused-argument
    def from_dict(self, description: dict, encoder=None):
        """Create the BDPW data from a dictionary describing it"""
        self.password_md5 = bytes.fromhex(description.get("password_md5", None))
        self.extra = bytes.fromhex(description.get("extra", None))
        return self


class HeaderLVSR(Structure):
    """Header for LVSR resource"""

    _pack_ = 1
    _fields_ = [
        ("version", Version),
        ("flags", 16 * ctypes.c_uint),
    ]


class TypeLVSR:
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
        self.header = HeaderLVSR()
        self.extra = b""

    def __flag_at_index(self, flag: int) -> int:
        if flag < len(self.header.flags):
            return self.header.flags[flag]

        flag -= len(self.header.flags)
        offset = flag * 4

        if offset + 4 > len(self.extra):
            return None

        return struct.unpack(">I", self.extra[offset : offset + 4])[0]

    def __flag_value(self, flag: int, mask: int, new_value: bool) -> bool:
        flag_value = self.__flag_at_index(flag)
        old_value = None if flag_value is None else (flag_value & mask != 0)

        if new_value is not None:
            if new_value:
                self.header.flags[flag] |= mask
            else:
                self.header.flags[flag] &= ~mask

        return old_value

    def breakpoint_count(self):
        """returns the number of breakpoints or None if not supported"""
        return self.__flag_at_index(TypeLVSR.BREAKPOINT_COUNT_INDEX)

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

    def to_bytes(self) -> bytes:
        """Convert to resource data"""
        return self.header.to_bytes() + self.extra

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        self.header = HeaderLVSR().from_bytes(data, offset)
        self.extra = data[offset + self.header.size() :]
        return self

    def size(self) -> int:
        """Get the number of bytes for this vers resource"""
        return self.header.size() + len(self.extra)

    def to_string(self):
        """Get a string representation of the vers resource information"""
        return (
            "{"
            + f"version={self.header.version.to_string()}, "
            + f"flags={','.join(bin(f) for f in self.header.flags)}, "
            + f"extra={self.extra.hex()}"
            + "}"
        )

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"TypeLVSR({self.to_string()})"

    # pylint: disable=unused-argument
    def to_dict(self, encoder=None) -> dict:
        """Create a dictionary of basic types of the LVSR"""
        return {
            "version": self.header.version.to_string(),
            "flags": self.header.flags,
            "extra": self.extra.hex(),
        }

    # pylint: disable=unused-argument
    def from_dict(self, description: dict, encoder=None):
        """Create the LVSR data from a dictionary describing it"""
        self.header = HeaderLVSR()
        # pylint: disable=attribute-defined-outside-init
        self.header.version = Version(description.get("version", "0"))
        flags = description.get("flags", [0] * 16)

        for flag in range(0, 16):
            self.header.flags[flag] = flags[flag]

        self.extra = bytes.fromhex(description.get("extra", ""))
        return self


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
            'version', version if isinstance(version, Version) else Version(version),
            'language', Integer(language or Typevers.ENGLISH, byte_count=IntSize.INT16),
            'text', PString(text or b""),
            'name', PString(name or b""),
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

    def from_value(self, description:any):
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
