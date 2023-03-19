#!/usr/bin/env python3


from pylavi.data_types import Structure, PString


def test_basic():
    s = Structure('first', PString(), 'last', PString())
    expected_repr = "Structure(first=PString('None'), last=PString('None'))"
    assert repr(s) == expected_repr, [repr(s), expected_repr]
    expected_str = "{'first': None, 'last': None}"
    assert str(s) == expected_str, [str(s), expected_str]
    s.from_bytes(b'\x04John\x09Appleseed')
    assert s.first == 'John'
    assert s.last == 'Appleseed'
    assert s.first == s['first']
    assert s.last == s['last']
    assert s['what'] is None
    assert s.to_bytes() == b'\x04John\x09Appleseed'
    description = s.to_value()
    reconstituted = Structure('first', PString(), 'last', PString()).from_value(description)
    assert reconstituted == s



if __name__ == "__main__":
    test_basic()
