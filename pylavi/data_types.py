"""
    Common data types for LabVIEW resources
"""


import struct
import enum
from functools import total_ordering
import re


ESCAPED_PATTERN = re.compile(b"\\\\x[0-9a-f][0-9a-f]")
ESCAPE_CHARS = re.compile(b"[^ -[\\]-~]")


def unescape_bytes(matchobj) -> bytes:
    """unescape non-ascii bytes"""
    return UInt8(int(matchobj.group(0)[2:], 16)).to_bytes()


def escape_bytes(matchobj) -> bytes:
    """escape non-ascii bytes"""
    return b"\\x" + matchobj.group(0).hex().encode("ascii")


class Description:
    """Base class for all descriptions"""

    def to_string(self) -> str:
        """Get a string representation"""
        return ""

    def size(self):
        """no size for an empty description"""
        return 0

    # pylint: disable=unused-argument
    def from_bytes(self, data: bytes, offset: int = 0):
        """no bytes to read"""
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return b""

    def __str__(self):
        return self.to_string()


class Endian(enum.Enum):
    """integer endian type"""

    BIG = ">"
    LITTLE = "<"


class IntSize(enum.Enum):
    """struct pack characters"""

    INT8 = "b"
    INT16 = "h"
    INT32 = "i"


@total_ordering
class Integer(Description):
    """Integer type"""

    SIZES = {
        IntSize.INT8: 1,
        IntSize.INT16: 2,
        IntSize.INT32: 4,
    }

    def __init__(
        self,
        value: int = None,
        endian: Endian = Endian.BIG,
        byte_count: IntSize = IntSize.INT32,
        signed: bool = False,
    ):
        assert value is None or signed or value >= 0
        self.value = value
        self.endian = endian
        self.signed = signed
        self.byte_count = byte_count

    def size(self) -> int:
        """Get the size of the bytes representation"""
        return Integer.SIZES[self.byte_count]

    def __struct_description(self):
        return self.endian.value + (
            self.byte_count.value if self.signed else self.byte_count.value.upper()
        )

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        assert len(data) >= offset + self.size(), [self.size(), offset, data]
        self.value = struct.unpack(
            self.__struct_description(), data[offset : offset + self.size()]
        )[0]
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        assert self.value is None or self.signed or self.value >= 0
        return struct.pack(self.__struct_description(), self.value)

    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        self.value = description
        assert self.value is None or self.signed or self.value >= 0
        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        assert self.value is None or self.signed or self.value >= 0
        return self.value

    def to_string(self) -> str:
        """Get a string representation"""
        return str(self.value)

    def __repr__(self) -> str:
        return (
            f"Integer({self.to_string()}, {self.endian}, "
            + f"signed={self.signed}, {self.byte_count})"
        )

    def __lt__(self, other) -> bool:
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, bytes):
            return self.value < struct.unpack(self.__struct_description(), other)[0]

        return self.value < other.value

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, bytes):
            return self.value == struct.unpack(self.__struct_description(), other)[0]

        return self.value == other.value

    def __add__(self, other) -> int:
        if isinstance(other, int):
            return self.value + other

        return self.value + other.value

    def __hash__(self):
        return self.value


class UInt32(Integer):
    """unsigned 32-bit integer"""

    def __init__(self, value: int = None, endian: Endian = Endian.BIG):
        super().__init__(value, endian, IntSize.INT32, signed=False)


class UInt16(Integer):
    """unsigned 16-bit integer"""

    def __init__(self, value: int = None, endian: Endian = Endian.BIG):
        super().__init__(value, endian, IntSize.INT16, signed=False)


class UInt8(Integer):
    """unsigned 16-bit integer"""

    def __init__(self, value: int = None, endian: Endian = Endian.BIG):
        super().__init__(value, endian, IntSize.INT8, signed=False)


class Bytes(Description):
    """Collection of Bytes"""

    def __init__(self, value: bytes = None, byte_count: int = 0):
        if isinstance(value, str):
            value = value.encode("ascii")

        elif value is None and byte_count > 0:
            value = b"\x00" * byte_count

        self.value = value

    def size(self) -> int:
        """Get the size of the bytes representation"""
        return len(self.value)

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        assert self.value is not None, "You must specify byte_count in constructor"
        self.value = data[offset : offset + self.size()]
        assert len(self.value) == self.size()
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return self.value

    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        if description is None:
            self.value = description
        else:
            self.value = ESCAPED_PATTERN.sub(
                unescape_bytes, description.encode("ascii")
            )

        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        if self.value is None:
            return None

        return ESCAPE_CHARS.sub(escape_bytes, self.value).decode("ascii")

    def to_string(self):
        """Get a string representation"""
        return self.to_value()

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"Bytes('{self.to_string()}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.to_string() == other

        if isinstance(other, bytes):
            return self.value == other

        return self.value == other.value


class FourCharCode(Bytes):
    """Four character identifier"""

    def __init__(self, value: bytes = None):
        assert value is None or len(value) == 4
        super().__init__(value, byte_count=4)

    def __repr__(self):
        return f"FourCharCode('{self.to_string()}')"


class PString(Bytes):
    """length-prefixed string"""

    def __init__(
        self,
        value: bytes = None,
        pad_to: IntSize = IntSize.INT8,
        prefix_size: IntSize = IntSize.INT8,
    ):
        assert value is None or len(value) < 2 ** (8 * Integer.SIZES[prefix_size])
        super().__init__(value)
        self.pad_to = Integer.SIZES[pad_to]
        self.prefix_size = prefix_size

    def size(self) -> int:
        """Get the size of the bytes representation"""
        return (
            int((Integer.SIZES[self.prefix_size] + super().size() - 1) / self.pad_to)
            + 1
        ) * self.pad_to

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        assert len(data) >= offset + Integer(byte_count=self.prefix_size).size(), [
            offset,
            Integer(byte_count=self.prefix_size).size(),
            data,
        ]
        byte_count = Integer(byte_count=self.prefix_size, signed=False)
        byte_count.from_bytes(data, offset)
        start = offset + Integer.SIZES[self.prefix_size]
        end = start + byte_count.value
        self.value = data[start:end]
        assert len(self.value) == byte_count.value, [
            len(self.value),
            byte_count,
            data[offset:],
        ]
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        prefix = Integer(
            len(self.value), byte_count=self.prefix_size, signed=False
        ).to_bytes()
        value = prefix + self.value
        return value + b"\x00" * (self.size() - len(value))

    def __repr__(self):
        return f"PString('{self.to_string()}')"


class PString16(PString):
    """16-bit length prefixed string"""

    def __init__(self, value: bytes = None, pad_to: IntSize = IntSize.INT8):
        super().__init__(value, pad_to, IntSize.INT16)


class Structure(Description):
    """A collection of heterogeneous, named data"""

    def __init__(self, *value):
        self.__fields = list(value[0::2])
        assert all(isinstance(n, str) for n in self.__fields)
        assert all(isinstance(v, Description) for v in value[1::2])
        self.__dict__.update(dict(zip(self.__fields, value[1::2])))

    def size(self):
        """Get the size of the bytes representation"""
        return sum(self.__dict__[n].size() for n in self.__fields)

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        for name in self.__fields:
            self.__dict__[name].from_bytes(data, offset)
            offset += self.__dict__[name].size()

        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return b"".join(self.__dict__[n].to_bytes() for n in self.__fields)

    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        assert set(description.keys()) <= set(self.__fields)

        for name in self.__fields:
            if name in description:
                self.__dict__[name].from_value(description[name])

        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        return {n: self.__dict__[n].to_value() for n in self.__fields}

    def to_string(self):
        """Get a string representation"""
        return str(self.to_value())

    def __repr__(self):
        return f"Structure({', '.join(n+'='+repr(self.__dict__[n]) for n in self.__fields)})"

    def __getitem__(self, key):
        for name in self.__fields:
            if name == key:
                return self.__dict__[name]

        return None

    # pylint: disable=protected-access
    def __eq__(self, other):
        if not isinstance(other, Structure) or self.__fields != other.__fields:
            return False

        return all(self.__dict__[n] == other.__dict__[n] for n in self.__fields)


class Array(Description):
    """A list of data of the same type"""

    def __init__(self, data_type, *value, data_count=0):
        assert all(isinstance(v, data_type) for v in value), [data_type, repr(value)]
        assert len(value) == 0 or data_count == 0
        self.data_type = data_type
        self.value = value if value else [data_type() for _ in range(0, data_count)]

    def size(self) -> int:
        """Get the size of the bytes representation"""
        assert self.length() >= 0
        return sum(v.size() for v in self.value)

    def length(self) -> int:
        """Get the number of elements in the array"""
        return len(self.value)

    def set_length(self, data_count: int):
        """Clear the array and fill it with data_count empty data elements"""
        self.value = [self.data_type() for _ in range(0, data_count)]
        return self

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        for value in self.value:
            value.from_bytes(data, offset)
            offset += value.size()

        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return b"".join(v.to_bytes() for v in self.value)

    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        self.value = [self.data_type().from_value(v) for v in description]
        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        return [v.to_value() for v in self.value]

    def to_string(self):
        """Get a string representation"""
        return str(self.to_value())

    def __repr__(self):
        return f"List({', '.join(repr(v) for v in self.value)})"

    def __len__(self):
        return self.length()

    def __getitem__(self, item_index):
        return self.value[item_index]

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        return all(a == b for a, b in zip(self, other))


class Path(Structure):
    """LabVIEW path type"""

    KNOWN_PATH_FORMATS = ["PTH0", "PTH1", "PTH2"]
    ABSOLUTE = 0
    RELATIVE = 1
    NOTAPATH = 2
    UNC = 3
    TYPE_VALUES = [ABSOLUTE, RELATIVE, NOTAPATH, UNC]
    TYPES = ["absolute", "relative", "not a path", "unc"]
    NEW_TYPES = ["abs ", "rel ", "!pth", "unc "]
    STARTS = {
        ABSOLUTE: "/",
        RELATIVE: "",
        UNC: "//",
    }
    NEW_PATH_PATTERN = re.compile(r"^{([0-9])}")

    def __init__(self):
        super().__init__(
            "format",
            FourCharCode(Path.KNOWN_PATH_FORMATS[0]),
            "byte_count",
            UInt32(FourCharCode().size() + UInt32().size()),
        )
        self.type = UInt16(Path.ABSOLUTE)
        self.count = UInt16(0)
        self.elements = Array(PString)
        assert self.format in Path.KNOWN_PATH_FORMATS, self.format
        assert self.type < len(Path.TYPES)

    def __name_to_str(self, name: bytes) -> str:
        if len(name) == 0:
            return ".."

        if self.format != Path.KNOWN_PATH_FORMATS[-1]:
            value = ESCAPE_CHARS.sub(escape_bytes, name).decode("ascii")
        else:
            value = name.decode("utf-8")

        return value.replace("/", "\\x2f")

    def __str_to_name(self, name: str) -> bytes:
        if name == "..":
            return b""

        value = name.replace("\\x2f", "/")

        if self.format != Path.KNOWN_PATH_FORMATS[-1]:
            return ESCAPED_PATTERN.sub(unescape_bytes, value.encode("ascii"))

        return value.encode("utf-8")

    def size(self):
        """Get the size of the bytes representation"""
        return (
            super().size() + self.type.size() + self.count.size() + self.elements.size()
        )

    def is_type(self, path_format: int) -> bool:
        """determine if this path has the given format"""
        if self.type.value in Path.TYPE_VALUES:
            return self.type.value == path_format

        return self.type.to_string() == Path.NEW_TYPES[path_format]

    def get_type(self) -> int:
        """Get the format int"""
        if isinstance(self.type, Integer):
            assert self.type.value < len(Path.TYPES)
            return self.type.value

        assert self.type.to_string() in Path.NEW_TYPES, [
            self.type.to_string(),
            Path.NEW_TYPES,
            self.type,
        ]
        return Path.NEW_TYPES.index(self.type.to_string())

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        super().from_bytes(data, offset)

        if self.format.to_string() == Path.KNOWN_PATH_FORMATS[0]:
            string_type = PString
            self.type = Integer(0, byte_count=IntSize.INT16)
            self.count = Integer(0, byte_count=IntSize.INT16)
        else:
            string_type = PString16
            self.type = FourCharCode()
            self.count = Description()

        offset += super().size()
        original_offset = offset
        self.type.from_bytes(data, offset)
        offset += self.type.size()
        self.count.from_bytes(data, offset)
        offset += self.count.size()
        elements = []
        assert self.byte_count + original_offset <= len(data), [original_offset, data]

        while offset - original_offset < self.byte_count:
            elements.append(string_type().from_bytes(data, offset))
            offset += elements[-1].size()

        assert offset - original_offset == self.byte_count, [
            offset,
            original_offset,
            self,
            data,
        ]
        self.elements = Array(string_type, *elements)
        assert not self.is_type(Path.NOTAPATH) or len(self.elements) == 0
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return (
            super().to_bytes()
            + self.type.to_bytes()
            + self.count.to_bytes()
            + self.elements.to_bytes()
        )

    # pylint: disable=attribute-defined-outside-init
    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        if description is None:
            self.format = FourCharCode(Path.KNOWN_PATH_FORMATS[0])
            self.byte_count = UInt32(self.format.size())
            self.type = UInt16(Path.NOTAPATH)
            self.count = UInt16(0)
            self.elements = Array(PString)
            return self

        new_path_type = Path.NEW_PATH_PATTERN.match(description)

        if new_path_type:
            description = description[new_path_type.end() :]
            type_index = int(new_path_type.group(1))
            name_type = PString16
        else:
            type_index = 0
            name_type = PString

        self.format = FourCharCode(Path.KNOWN_PATH_FORMATS[type_index])
        path_format = [
            f
            for f in [Path.UNC, Path.ABSOLUTE, Path.RELATIVE]
            if description.startswith(Path.STARTS[f])
        ][0]
        self.type = (
            FourCharCode(Path.NEW_TYPES[path_format])
            if new_path_type
            else UInt16(path_format)
        )
        description = description[len(Path.STARTS[path_format]) :]
        self.elements = Array(
            name_type,
            *[name_type(self.__str_to_name(n)) for n in description.split("/")],
        )
        self.count = Description() if new_path_type else UInt16(len(self.elements))
        self.byte_count = UInt32(len(self.to_bytes()) - super().size())
        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        if self.is_type(Path.NOTAPATH):
            return None

        if self.format.to_string() != Path.KNOWN_PATH_FORMATS[0]:
            value = f"{{{Path.KNOWN_PATH_FORMATS.index(self.format.to_string())}}}"
        else:
            value = ""

        value += Path.STARTS[self.get_type()]
        return value + "/".join(self.__name_to_str(n.value) for n in self.elements)

    def to_string(self) -> str:
        return str(self.to_value())

    def __repr__(self) -> str:
        return (
            f"Path({self.format}[{self.byte_count}] "
            + f"{Path.TYPES[self.get_type()]} #{self.count} {self.elements})"
        )


@total_ordering
class Version(UInt32):
    """LabVIEW version number"""

    DEVELOPMENT = 1
    ALPHA = 2
    BETA = 3
    RELEASE = 4
    PHASES = "?dabf"
    PATTERN = re.compile(r"((\d+)(\.(\d+)(\.(\d+))?)?)(([abdfABDF]|{\d})(\d+)?)?")

    @staticmethod
    def __from_string(version: str) -> (int, int, int, int, int):
        final = Version.PHASES[Version.RELEASE]
        correct_format = Version.PATTERN.match(version)
        assert correct_format, f"Incorrect version string: '{version}'"
        major = int(correct_format.group(2))
        minor = int(correct_format.group(4)) if correct_format.group(4) else 0
        patch = int(correct_format.group(6)) if correct_format.group(6) else 0
        phase_str = correct_format.group(8) if correct_format.group(8) else final
        build = int(correct_format.group(9)) if correct_format.group(9) else 0

        if phase_str.startswith("{") and phase_str.endswith("}"):
            phase = int(phase_str[1:-1])
        else:
            phase = Version.PHASES.find(phase_str)
        return major, minor, patch, phase, build

    @staticmethod
    def __compose(major: int, minor: int, patch: int, phase: int, build: int) -> int:
        assert major <= 99, major
        assert minor <= 9, minor
        assert patch <= 9, patch
        assert build <= 1999, build
        return (
            (int(major / 10) << 28)
            + ((major % 10) << 24)
            + (minor << 20)
            + (patch << 16)
            + (phase << 13)
            + (int(build / 1000) << 12)
            + (int(build % 1000 / 100) << 8)
            + (int(build % 100 / 10) << 4)
            + ((build % 10) << 0)
        )

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        major_or_str: any = None,
        minor: int = None,
        patch: int = None,
        phase: int = None,
        build: int = None,
    ):
        version_value = None

        if major_or_str is not None:
            if isinstance(major_or_str, str):
                assert minor is None
                assert patch is None
                assert phase is None
                assert build is None
                major, minor, patch, phase, build = Version.__from_string(major_or_str)
            elif isinstance(major_or_str, bytes):
                assert minor is None
                assert patch is None
                assert phase is None
                assert build is None
                version_value = int.from_bytes(major_or_str, "big")
            elif major_or_str <= 99:
                major = major_or_str
                minor = minor or 0
                patch = patch or 0
                phase = Version.RELEASE if phase is None else phase
                build = build or 0
            else:
                assert minor is None
                assert patch is None
                assert phase is None
                assert build is None
                version_value = major_or_str

            if not version_value:
                version_value = Version.__compose(major, minor, patch, phase, build)

        super().__init__(version_value)

    def size(self) -> int:
        """Get the size of the bytes representation"""
        return Integer.SIZES[self.byte_count]

    def from_value(self, description: any):
        """Get a Python basic type to represent this value"""
        self.value = Version.__compose(*Version.__from_string(description))
        return self

    def to_value(self) -> any:
        """restore from a basic python type"""
        major = self.major()
        minor = self.minor()
        patch = self.patch()
        phase = self.phase()
        build = self.build()
        version_string = str(major)

        if minor > 0 or patch > 0:
            version_string += f".{minor}"

            if patch > 0:
                version_string += f".{patch}"

        if phase != Version.RELEASE or build > 0:
            if Version.DEVELOPMENT <= phase <= Version.RELEASE:
                phase_str = Version.PHASES[phase]
            else:
                phase_str = f"{{{phase}}}"

            version_string += phase_str

            if build > 0:
                version_string += str(build)
        return version_string

    def to_string(self):
        """Get a string representation"""
        return self.to_value()

    def __repr__(self):
        return f"Version('{self.to_string()}')"

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.value < other.value

        return self.value < Version(other).value

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.value == other.value

        return self.value == Version(other).value

    def __hash__(self):
        return self.value

    def major(self):
        """get the major version"""
        return (self.value >> 28 & 0xF) * 10 + (self.value >> 24 & 0xF)

    def minor(self):
        """get the minor version"""
        return int(self.value >> 20 & 0xF)

    def patch(self):
        """get the patch version"""
        return int(self.value >> 16 & 0xF)

    def phase(self):
        """get the version phase"""
        return self.value >> 13 & 0x7

    def build(self):
        """get the build number"""
        return (
            1000 * (self.value >> 12 & 0x01)
            + 100 * (self.value >> 8 & 0xF)
            + 10 * int(self.value >> 4 & 0xF)
            + (self.value >> 0 & 0xF)
        )
