"""
    LabVIEW resource data
"""


import ctypes

from pylavi.data_types import Structure, Version, PString


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
