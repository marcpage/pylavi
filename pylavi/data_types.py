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
    return Integer(int(matchobj.group(0)[2:], 16), byte_count=IntSize.INT8, signed=False).to_bytes()

def escape_bytes(matchobj) -> bytes:
    return b'\\x' + matchobj.group(0).hex().encode('ascii')


class Description:
    def __str__(self):
        return self.to_string()


class Endian(enum.Enum):
    BIG = '>'
    LITTLE = '<'


class IntSize(enum.Enum):
    INT8 = 'b'
    INT16 = 'h'
    INT32 = 'i'


@total_ordering
class Integer(Description):
    SIZES = {
        IntSize.INT8: 1,
        IntSize.INT16: 2,
        IntSize.INT32: 4,
    }
    def __init__(self, value:int=None, endian:Endian=Endian.BIG, byte_count:IntSize=IntSize.INT32, signed:bool=False):
        self.value = value
        self.endian = endian
        self.signed = signed
        self.byte_count = byte_count

    def size(self) -> int:
        return Integer.SIZES[self.byte_count]

    def __struct_description(self):
        return self.endian.value + (self.byte_count.value if self.signed else self.byte_count.value.upper())

    def from_bytes(self, data:bytes, offset:int=0):
        self.value = struct.unpack(self.__struct_description(), data[offset:offset + self.size()])[0]
        return self

    def to_bytes(self) -> bytes:
        return struct.pack(self.__struct_description(), self.value)

    def from_value(self, description:any):
        self.value = description
        return self

    def to_value(self) -> any:
        return self.value

    def to_string(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"Integer({self.to_string()}, {self.endian}, signed={self.signed}, {self.byte_count})"

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


class Bytes(Description):
    def __init__(self, value:bytes=None, byte_count:int=0):
        if isinstance(value, str):
            value = value.encode('ascii')

        elif value is None and byte_count > 0:
            value = b'\x00'*byte_count

        self.value = value

    def size(self) -> int:
        return len(self.value)

    def from_bytes(self, data:bytes, offset:int=0):
        assert self.value is not None, "You must specify byte_count in constructor"
        self.value = data[offset:offset + self.size()]
        assert len(self.value) == self.size()
        return self

    def to_bytes(self) -> bytes:
        return self.value

    def from_value(self, description:any):
        if description is None:
            self.value = description
        else:
            self.value = ESCAPED_PATTERN.sub(unescape_bytes, description.encode('ascii'))

        return self

    def to_value(self) -> any:
        if self.value is None:
            return None

        return ESCAPE_CHARS.sub(escape_bytes, self.value).decode('ascii')

    def to_string(self):
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
    def __init__(self, value:bytes=None):
        assert value is None or len(value) == 4
        super().__init__(value, byte_count=4)

    def __repr__(self):
        return f"FourCharCode('{self.to_string()}')"


class PString(Bytes):
    def __init__(self, value:bytes=None):
        assert value is None or len(value) < 256
        super().__init__(value)

    def size(self) -> int:
        return 1 + super().size()

    def from_bytes(self, data:bytes, offset:int=0):
        byte_count = Integer(byte_count=IntSize.INT8, signed=False).from_bytes(data, offset)
        self.value = data[offset + 1:offset + byte_count.value + 1]
        assert len(self.value) == byte_count.value, f"{[len(self.value), byte_count]} {data}"
        return self

    def to_bytes(self) -> bytes:
        prefix = Integer(len(self.value), byte_count=IntSize.INT8, signed=False).to_bytes()
        return prefix + self.value

    def __repr__(self):
        return f"PString('{self.to_string()}')"


class Structure(Description):
    def __init__(self, *value):
        self.__fields = [n for n in value[0::2]]
        assert all(isinstance(n, str) for n in self.__fields)
        assert all(isinstance(v, Description) for v in value[1::2])
        self.__dict__.update({n:v for n, v in zip(self.__fields, value[1::2])})

    def size(self):
        return sum(self.__dict__[n].size() for n in self.__fields)

    def from_bytes(self, data:bytes, offset:int=0):
        for name in self.__fields:
            self.__dict__[name].from_bytes(data, offset)
            offset += self.__dict__[name].size()

        return self

    def to_bytes(self) -> bytes:
        return b''.join(self.__dict__[n].to_bytes() for n in self.__fields)

    def from_value(self, description:any):
        assert set(description.keys()) <= set(self.__fields)

        for name in self.__fields:
            if name in description:
                self.__dict__[name].from_value(description[name])

        return self

    def to_value(self) -> any:
        return {n:self.__dict__[n].to_value() for n in self.__fields}

    def to_string(self):
        return str(self.to_value())

    def __repr__(self):
        return f"Structure({', '.join(n+'='+repr(self.__dict__[n]) for n in self.__fields)})"

    def __getitem__(self, key):
        for name in self.__fields:
            if name == key:
                return self.__dict__[name]

        return None

    def __eq__(self, other):

        if not isinstance(other, Structure) or self.__fields != other.__fields:
            return False

        return all(self.__dict__[n] == other.__dict__[n] for n in self.__fields)


class Array(Description):
    def __init__(self, data_type, *value, data_count=0):
        assert all(isinstance(v, data_type) for v in value)
        self.data_type = data_type
        self.value = value if value else [data_type() for _ in range(0, data_count)]

    def size(self) -> int:
        assert self.length() > 0
        return sum(v.size() for v in self.value)

    def length(self) -> int:
        return len(self.value)

    def set_length(self, data_count):
        self.value = [self.data_type() for _ in range(0, data_count)]
        return self

    def from_bytes(self, data:bytes, offset:int=0):
        for value in self.value:
            value.from_bytes(data, offset)
            offset += value.size()

        return self

    def to_bytes(self) -> bytes:
        return b''.join(v.to_bytes() for v in self.value)

    def from_value(self, description:any):
        self.value = [self.data_type().from_value(v) for v in description]
        return self

    def to_value(self) -> any:
        return [v.to_value() for v in self.value]

    def to_string(self):
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

        return all(a == b for a,b in zip(self, other))


@total_ordering
class Version(Integer):
    DEVELOPMENT = 1
    ALPHA = 2
    BETA = 3
    RELEASE = 4
    PHASES = "?dabf"
    PATTERN = re.compile(r"((\d+)(\.(\d+)(\.(\d+))?)?)(([abdfABDF]|{\d})(\d+)?)?")

    @staticmethod
    def __from_string(version:str) -> (int, int, int, int, int):
        final = Version.PHASES[Version.RELEASE]
        correct_format = Version.PATTERN.match(version)
        assert correct_format, f"Incorrect version string: '{version}'"
        major = int(correct_format.group(2))
        minor = int(correct_format.group(4)) if correct_format.group(4) else 0
        patch = int(correct_format.group(6)) if correct_format.group(6) else 0
        phase_str = (
            correct_format.group(8) if correct_format.group(8) else final
        )
        build = int(correct_format.group(9)) if correct_format.group(9) else 0

        if phase_str.startswith("{") and phase_str.endswith("}"):
            phase = int(phase_str[1:-1])
        else:
            phase = Version.PHASES.find(phase_str)
        return major, minor, patch, phase, build

    @staticmethod
    def __compose(major:int, minor:int, patch:int, phase:int, build:int) -> int:
        assert major <= 99, major_or_str
        assert minor <= 9, major_or_str
        assert patch <= 9, major_or_str
        assert build <= 1999, major_or_str
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

        super().__init__(version_value, Endian.BIG, IntSize.INT32, signed=False)

    def size(self) -> int:
        return Integer.SIZES[self.byte_count]

    def from_value(self, description:any):
        self.value = Version.__compose(*Version.__from_string(description))
        return self

    def to_value(self) -> any:
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

