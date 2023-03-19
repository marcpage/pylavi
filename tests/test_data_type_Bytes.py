#!/usr/bin/env python3


from pylavi.data_types import Bytes


def test_basic():
    for test_index, test_set in enumerate(TEST_SET):
        b = Bytes(byte_count=len(test_set)).from_bytes(test_set)
        assert b.to_bytes() == test_set
        description = b.to_value()
        reconstituted = Bytes().from_value(description)
        assert reconstituted == b

    assert Bytes().from_value(Bytes().to_value()) == Bytes()
    expected_repr = "Bytes('\\xfftest\\x09')"
    assert repr(Bytes(b'\xFFtest\t')) == expected_repr, [repr(Bytes(b'\xFFtest\t')), expected_repr]
    expected_str = '\\xfftest\\x09'
    assert str(Bytes(b'\xFFtest\t')) == expected_str, [str(Bytes(b'\xFFtest\t')), expected_str]


TEST_SET = [
    b'test',
    b'\x00test\x00',
    b'\xFF\twhat',
]


if __name__ == "__main__":
    test_basic()
