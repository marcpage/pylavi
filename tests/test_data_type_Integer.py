#!/usr/bin/env python3


from pylavi.data_types import Integer, IntSize, Endian, UInt32, UInt16


def test_basic():
    for test_index, test_set in enumerate(TEST_SET):
        assert Integer(test_set[0], *test_set[2:]) == Integer(None, *test_set[2:]).from_bytes(test_set[1]), f"#{test_index} {test_set} {Integer(test_set[0], *test_set[2:])} vs {Integer(None, *test_set[2:]).from_bytes(test_set[1])}"
        i = Integer(None, *test_set[2:]).from_bytes(test_set[1])
        assert i.to_bytes() == test_set[1]
        description = i.to_value()
        reconstituted = Integer(None, *test_set[2:]).from_value(description)
        assert reconstituted == test_set[1]

    expected_repr = 'Integer(5, Endian.BIG, signed=False, IntSize.INT32)'
    assert repr(Integer(5)) == expected_repr, [repr(Integer(5)), expected_repr]
    expected_str = '5'
    assert str(Integer(5)) == expected_str, [str(Integer(5)), expected_str]
    assert Integer(5) < Integer(7)
    assert Integer(5) < b'\x00\x00\x00\x07'
    assert set((Integer(5), Integer(7), Integer(7))) == set((Integer(5), Integer(7)))


def test_aliases():
    for test_index, test_set in enumerate(TEST_SET):
        if test_set[3] == IntSize.INT32:
            assert UInt32(test_set[0], test_set[2]) == UInt32(None, test_set[2]).from_bytes(test_set[1]), f"#{test_index} {test_set} {UInt32(test_set[0], test_set[2])} vs {UInt32(None, test_set[2]).from_bytes(test_set[1])}"
            i = UInt32(None, test_set[2]).from_bytes(test_set[1])
            assert i.to_bytes() == test_set[1]
            description = i.to_value()
            reconstituted = UInt32(None, test_set[2]).from_value(description)
            assert reconstituted == test_set[1]
        elif test_set[3] == IntSize.INT16:
            assert UInt16(test_set[0], test_set[2]) == UInt16(None, test_set[2]).from_bytes(test_set[1]), f"#{test_index} {test_set} {UInt16(test_set[0], test_set[2])} vs {UInt16(None, test_set[2]).from_bytes(test_set[1])}"
            i = UInt16(None, test_set[2]).from_bytes(test_set[1])
            assert i.to_bytes() == test_set[1]
            description = i.to_value()
            reconstituted = UInt16(None, test_set[2]).from_value(description)
            assert reconstituted == test_set[1]


TEST_SET = [
    (0, b'\x00\x00\x00\x00', Endian.BIG, IntSize.INT32, True),
    (0, b'\x00\x00\x00\x00', Endian.BIG, IntSize.INT32, False),
    (1, b'\x00\x00\x00\x01', Endian.BIG, IntSize.INT32, True),
    (1, b'\x00\x00\x00\x01', Endian.BIG, IntSize.INT32, False),
    (127, b'\x00\x00\x00\x7F', Endian.BIG, IntSize.INT32, True),
    (127, b'\x00\x00\x00\x7F', Endian.BIG, IntSize.INT32, False),
    (128, b'\x00\x00\x00\x80', Endian.BIG, IntSize.INT32, True),
    (128, b'\x00\x00\x00\x80', Endian.BIG, IntSize.INT32, False),
    (255, b'\x00\x00\x00\xFF', Endian.BIG, IntSize.INT32, True),
    (255, b'\x00\x00\x00\xFF', Endian.BIG, IntSize.INT32, False),
    (0, b'\x00\x00\x00\x00', Endian.LITTLE, IntSize.INT32, True),
    (0, b'\x00\x00\x00\x00', Endian.LITTLE, IntSize.INT32, False),
    (1, b'\x01\x00\x00\x00', Endian.LITTLE, IntSize.INT32, True),
    (1, b'\x01\x00\x00\x00', Endian.LITTLE, IntSize.INT32, False),
    (127, b'\x7F\x00\x00\x00', Endian.LITTLE, IntSize.INT32, True),
    (127, b'\x7F\x00\x00\x00', Endian.LITTLE, IntSize.INT32, False),
    (128, b'\x80\x00\x00\x00', Endian.LITTLE, IntSize.INT32, True),
    (128, b'\x80\x00\x00\x00', Endian.LITTLE, IntSize.INT32, False),
    (255, b'\xFF\x00\x00\x00', Endian.LITTLE, IntSize.INT32, True),
    (255, b'\xFF\x00\x00\x00', Endian.LITTLE, IntSize.INT32, False),
    (0, b'\x00\x00', Endian.BIG, IntSize.INT16, True),
    (0, b'\x00\x00', Endian.BIG, IntSize.INT16, False),
    (1, b'\x00\x01', Endian.BIG, IntSize.INT16, True),
    (1, b'\x00\x01', Endian.BIG, IntSize.INT16, False),
    (127, b'\x00\x7F', Endian.BIG, IntSize.INT16, True),
    (127, b'\x00\x7F', Endian.BIG, IntSize.INT16, False),
    (128, b'\x00\x80', Endian.BIG, IntSize.INT16, True),
    (128, b'\x00\x80', Endian.BIG, IntSize.INT16, False),
    (255, b'\x00\xFF', Endian.BIG, IntSize.INT16, True),
    (255, b'\x00\xFF', Endian.BIG, IntSize.INT16, False),
    (0, b'\x00\x00', Endian.LITTLE, IntSize.INT16, True),
    (0, b'\x00\x00', Endian.LITTLE, IntSize.INT16, False),
    (1, b'\x01\x00', Endian.LITTLE, IntSize.INT16, True),
    (1, b'\x01\x00', Endian.LITTLE, IntSize.INT16, False),
    (127, b'\x7F\x00', Endian.LITTLE, IntSize.INT16, True),
    (127, b'\x7F\x00', Endian.LITTLE, IntSize.INT16, False),
    (128, b'\x80\x00', Endian.LITTLE, IntSize.INT16, True),
    (128, b'\x80\x00', Endian.LITTLE, IntSize.INT16, False),
    (255, b'\xFF\x00', Endian.LITTLE, IntSize.INT16, True),
    (255, b'\xFF\x00', Endian.LITTLE, IntSize.INT16, False),
    (1, b'\x01', Endian.BIG, IntSize.INT8, True),
    (1, b'\x01', Endian.BIG, IntSize.INT8, False),
    (0, b'\x00', Endian.BIG, IntSize.INT8, True),
    (0, b'\x00', Endian.BIG, IntSize.INT8, False),
    (127, b'\x7F', Endian.BIG, IntSize.INT8, True),
    (127, b'\x7F', Endian.BIG, IntSize.INT8, False),
    (-128, b'\x80', Endian.BIG, IntSize.INT8, True),
    (128, b'\x80', Endian.BIG, IntSize.INT8, False),
    (-1, b'\xFF', Endian.BIG, IntSize.INT8, True),
    (255, b'\xFF', Endian.BIG, IntSize.INT8, False),
    (1, b'\x01', Endian.LITTLE, IntSize.INT8, True),
    (1, b'\x01', Endian.LITTLE, IntSize.INT8, False),
    (0, b'\x00', Endian.LITTLE, IntSize.INT8, True),
    (0, b'\x00', Endian.LITTLE, IntSize.INT8, False),
    (127, b'\x7F', Endian.LITTLE, IntSize.INT8, True),
    (127, b'\x7F', Endian.LITTLE, IntSize.INT8, False),
    (-128, b'\x80', Endian.LITTLE, IntSize.INT8, True),
    (128, b'\x80', Endian.LITTLE, IntSize.INT8, False),
    (-1, b'\xFF', Endian.LITTLE, IntSize.INT8, True),
    (255, b'\xFF', Endian.LITTLE, IntSize.INT8, False),
]


if __name__ == "__main__":
    test_basic()
    test_aliases()

