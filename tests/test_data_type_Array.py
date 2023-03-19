#!/usr/bin/env python3


from pylavi.data_types import Array, PString, Description


def test_basic():
    a = Array(PString)
    a.set_length(2).from_bytes(b'\x04John\x09Appleseed')
    expected_repr = "List(PString('John'), PString('Appleseed'))"
    assert repr(a) == expected_repr, [repr(a), expected_repr]
    expected_str = "['John', 'Appleseed']"
    assert str(a) == expected_str, [str(a), expected_str]
    assert a[0] == 'John'
    assert a[1] == 'Appleseed'
    assert a.to_bytes() == b'\x04John\x09Appleseed'
    description = a.to_value()
    reconstituted = Array(PString).from_value(description)
    assert reconstituted == a, [reconstituted, a]
    a2 = Array(PString, PString('John'))
    assert a != a2


def test_Description():
    assert Description().to_string() == ''


if __name__ == "__main__":
    test_basic()
    test_Description()
