#!/usr/bin/env python3


from pylavi.data_types import PString


def test_strings():
    for binary in TEST_SET:
        string = PString(binary)
        assert string.size() == TEST_SET[binary][0], f"{string.size()} {binary}"
        assert string.to_bytes()[1:] == binary
        assert PString().from_bytes(string.to_bytes()) == string
        assert str(string) == str(binary)
        assert repr(string) == f"PString({str(binary)})"

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
