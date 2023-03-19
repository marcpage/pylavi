#!/usr/bin/env python3


from pylavi.data_types import PString


def test_strings():
    for binary in TEST_SET:
        string = PString(binary)
        assert string.size() == TEST_SET[binary][0], f"{string.size()} {binary}"
        assert string.to_bytes()[1:] == binary, f"{string.to_bytes()[1:]} vs {binary}"
        s = PString().from_bytes(string.to_bytes())
        assert s == string, [PString().from_bytes(string.to_bytes()), string]
        description = s.to_value()
        reconstituted = PString().from_value(description)
        assert reconstituted == s

    assert str(PString(b'\tmore\\')) == '\\x09more\\x5c', [str(PString(b'\tmore\\')), '\\x09more\\x5c']
    assert repr(PString(b'\tmore\\')) == "PString('\\x09more\\x5c')"
    try:
        PString(b'01234567890123456789012345678901234567890123456789'
        +b'01234567890123456789012345678901234567890123456789'
        +b'01234567890123456789012345678901234567890123456789'
        +b'01234567890123456789012345678901234567890123456789'
        +b'01234567890123456789012345678901234567890123456789'
        +b'123456')
        raise SyntaxError("We should have thrown an exception")
    except AssertionError:
        pass




TEST_SET = {
    b'': (1,),
    b'test': (5,),
    (b'01234567890123456789012345678901234567890123456789'
    +b'01234567890123456789012345678901234567890123456789'
    +b'01234567890123456789012345678901234567890123456789'
    +b'01234567890123456789012345678901234567890123456789'
    +b'01234567890123456789012345678901234567890123456789'
    +b'12345'): (256,)
}

if __name__ == "__main__":
    test_strings()
