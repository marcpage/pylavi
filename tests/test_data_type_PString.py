#!/usr/bin/env python3


from pylavi.data_types import PString, Structure, IntSize, PString16


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


def test_padding_and_prefix_size():
    for test_index, binary in enumerate(PADDING_TEST_SET):
        pad_to = PADDING_TEST_SET[binary].get('pad_to', IntSize.INT16)
        prefix_size = PADDING_TEST_SET[binary].get('prefix_size', IntSize.INT8)
        s = Structure('first', PString(pad_to=pad_to, prefix_size=prefix_size),'last', PString(pad_to=pad_to, prefix_size=prefix_size)).from_bytes(binary)
        assert s.first == PADDING_TEST_SET[binary]['first'], [test_index, s, PADDING_TEST_SET[binary], binary]
        assert s.last == PADDING_TEST_SET[binary]['last']
        assert s.to_bytes() == binary, [test_index, s.to_bytes(), binary]
        description = s.to_value()
        reconstituted = Structure('first', PString(pad_to=pad_to, prefix_size=prefix_size),'last', PString(pad_to=pad_to, prefix_size=prefix_size)).from_value(description)
        assert reconstituted.to_bytes() == binary, [test_index, reconstituted.to_bytes(), binary]


def test_PString16():
    for test_index, binary in enumerate(PADDING_TEST_SET):
        pad_to = PADDING_TEST_SET[binary].get('pad_to', IntSize.INT16)
        prefix_size = PADDING_TEST_SET[binary].get('prefix_size', IntSize.INT8)

        if prefix_size != IntSize.INT16:
            continue

        s = Structure('first', PString16(pad_to=pad_to),'last', PString16(pad_to=pad_to)).from_bytes(binary)
        assert s.first == PADDING_TEST_SET[binary]['first'], [test_index, s, PADDING_TEST_SET[binary], binary]
        assert s.last == PADDING_TEST_SET[binary]['last']
        assert s.to_bytes() == binary, [test_index, s.to_bytes(), binary]
        description = s.to_value()
        reconstituted = Structure('first', PString16(pad_to=pad_to),'last', PString16(pad_to=pad_to)).from_value(description)
        assert reconstituted.to_bytes() == binary, [test_index, reconstituted.to_bytes(), binary]


PADDING_TEST_SET = {
    b'\x02AB\x00\x01A\x00\x00': {'first': 'AB', 'last': 'A', 'pad_to': IntSize.INT32},
    b'\x01J\x00\x00\x01K\x00\x00': {'first': 'J', 'last': 'K', 'pad_to': IntSize.INT32},
    b'\x01J\x00\x00\x02KB\x00': {'first': 'J', 'last': 'KB', 'pad_to': IntSize.INT32},

    b'\x00\x02AB\x00\x01A\x00': {'first': 'AB', 'last': 'A', 'prefix_size': IntSize.INT16},
    b'\x00\x01J\x00\x00\x01K\x00': {'first': 'J', 'last': 'K', 'prefix_size': IntSize.INT16},
    b'\x00\x01J\x00\x00\x02KB': {'first': 'J', 'last': 'KB', 'prefix_size': IntSize.INT16},

    b'\x02AB\x00\x01A': {'first': 'AB', 'last': 'A'},
    b'\x01J\x01K': {'first': 'J', 'last': 'K'},
    b'\x01J\x02KB\x00': {'first': 'J', 'last': 'KB'},
}

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
    test_padding_and_prefix_size()
    test_PString16()

