"""
    Common data types for LabVIEW resources
"""


import struct
import enum
import re


ESCAPED_PATTERN = re.compile(b"\\\\x[0-9a-f][0-9a-f]")
ESCAPE_CHARS = re.compile(b"[^ -[\\]-~]")


def unescape_bytes(matchobj) -> bytes:
    return Integer.to_bytes(int(matchobj.group(0)[2:], 16), IntSize.INT8, signed=False)

def escape_bytes(matchobj) -> bytes:
    return b'\\x' + matchobj.group(0).hex().encode('ascii')


class Description:
    def __str__(self):
        return self.to_string()


class Endian(enum.Enum):
    BIG = '>'
    LITTLE = '<'
    NATIVE = '='


class IntSize(enum.Enum):
    INT8 = 'b'
    INT16 = 'h'
    INT32 = 'i'
    INT64 = 'q'


class Integer(Description):
    SIZES = {
        IntSize.INT8: 1,
        IntSize.INT16: 2,
        IntSize.INT32: 4,
        IntSize.INT64: 8,
    }
    def __init__(self, value:int=None, endian:Endian=Endian.BIG, byte_count:IntSize=IntSize.INT32, signed:bool=False):
        self.value = value
        self.endian = endian
        self.signed = signed
        self.byte_count = byte_count

    def size(self) -> int:
        return Integer.SIZES[self.byte_count]

    def __struct_description(self):
        return self.endian.value + (self.size if self.signed else self.byte_count.value.upper())

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

class FourCharCode(Description):
    def __init__(self, value:bytes=None):
        if isinstance(value, str):
            value = value.encode('ascii')
        assert value is None or len(value) == 4
        self.value = value

    def size(self) -> int:
        return 4

    def from_bytes(self, data:bytes, offset:int=0):
        self.value = data[offset:offset + self.size()]
        assert len(self.value) == self.size()
        return self

    def to_bytes(self) -> bytes:
        return self.value

    def from_value(self, description:any):
        self.value = ESCAPED_PATTERN.sub(unescape_bytes, description.encode('ascii'))

    def to_value(self) -> any:
        return ESCAPE_CHARS.sub(escape_bytes, self.value).decode('ascii')

    def to_string(self):
        return self.to_value()

    def __repr__(self):
        return f"FourCharCode('{self.to_string()}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.to_string() == other

        if isinstance(other, bytes):
            return self.to_bytes() == other

        return self.value == other.value

class PString(Description):
    def __init__(self, value:bytes=None):
        assert value is None or len(value) < 256
        self.value = value

    def size(self) -> int:
        return 1 + len(self.value)

    def from_bytes(self, data:bytes, offset:int=0):
        byte_count = Integer(byte_count=IntSize.INT8, signed=False).from_bytes(data, offset)
        self.value = data[offset + 1:offset + byte_count.value + 1]
        assert len(self.value) == byte_count.value, f"{[len(self.value), byte_count]} {data}"
        return self

    def to_bytes(self) -> bytes:
        prefix = Integer(len(self.value), byte_count=IntSize.INT8, signed=False).to_bytes()
        return prefix + self.value

    def from_value(self, description:any):
        self.value = ESCAPED_PATTERN.sub(unescape_bytes, description.encode('ascii'))

    def to_value(self) -> any:
        return ESCAPE_CHARS.sub(escape_bytes, self.value).decode('ascii')

    def to_string(self):
        return self.to_value()

    def __repr__(self):
        return f"PString('{self.to_string()}')"

    def __eq__(self, other) -> bool:
        return self.value == other.value

class Structure(Description):
    def __init__(self, *value):
        assert all(isinstance(n, str) for n in value[0::2])
        assert all(isinstance(v, Description) for v in value[1::2])
        self.value = value

    def size(self):
        return sum(v.size() for v in self.value[1::2])

    def from_bytes(self, data:bytes, offset:int=0):
        for value in self.value[1::2]:
            value.from_bytes(data, offset)
            offset += value.size()

        return self

    def to_bytes(self) -> bytes:
        return b''.join(v.to_bytes() for v in self.value[1::2])

    def from_value(self, description:any):
        assert set(description.keys()) <= set(n for n in self.value[0::2])

        for name, value in zip(self.value[0::2], self.value[1::2]):
            if name in description:
                value.from_value(description[name])

        return self

    def to_value(self) -> any:
        return {n:v.to_value() for n, v in zip(self.value[0::2], self.value[1::2])}

    def to_string(self):
        return str(self.to_value())

    def __repr__(self):
        return f"Structure({', '.join(n+'='+repr(v) for n, v in zip(self.value[0::2], self.value[1::2]))})"

    def __getitem__(self, key):
        for name, value in zip(self.value[0::2], self.value[1::2]):
            if name == key:
                return value

        return None

class Array(Description):
    def __init__(self, data_type, *value, data_count=0):
        assert all(isinstance(v, data_type) for v in value)
        self.data_type = data_type
        self.value = value if value else [data_type() for _ in range(0, data_count)]

    def size(self) -> int:
        assert len(self.value) > 0
        return sum(v.size() for v in self.value)

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

