"""
    LabVIEW resource data
"""


import ctypes
import struct
import hashlib

from pylavi.data_types import Structure, Version, PString


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

    LOCKED = (0, 0x00002000)
    SAVE_FOR_PREVIOUS = (1, 0x00000004)
    SEPARATE_CODE = (1, 0x00000400)
    AUTO_ERROR_HANDLING = (1, 0x20000000)
    BREAKPOINTS_SET = (5, 0x20000000)
    BREAKPOINT_COUNT_OFFSET = 48

    def __init__(self):
        self.header = HeaderLVSR()
        self.extra = b""

    def __flag_value(self, flag: int, mask: int, new_value: bool) -> bool:
        old_value = self.header.flags[flag] & mask != 0

        if new_value is not None:
            if new_value:
                self.header.flags[flag] |= mask
            else:
                self.header.flags[flag] &= ~mask

        return old_value

    def breakpoint_count(self):
        """returns the number of breakpoints or None if not supported"""
        if len(self.extra) < 52:
            return None

        return struct.unpack(
            ">I",
            self.extra[
                TypeLVSR.BREAKPOINT_COUNT_OFFSET : TypeLVSR.BREAKPOINT_COUNT_OFFSET + 4
            ],
        )[0]

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


class Headervers(Structure):
    """Header for vers resource"""

    _pack_ = 1
    _fields_ = [
        ("version", Version),
        ("language", ctypes.c_short),
    ]


class Typevers:
    """handles 'vers' resource types"""

    ENGLISH = 0
    FRENCH = 1
    GERMAN = 3
    JAPANESE = 14
    KOREAN = 23
    CHINESE = 33
    LANGUAGES = [0, 1, 3, 14, 23, 33]

    @staticmethod
    def __decode_byte_string(string: bytes) -> str:
        return string.decode("ascii")

    @staticmethod
    def __encode_byte_string(string: str) -> bytes:
        return string.encode("ascii")

    def __init__(
        self,
        version: any = None,
        language: int = None,
        text: bytes = None,
        name: bytes = None,
    ):
        self.version = version if isinstance(version, Version) else Version(version)
        self.language = language or Typevers.ENGLISH
        assert self.language in Typevers.LANGUAGES
        self.text = text or b""
        PString(self.text)
        self.name = name or b""
        PString(self.name)

    def to_bytes(self) -> bytes:
        """Convert to resource data"""
        header = Headervers(version=self.version, language=self.language).to_bytes()
        return header + PString(self.text).to_bytes() + PString(self.name).to_bytes()

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        header = Headervers().from_bytes(data, offset)
        text = PString().from_bytes(data, offset + header.size())
        name = PString().from_bytes(data, offset + header.size() + text.size())
        self.version = header.version
        self.language = header.language
        self.text = text.string
        self.name = name.string
        assert self.language in Typevers.LANGUAGES
        return self

    def size(self) -> int:
        """Get the number of bytes for this vers resource"""
        return (
            Headervers().size() + PString(self.text).size() + PString(self.name).size()
        )

    def to_string(self):
        """Get a string representation of the vers resource information"""
        return (
            "{"
            + f"version={self.version.to_string()}, "
            + f"language={self.language}, "
            + f"text={self.text}, "
            + f"name={self.name}"
            + "}"
        )

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return f"Typevers({self.to_string()})"

    def to_dict(self, encoder=None) -> dict:
        """Create a dictionary of basic types of the vers"""
        encoder_func = (
            Typevers.__decode_byte_string if encoder is None else encoder.byte_string
        )
        return {
            "version": self.version.to_string(),
            "language": self.language,
            "text": encoder_func(self.text),
            "name": encoder_func(self.name),
        }

    def from_dict(self, description: dict, encoder=None):
        """Create the vers data from a dictionary describing it"""
        encoder_func = (
            Typevers.__encode_byte_string if encoder is None else encoder.string_byte
        )
        self.version = Version(description.get("version", "0"))
        self.language = description.get("language", Typevers.ENGLISH)
        assert self.language in Typevers.LANGUAGES
        self.text = encoder_func(description.get("text", ""))
        self.name = encoder_func(description.get("name", ""))
        return self

    def __lt__(self, other):
        if isinstance(other, Typevers):
            return self.version < other.version

        return self.version < other

    def __eq__(self, other):
        if isinstance(other, Typevers):
            return self.version == other.version

        return self.version == other
