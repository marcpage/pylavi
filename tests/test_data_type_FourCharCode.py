#!/usr/bin/env python3


from pylavi.file import FourCharCode


def test_FourCharCode():
    test_set = {b"TEST":"TEST", b"test":"test", b"Test":"Test", b"\xff\x00\xff\x00":"\\xff\\x00\\xff\\x00"}

    for test_bytes in test_set:
        fcc = FourCharCode().from_bytes(test_bytes)
        assert fcc.to_string().lower() == test_set[test_bytes].lower(), f"{fcc.to_string()} != {test_set[test_bytes]}"
        assert fcc.to_bytes() == test_bytes
        assert fcc == test_bytes, [fcc, test_bytes]
        description = fcc.to_value()
        reconstituted = FourCharCode().from_value(description)
        assert reconstituted == test_bytes

    assert FourCharCode('TEST').to_string() == 'TEST'
    assert FourCharCode('TEST') == 'TEST'
    assert FourCharCode('TEST') == FourCharCode('TEST')
    assert repr(FourCharCode('TEST')) == "FourCharCode('TEST')"
    assert str(FourCharCode('TEST')) == "TEST", [str(FourCharCode('TEST'))]


if __name__ == "__main__":
    test_FourCharCode()
