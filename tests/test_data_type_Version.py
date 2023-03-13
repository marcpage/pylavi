#!/usr/bin/env python3


from pylavi.data_types import Version


def test_strings():
    for version_string in VERSION_STRINGS:
        version = Version(version_string)
        assert version.major() == VERSION_STRINGS[version_string][0]
        assert version.minor() == VERSION_STRINGS[version_string][1], f"{version_string} -> {version.minor()} {VERSION_STRINGS[version_string]}"
        assert version.patch() == VERSION_STRINGS[version_string][2]
        assert version.phase() == VERSION_STRINGS[version_string][3], f"{version_string} -> {version.phase()} {VERSION_STRINGS[version_string]}"
        assert version.build() == VERSION_STRINGS[version_string][4]
        assert str(version) == version_string, f"{version_string} -> {str(version)}"
        assert repr(version) == f"Version('{version}')"


def test_ints():
    for version_int in VERSION_INTS:
        version = Version(version_int)
        assert version.major() == VERSION_INTS[version_int][0]
        assert version.minor() == VERSION_INTS[version_int][1], f"{version_int} -> {version.minor()} {VERSION_INTS[version_int]}"
        assert version.patch() == VERSION_INTS[version_int][2]
        assert version.phase() == VERSION_INTS[version_int][3], f"{version_int} -> {version.phase()} {VERSION_INTS[version_int]}"
        assert version.build() == VERSION_INTS[version_int][4]


def test_bytes():
    for version_bytes in VERSION_BYTES:
        version = Version(version_bytes)
        assert version.major() == VERSION_BYTES[version_bytes][0]
        assert version.minor() == VERSION_BYTES[version_bytes][1], f"{version_bytes} -> {version.minor()} {VERSION_BYTES[version_bytes]}"
        assert version.patch() == VERSION_BYTES[version_bytes][2]
        assert version.phase() == VERSION_BYTES[version_bytes][3], f"{version_bytes} -> {version.phase()} {VERSION_BYTES[version_bytes]}"
        assert version.build() == VERSION_BYTES[version_bytes][4]


def test_fields():
    for version_fields in VERSION_BYTES.values():
        version = Version(*version_fields)
        assert version.major() == version_fields[0]
        assert version.minor() == version_fields[1], f"{version_fields} -> {version.minor()} {version_fields}"
        assert version.patch() == version_fields[2]
        assert version.phase() == version_fields[3], f"{version_fields} -> {version.phase()} {version_fields}"
        assert version.build() == version_fields[4]


def test_comparisons():
    versions = {Version(v):v for v in VERSION_STRINGS}

    for version_string in VERSION_STRINGS:
        version = Version(version_string)

    for sorted_version, ordered_version in zip(sorted(versions), versions):
        assert sorted_version == ordered_version
        assert sorted_version == ordered_version.to_string()

    assert Version("1.2.3a") < "1.2.3a1234"


VERSION_STRINGS = {
    '0': (0,0,0,Version.RELEASE,0),
    '1{0}': (1,0,0,0,0),
    '1': (1,0,0,Version.RELEASE,0),
    '1{6}': (1,0,0,6,0),
    '1.2': (1,2,0,Version.RELEASE,0),
    '1.2.3a': (1,2,3,Version.ALPHA,0),
    '1.2.3a1234': (1,2,3,Version.ALPHA,1234),
    '1.2.3': (1,2,3,Version.RELEASE,0),
    '23': (23,0,0,Version.RELEASE,0),
}

VERSION_INTS = {
    0x00008000: (0,0,0,Version.RELEASE,0),
    0x01008000: (1,0,0,Version.RELEASE,0),
    0x23008000: (23,0,0,Version.RELEASE,0),
    0x01208000: (1,2,0,Version.RELEASE,0),
    0x01238000: (1,2,3,Version.RELEASE,0),
    0x01234000: (1,2,3,Version.ALPHA,0),
    0x01235234: (1,2,3,Version.ALPHA,1234),
    0x0100c000: (1,0,0,6,0),
    0x01000000: (1,0,0,0,0),
}

VERSION_BYTES = {
    b'\x00\x00\x80\x00': (0,0,0,Version.RELEASE,0),
    b'\x01\x00\x80\x00': (1,0,0,Version.RELEASE,0),
    b'\x23\x00\x80\x00': (23,0,0,Version.RELEASE,0),
    b'\x01\x20\x80\x00': (1,2,0,Version.RELEASE,0),
    b'\x01\x23\x80\x00': (1,2,3,Version.RELEASE,0),
    b'\x01\x23\x40\x00': (1,2,3,Version.ALPHA,0),
    b'\x01\x23\x52\x34': (1,2,3,Version.ALPHA,1234),
    b'\x01\x00\xc0\x00': (1,0,0,6,0),
    b'\x01\x00\x00\x00': (1,0,0,0,0),
}


if __name__ == "__main__":
    test_strings()
    test_ints()
    test_bytes()
    test_fields()
    test_comparisons()


