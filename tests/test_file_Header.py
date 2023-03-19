#!/usr/bin/env python3


from pylavi.file import Header


TEST_SETS = {
    b'RSRC\r\n\x00\x03LVINLBVW\x00\x00\x90l\x00\x00\x04\xf3\x00\x00\x00 \x00\x00\x90L': {
        'file_type': 'LVIN',
        'file_creator': 'LBVW',
        'metadata_offset': 36972,
        'metadata_size': 1267,
        'data_offset': 32,
        'data_size': 36940},
    b"RSRC\r\n\x00\x03LVCCLBVW\x00\x00'\xe0\x00\x00\x04<\x00\x00\x00 \x00\x00'\xc0": {
        'file_type': 'LVCC',
        'file_creator': 'LBVW',
        'metadata_offset': 10208,
        'metadata_size': 1084,
        'data_offset': 32,
        'data_size': 10176},
    b'RSRC\r\n\x00\x03LMNULBVW\x00\x00\x0cx\x00\x00\x02\xa4\x00\x00\x00 \x00\x00\x0cX': {
        'file_type': 'LMNU',
        'file_creator': 'LBVW',
        'metadata_offset': 3192,
        'metadata_size': 676,
        'data_offset': 32,
        'data_size': 3160},
    b'RSRC\r\n\x00\x03LVARLBVW\x00\x1f\r\xcc\x00\x00T\x13\x00\x00\x00 \x00\x1f\r\xac': {
        'file_type': 'LVAR',
        'file_creator': 'LBVW',
        'metadata_offset': 2035148,
        'metadata_size': 21523,
        'data_offset': 32,
        'data_size': 2035116},
    b'RSRC\r\n\x00\x03\x00\x00\x00\x00LBVW\x00\x00\x0b\xb8\x00\x00\x01\x90\x00\x00\x00 \x00\x00\x0b\x98': {
        'file_type': 'x00000000',
        'file_creator': 'LBVW',
        'metadata_offset': 3000,
        'metadata_size': 400,
        'data_offset': 32,
        'data_size': 2968},
    b'RSRC\r\n\x00\x03LVRSLBVW\x00\x00\t\x04\x00\x00\x02G\x00\x00\x00 \x00\x00\x08\xe4': {
        'file_type': 'LVRS',
        'file_creator': 'LBVW',
        'metadata_offset': 2308,
        'metadata_size': 583,
        'data_offset': 32,
        'data_size': 2276},
    b'RSRC\r\n\x00\x03LVSBLBVW\x00\x01p`\x00\x00\x00\x88\x00\x00\x00 \x00\x01p@': {
        'file_type': 'LVSB',
        'file_creator': 'LBVW',
        'metadata_offset': 94304,
        'metadata_size': 136,
        'data_offset': 32,
        'data_size': 94272},
    b'RSRC\r\n\x00\x03iUWl\x00\x00\x00\x00\x00\x00\r4\x00\x00\x028\x00\x00\x00 \x00\x00\r\x14': {
        'file_type': 'iUWl',
        'file_creator': 'x00000000',
        'metadata_offset': 3380,
        'metadata_size': 568,
        'data_offset': 32,
        'data_size': 3348},
    b'RSRC\r\n\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b$\x00\x00\x08|\x00\x00\x00 \x00\x00b\x04': {
        'file_type': 'x00000000',
        'file_creator': 'x00000000',
        'metadata_offset': 25124,
        'metadata_size': 2172,
        'data_offset': 32,
        'data_size': 25092},
    b'RSRC\r\n\x00\x03iUWlWLin\x00\x00.\xfc\x00\x00\x04@\x00\x00\x00 \x00\x00.\xdc': {
        'file_type': 'iUWl',
        'file_creator': 'WLin',
        'metadata_offset': 12028,
        'metadata_size': 1088,
        'data_offset': 32,
        'data_size': 11996},
}


def test_Header():
    for header_index, header_bytes in enumerate(TEST_SETS):
        header = Header().from_bytes(header_bytes)
        assert header['file_type'] == TEST_SETS[header_bytes]['file_type']
        assert header['file_creator'] == TEST_SETS[header_bytes]['file_creator']
        assert header['metadata_offset'] == TEST_SETS[header_bytes]['metadata_offset']
        assert header['metadata_size'] == TEST_SETS[header_bytes]['metadata_size']
        assert header['data_offset'] == TEST_SETS[header_bytes]['data_offset'], f"{header['data_offset']} != {TEST_SETS[header_bytes]['data_offset']}"
        assert header['data_size'] == TEST_SETS[header_bytes]['data_size'], f"{header['data_size']} != {TEST_SETS[header_bytes]['data_size']}"
        expected_repr = f"Header({{file_type={header['file_type'].to_string()}, file_creator={header['file_creator'].to_string()}, metadata_offset={header['metadata_offset']}, metadata_size={header['metadata_size']}, data_offset={header['data_offset']}, data_size={header['data_size']}}})"
        assert repr(header) == expected_repr, f"repr\n{repr(header)}\nvs\n{expected_repr}"
        header.validate(header['metadata_offset'] + header['metadata_size'])
        assert header == Header().from_bytes(header_bytes)
        assert header != 5


if __name__ == "__main__":
    test_Header()
