#!/usr/bin/env python3


from pylavi.file import MetadataHeader, Header


TEST_SETS = {
    b"D8.\x01'\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c": {
        'unused_8': 1144532481, 'unused_16': 663748616, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b"H\x00\x15\x00'\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\t\xdc": {
        'unused_8': 1207964928, 'unused_16': 662700041, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2524},
    b"\x00\x00\x00\x00'\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04,": {
        'unused_8': 0, 'unused_16': 663748616, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1068},
    b"\x02\x00\x00\x00' \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c": {
        'unused_8': 33554432, 'unused_16': 656408584, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b"\x8cp'\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\t\xc4": {
        'unused_8': 2356160258, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2500},
    b"\xc6\xbc\xda\x0e'\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c": {
        'unused_8': 3334265358, 'unused_16': 666894344, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b"\xd8d\xb5\x00p'\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x1c": {
        'unused_8': 3630478592, 'unused_16': 1881604103, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 796},
    b"\xfe\xff\xff\xff'`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c": {
        'unused_8': 4278190079, 'unused_16': 660602888, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b"`p'\x01\x10E3\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x020": {
        'unused_8': 1617962753, 'unused_16': 272970512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 560},
    b"e\x12Fl' \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98": {
        'unused_8': 1695696492, 'unused_16': 656408584, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b' Cal\xb7\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x90': {
        'unused_8': 541286764, 'unused_16': 3078619145, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 912},
    b' SofC\x07\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 542338918, 'unused_16': 1124532230, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b' Sof\xe4\xe9\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 542338918, 'unused_16': 3840475143, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b' Whi\x8f\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 542599273, 'unused_16': 2410676233, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b' seq/p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x10': {
        'unused_8': 544433521, 'unused_16': 795869193, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1808},
    b'%\x01\x00\x00\\!\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xb8': {
        'unused_8': 620822528, 'unused_16': 1545666567, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1976},
    b'%\x01\x00\x00\xbf,\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x18': {
        'unused_8': 620822528, 'unused_16': 3207331847, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 792},
    b'%\x01\x00\x00^\x97\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x08X': {
        'unused_8': 620822528, 'unused_16': 1586954247, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2136},
    b'.1 S\xe3[\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x01p': {
        'unused_8': 774971475, 'unused_16': 3814391815, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 368},
    b'13pt\x00@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 825454708, 'unused_16': 4194312, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'13pt\xd0\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03|': {
        'unused_8': 825454708, 'unused_16': 3504341000, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 892},
    b'14pt\x0f\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07P': {
        'unused_8': 825520244, 'unused_16': 267386888, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1872},
    b'4\x00!\x00p`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x08': {
        'unused_8': 872423680, 'unused_16': 1885339657, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1288},
    b'8\x03\x16\x00\xe3\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 939726336, 'unused_16': 3819962376, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'<\xa3 \x01=\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xcc': {
        'unused_8': 1017323521, 'unused_16': 1034944521, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1228},
    b'@\x056T\x94v\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x18': {
        'unused_8': 1074083412, 'unused_16': 2490761222, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 280},
    b'AWG.\x85\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xb8': {
        'unused_8': 1096238894, 'unused_16': 2246049800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1464},
    b'Core\xb8@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03h': {
        'unused_8': 1131377253, 'unused_16': 3091202057, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 872},
    b'Hpo\x01\x10EF\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xc8': {
        'unused_8': 1215328001, 'unused_16': 272975568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 456},
    b'Lp/\x01\x10E3\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xd4': {
        'unused_8': 1282420481, 'unused_16': 272970512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 468},
    b'Lp@\x01\x10E3\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xd4': {
        'unused_8': 1282424833, 'unused_16': 272970512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 468},
    b'Lp\x0f\x01\x10E\xbc\xa8\x00\x00\x00 \x00\x00\x004\x00\x00\x020': {
        'unused_8': 1282412289, 'unused_16': 273005736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 560},
    b'Lpo\x01\x10EF\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x18': {
        'unused_8': 1282436865, 'unused_16': 272975568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 536},
    b'M\x00,\x8a\x92\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 1291857034, 'unused_16': 2457862152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'OPE\x10\xf0 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 1330660624, 'unused_16': 4028629000, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'O\x00\x00\x00\xb7`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03t': {
        'unused_8': 1325400064, 'unused_16': 3076521993, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 884},
    b'Ppo\x01\x10EF\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02h': {
        'unused_8': 1349545729, 'unused_16': 272975568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 616},
    b'Pref\xb00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c': {
        'unused_8': 1349674342, 'unused_16': 2955935752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b'PrinI0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xc4': {
        'unused_8': 1349675374, 'unused_16': 1227882504, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2244},
    b'Prin\x8e\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\nh': {
        'unused_8': 1349675374, 'unused_16': 2390753289, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2664},
    b'R\x05\x00\x00\xd5 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x084': {
        'unused_8': 1376059392, 'unused_16': 3575644169, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2100},
    b'T\x9f\xf1\x06\xb7\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03d': {
        'unused_8': 1419768070, 'unused_16': 3079667721, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 868},
    b'Td\x04\x01\xa6\x02\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x04L': {
        'unused_8': 1415840769, 'unused_16': 2785148934, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1100},
    b'Td\x04\x01t\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe4': {
        'unused_8': 1415840769, 'unused_16': 1955594249, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1252},
    b'Test\x94\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 1415934836, 'unused_16': 2484076552, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'Test\xa0P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x10': {
        'unused_8': 1415934836, 'unused_16': 2689597448, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1040},
    b'Testl`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\\': {
        'unused_8': 1415934836, 'unused_16': 1818230793, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 860},
    b'\\p\x03\x01\x10`\x83@\x00\x00\x00 \x00\x00\x004\x00\x00\x05 ': {
        'unused_8': 1550844673, 'unused_16': 274760512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1312},
    b'\\p\x03\x01\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xfc': {
        'unused_8': 1550844673, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 764},
    b'\\p\x05\x01\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03<': {
        'unused_8': 1550845185, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 828},
    b'\\p\x9b\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x03p': {
        'unused_8': 1550883584, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 880},
    b'\\p\xa3\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x88': {
        'unused_8': 1550885632, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1416},
    b'\\p\xa3\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xcc': {
        'unused_8': 1550885632, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 460},
    b'\\p\xa4\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xdc': {
        'unused_8': 1550885888, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1244},
    b'\\p\xa4\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 1550885888, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'\\p\xa4\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x02x': {
        'unused_8': 1550885888, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 632},
    b'\\p\xa7\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xfc': {
        'unused_8': 1550886656, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 508},
    b'\\p\xa7\x00\x10e\xc4\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xcc': {
        'unused_8': 1550886656, 'unused_16': 275104784, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 460},
    b'\\p\xa7\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xe0': {
        'unused_8': 1550886656, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 480},
    b'\\p\xa8\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xb4': {
        'unused_8': 1550886912, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 436},
    b'\\p\xa8\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x8c': {
        'unused_8': 1550886912, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1932},
    b'\\p\xaa\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x07p': {
        'unused_8': 1550887424, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1904},
    b'\\p\xab\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x04': {
        'unused_8': 1550887680, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1284},
    b'\\p\xab\x00\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c': {
        'unused_8': 1550887680, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b'\\p\xac\x00\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x02D': {
        'unused_8': 1550887936, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 580},
    b'\\p\xad\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x02l': {
        'unused_8': 1550888192, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 620},
    b'\\p\xae\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 1550888448, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\\p\xaf\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x03,': {
        'unused_8': 1550888704, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 812},
    b'\\p\xb4\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x18': {
        'unused_8': 1550889984, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 792},
    b'\\p\xbc\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xc8': {
        'unused_8': 1550892032, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 712},
    b'\\p\xd5\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x02p': {
        'unused_8': 1550898432, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 624},
    b'\\p\xd9\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x10': {
        'unused_8': 1550899456, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 528},
    b'\\p\xda\x00\x10G\n`\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xa0': {
        'unused_8': 1550899712, 'unused_16': 273091168, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 416},
    b'\\p\xdb\x00\x10Z\x04\x80\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x80': {
        'unused_8': 1550899968, 'unused_16': 274334848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 640},
    b'\\p\xe0\x00\x10^!\xa0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xa8': {
        'unused_8': 1550901248, 'unused_16': 274604448, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 680},
    b'\\p\xe2\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xdc': {
        'unused_8': 1550901760, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 476},
    b'\t\x00\x00\x00\xaf\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03`': {
        'unused_8': 150994944, 'unused_16': 2949644296, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 864},
    b'\x00Kf\x80\x99\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x10x': {
        'unused_8': 4941440, 'unused_16': 2577399816, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4216},
    b'\x00Kf\x80z\xb2\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\n\x14': {
        'unused_8': 4941440, 'unused_16': 2058485766, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2580},
    b'\x00\x00\x00\x00 \x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x9c': {
        'unused_8': 0, 'unused_16': 545259528, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 668},
    b'\x00\x00\x00\x00 \xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x0bP': {
        'unused_8': 0, 'unused_16': 547356681, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2896},
    b'\x00\x00\x00\x00!\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05|': {
        'unused_8': 0, 'unused_16': 562036744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1404},
    b'\x00\x00\x00\x00#\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 598736904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00$`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07@': {
        'unused_8': 0, 'unused_16': 610271240, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1856},
    b'\x00\x00\x00\x00%\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08|': {
        'unused_8': 0, 'unused_16': 632291336, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2172},
    b'\x00\x00\x00\x00&0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xec': {
        'unused_8': 0, 'unused_16': 640679944, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1772},
    b'\x00\x00\x00\x00&\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07(': {
        'unused_8': 0, 'unused_16': 649068552, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1832},
    b'\x00\x00\x00\x00(@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04d': {
        'unused_8': 0, 'unused_16': 675282952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1124},
    b'\x00\x00\x00\x00(\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05L': {
        'unused_8': 0, 'unused_16': 683671560, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1356},
    b'\x00\x00\x00\x00(\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xc4': {
        'unused_8': 0, 'unused_16': 684720136, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1476},
    b'\x00\x00\x00\x00)\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06x': {
        'unused_8': 0, 'unused_16': 699400200, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1656},
    b'\x00\x00\x00\x00* \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x04': {
        'unused_8': 0, 'unused_16': 706740232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1284},
    b'\x00\x00\x00\x00*\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 0, 'unused_16': 714080265, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x00\x00\x00\x00+\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b@': {
        'unused_8': 0, 'unused_16': 737148936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2880},
    b'\x00\x00\x00\x00,\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xcc': {
        'unused_8': 0, 'unused_16': 750780425, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 972},
    b'\x00\x00\x00\x00.0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x1c': {
        'unused_8': 0, 'unused_16': 774897673, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1564},
    b'\x00\x00\x00\x00/\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x074': {
        'unused_8': 0, 'unused_16': 800063497, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1844},
    b'\x00\x00\x00\x00/\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x08': {
        'unused_8': 0, 'unused_16': 804257801, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1800},
    b'\x00\x00\x00\x000@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00"|': {
        'unused_8': 0, 'unused_16': 809500681, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 8828},
    b'\x00\x00\x00\x000\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\tp': {
        'unused_8': 0, 'unused_16': 813694985, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2416},
    b'\x00\x00\x00\x001\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b<': {
        'unused_8': 0, 'unused_16': 831520776, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2876},
    b'\x00\x00\x00\x0030\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xec': {
        'unused_8': 0, 'unused_16': 858783753, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2028},
    b'\x00\x00\x00\x0030\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xac': {
        'unused_8': 0, 'unused_16': 858783752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1964},
    b'\x00\x00\x00\x003P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 0, 'unused_16': 860880905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x00\x00\x00\x003\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x98': {
        'unused_8': 0, 'unused_16': 864026632, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1944},
    b'\x00\x00\x00\x004@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x00': {
        'unused_8': 0, 'unused_16': 876609545, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1024},
    b'\x00\x00\x00\x004P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08$': {
        'unused_8': 0, 'unused_16': 877658120, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2084},
    b'\x00\x00\x00\x006\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 0, 'unused_16': 916455433, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x00\x00\x00\x0070\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t8': {
        'unused_8': 0, 'unused_16': 925892616, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2360},
    b'\x00\x00\x00\x007\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x84': {
        'unused_8': 0, 'unused_16': 933232648, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 900},
    b'\x00\x00\x00\x007\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x84': {
        'unused_8': 0, 'unused_16': 934281224, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 900},
    b'\x00\x00\x00\x007\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\xa8': {
        'unused_8': 0, 'unused_16': 937426952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2472},
    b'\x00\x00\x00\x0080\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 942669832, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x008\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 0, 'unused_16': 953155593, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x00\x00\x00\x00:\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe8': {
        'unused_8': 0, 'unused_16': 988807177, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1256},
    b'\x00\x00\x00\x00:\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x18': {
        'unused_8': 0, 'unused_16': 988807176, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1560},
    b'\x00\x00\x00\x00;\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xec': {
        'unused_8': 0, 'unused_16': 998244361, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1516},
    b'\x00\x00\x00\x00;\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xec': {
        'unused_8': 0, 'unused_16': 999292936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2028},
    b'\x00\x00\x00\x00<\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\n\xfc': {
        'unused_8': 0, 'unused_16': 1015021577, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2812},
    b'\x00\x00\x00\x00>0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05X': {
        'unused_8': 0, 'unused_16': 1043333128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1368},
    b'\x00\x00\x00\x00>p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\r\xc4': {
        'unused_8': 0, 'unused_16': 1047527432, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3524},
    b'\x00\x00\x00\x00@\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x18': {
        'unused_8': 0, 'unused_16': 1086324745, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 280},
    b'\x00\x00\x00\x00A\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x8c': {
        'unused_8': 0, 'unused_16': 1090519049, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1164},
    b'\x00\x00\x00\x00B@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xa0': {
        'unused_8': 0, 'unused_16': 1111490568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1440},
    b'\x00\x00\x00\x00B\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08,': {
        'unused_8': 0, 'unused_16': 1117782024, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2092},
    b'\x00\x00\x00\x00Bp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 0, 'unused_16': 1114636296, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'\x00\x00\x00\x00C\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07l': {
        'unused_8': 0, 'unused_16': 1135607817, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1900},
    b'\x00\x00\x00\x00Cp\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\n\xe4': {
        'unused_8': 0, 'unused_16': 1131413513, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2788},
    b'\x00\x00\x00\x00D0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t,': {
        'unused_8': 0, 'unused_16': 1143996424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2348},
    b'\x00\x00\x00\x00Dp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\x04': {
        'unused_8': 0, 'unused_16': 1148190728, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2308},
    b'\x00\x00\x00\x00E\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xfc': {
        'unused_8': 0, 'unused_16': 1157627912, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1532},
    b'\x00\x00\x00\x00E\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xd4': {
        'unused_8': 0, 'unused_16': 1173356552, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1748},
    b'\x00\x00\x00\x00F\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd0': {
        'unused_8': 0, 'unused_16': 1174405129, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 976},
    b'\x00\x00\x00\x00GP\x00\n\x00\x00\x00 \x00\x00\x004\x00\x009\xd8': {
        'unused_8': 0, 'unused_16': 1196425226, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 14808},
    b'\x00\x00\x00\x00G\x80\x00\x04\x00\x00\x00 \x00\x00\x004\x00\x00\x00x': {
        'unused_8': 0, 'unused_16': 1199570948, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 120},
    b'\x00\x00\x00\x00H@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\\': {
        'unused_8': 0, 'unused_16': 1212153864, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 860},
    b'\x00\x00\x00\x00H\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06 ': {
        'unused_8': 0, 'unused_16': 1222639625, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1568},
    b'\x00\x00\x00\x00Ip\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xb8': {
        'unused_8': 0, 'unused_16': 1232076809, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1720},
    b'\x00\x00\x00\x00N \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x16\xbc': {
        'unused_8': 0, 'unused_16': 1310720009, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5820},
    b'\x00\x00\x00\x00N\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05(': {
        'unused_8': 0, 'unused_16': 1318060041, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1320},
    b'\x00\x00\x00\x00O\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xf4': {
        'unused_8': 0, 'unused_16': 1339031560, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1780},
    b'\x00\x00\x00\x00O\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xb0': {
        'unused_8': 0, 'unused_16': 1341128712, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 688},
    b'\x00\x00\x00\x00P0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06T': {
        'unused_8': 0, 'unused_16': 1345323016, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1620},
    b'\x00\x00\x00\x00P`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\nt': {
        'unused_8': 0, 'unused_16': 1348468744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2676},
    b'\x00\x00\x00\x00Q0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x084': {
        'unused_8': 0, 'unused_16': 1362100232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2100},
    b'\x00\x00\x00\x00Q@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x00': {
        'unused_8': 0, 'unused_16': 1363148808, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 768},
    b'\x00\x00\x00\x00Qp\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06d': {
        'unused_8': 0, 'unused_16': 1366294537, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1636},
    b'\x00\x00\x00\x00R \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x070': {
        'unused_8': 0, 'unused_16': 1377828872, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1840},
    b'\x00\x00\x00\x00R\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xb4': {
        'unused_8': 0, 'unused_16': 1376780297, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1460},
    b'\x00\x00\x00\x00S\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xec': {
        'unused_8': 0, 'unused_16': 1392508936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2028},
    b'\x00\x00\x00\x00S\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xe8': {
        'unused_8': 0, 'unused_16': 1405091849, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1768},
    b'\x00\x00\x00\x00S\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0e\xcc': {
        'unused_8': 0, 'unused_16': 1406140424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3788},
    b'\x00\x00\x00\x00S\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08(': {
        'unused_8': 0, 'unused_16': 1407189000, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2088},
    b'\x00\x00\x00\x00U\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xd4': {
        'unused_8': 0, 'unused_16': 1426063368, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1492},
    b'\x00\x00\x00\x00U\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x0c': {
        'unused_8': 0, 'unused_16': 1427111944, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1804},
    b'\x00\x00\x00\x00W\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x0c': {
        'unused_8': 0, 'unused_16': 1470103560, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1548},
    b'\x00\x00\x00\x00X\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06H': {
        'unused_8': 0, 'unused_16': 1476395017, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1608},
    b'\x00\x00\x00\x00X\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\n(': {
        'unused_8': 0, 'unused_16': 1485832200, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2600},
    b'\x00\x00\x00\x00X\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 0, 'unused_16': 1487929353, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'\x00\x00\x00\x00X\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xa8': {
        'unused_8': 0, 'unused_16': 1490026505, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1448},
    b'\x00\x00\x00\x00Y\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 1503657992, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00Y\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 1504706568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00Y\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x12\xa0': {
        'unused_8': 0, 'unused_16': 1508900873, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4768},
    b'\x00\x00\x00\x00Z \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\t\x80': {
        'unused_8': 0, 'unused_16': 1512046601, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2432},
    b'\x00\x00\x00\x00Z\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 1525678088, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00Z`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x0c': {
        'unused_8': 0, 'unused_16': 1516240905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1292},
    b'\x00\x00\x00\x00[ \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\\': {
        'unused_8': 0, 'unused_16': 1528823816, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2908},
    b'\x00\x00\x00\x00[\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc4': {
        'unused_8': 0, 'unused_16': 1540358152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 964},
    b'\x00\x00\x00\x00\\\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x88': {
        'unused_8': 0, 'unused_16': 1552941065, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1928},
    b'\x00\x00\x00\x00\n\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x060': {
        'unused_8': 0, 'unused_16': 180355080, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1584},
    b'\x00\x00\x00\x00\r\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x80': {
        'unused_8': 0, 'unused_16': 226492425, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1664},
    b'\x00\x00\x00\x00\r\xb1S\xb8\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xac': {
        'unused_8': 0, 'unused_16': 229725112, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1964},
    b'\x00\x00\x00\x00\t0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 0, 'unused_16': 154140680, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x00\x00\x00\x00\t\r\xf4\xb8\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x04': {
        'unused_8': 0, 'unused_16': 151909560, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1028},
    b'\x00\x00\x00\x00\t\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\tT': {
        'unused_8': 0, 'unused_16': 162529289, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2388},
    b'\x00\x00\x00\x00\t\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\n(': {
        'unused_8': 0, 'unused_16': 165675017, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2600},
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe8': {
        'unused_8': 0, 'unused_16': 0, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1256},
    b'\x00\x00\x00\x00\x00\x00\x07\xc8\x00\x00\x00 \x00\x00\x004\x00\x00\x00x': {
        'unused_8': 0, 'unused_16': 1992, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 120},
    b'\x00\x00\x00\x00\x00\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\nD': {
        'unused_8': 0, 'unused_16': 11534344, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2628},
    b'\x00\x00\x00\x00\x00\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\tL': {
        'unused_8': 0, 'unused_16': 15728649, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2380},
    b'\x00\x00\x00\x00\x00`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x90': {
        'unused_8': 0, 'unused_16': 6291464, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1936},
    b'\x00\x00\x00\x00\x01\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07D': {
        'unused_8': 0, 'unused_16': 28311560, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1860},
    b'\x00\x00\x00\x00\x01\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 31457288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x02 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 35651592, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x02@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 37748744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x02\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xf0': {
        'unused_8': 0, 'unused_16': 33554441, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1520},
    b'\x00\x00\x00\x00\x02\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 34603016, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x02\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 41943048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x02\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 44040201, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\x02p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01,': {
        'unused_8': 0, 'unused_16': 40894472, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 300},
    b'\x00\x00\x00\x00\x03 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\xf0': {
        'unused_8': 0, 'unused_16': 52428808, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3056},
    b'\x00\x00\x00\x00\x03\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04<': {
        'unused_8': 0, 'unused_16': 65011720, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1084},
    b'\x00\x00\x00\x00\x03\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd4': {
        'unused_8': 0, 'unused_16': 66060296, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 980},
    b'\x00\x00\x00\x00\x04 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 69206025, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\x04\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 78643208, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\x05 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x10\x14': {
        'unused_8': 0, 'unused_16': 85983241, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4116},
    b'\x00\x00\x00\x00\x05\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x88': {
        'unused_8': 0, 'unused_16': 93323272, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1416},
    b'\x00\x00\x00\x00\x05\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xf8': {
        'unused_8': 0, 'unused_16': 94371848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2296},
    b'\x00\x00\x00\x00\x05\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xc4': {
        'unused_8': 0, 'unused_16': 95420424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1476},
    b'\x00\x00\x00\x00\x05\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08L': {
        'unused_8': 0, 'unused_16': 98566152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2124},
    b'\x00\x00\x00\x00\x05\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06(': {
        'unused_8': 0, 'unused_16': 99614729, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1576},
    b'\x00\x00\x00\x00\x060\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x18': {
        'unused_8': 0, 'unused_16': 103809032, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1304},
    b'\x00\x00\x00\x00\x06\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04D': {
        'unused_8': 0, 'unused_16': 100663305, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1092},
    b'\x00\x00\x00\x00\x06\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 109051912, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\x06\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x90': {
        'unused_8': 0, 'unused_16': 112197640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1168},
    b'\x00\x00\x00\x00\x06\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xa0': {
        'unused_8': 0, 'unused_16': 114294792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1184},
    b'\x00\x00\x00\x00\x07@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x94': {
        'unused_8': 0, 'unused_16': 121634825, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1428},
    b'\x00\x00\x00\x00\x07\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b,': {
        'unused_8': 0, 'unused_16': 126877704, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2860},
    b'\x00\x00\x00\x00\x07p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 0, 'unused_16': 124780552, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'\x00\x00\x00\x00\x080\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd0': {
        'unused_8': 0, 'unused_16': 137363465, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 976},
    b'\x00\x00\x00\x00\x08\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x12\xd4': {
        'unused_8': 0, 'unused_16': 142606345, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4820},
    b'\x00\x00\x00\x00\x08\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\xac': {
        'unused_8': 0, 'unused_16': 149946376, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2988},
    b'\x00\x00\x00\x00\x08`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04p': {
        'unused_8': 0, 'unused_16': 140509193, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1136},
    b'\x00\x00\x00\x00\x0e"K(\x00\x00\x00 \x00\x00\x004\x00\x00\t$': {
        'unused_8': 0, 'unused_16': 237128488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2340},
    b'\x00\x00\x00\x00\x0e%\x9ex\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xac': {
        'unused_8': 0, 'unused_16': 237346424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1964},
    b'\x00\x00\x00\x00\x0e\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\tD': {
        'unused_8': 0, 'unused_16': 235929609, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2372},
    b'\x00\x00\x00\x00\x0e\x9c\xed\xc8\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 0, 'unused_16': 245165512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x00\x00\x00\x00\x0f^Qp\x00\x00\x00 \x00\x00\x004\x00\x00\x1e\xcc': {
        'unused_8': 0, 'unused_16': 257839472, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 7884},
    b'\x00\x00\x00\x00\x10\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03(': {
        'unused_8': 0, 'unused_16': 269484040, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 808},
    b'\x00\x00\x00\x00\x10\x1dix\x00\x00\x00 \x00\x00\x004\x00\x00\x05`': {
        'unused_8': 0, 'unused_16': 270363000, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1376},
    b'\x00\x00\x00\x00\x10\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04d': {
        'unused_8': 0, 'unused_16': 281018376, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1124},
    b'\x00\x00\x00\x00\x10\xcc6\xc0\x00\x00\x00 \x00\x00\x004\x00\x00\x038': {
        'unused_8': 0, 'unused_16': 281818816, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 824},
    b'\x00\x00\x00\x00\x10\xcc\x99\xa0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe0': {
        'unused_8': 0, 'unused_16': 281844128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1248},
    b'\x00\x00\x00\x00\x10\xce>\xd8\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x04': {
        'unused_8': 0, 'unused_16': 281951960, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1284},
    b'\x00\x00\x00\x00\x10\xcf\x02\x00\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xa4': {
        'unused_8': 0, 'unused_16': 282001920, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 676},
    b'\x00\x00\x00\x00\x10\xd0F\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x08H': {
        'unused_8': 0, 'unused_16': 282085008, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2120},
    b'\x00\x00\x00\x00\x11 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc0': {
        'unused_8': 0, 'unused_16': 287309833, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1216},
    b'\x00\x00\x00\x00\x11\xe1\xc7\xc0\x00\x00\x00 \x00\x00\x004\x00\x00\x04,': {
        'unused_8': 0, 'unused_16': 300009408, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1068},
    b'\x00\x00\x00\x00\x11\xe6\xd6\xd8\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 0, 'unused_16': 300340952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x00\x00\x00\x00\x11si(\x00\x00\x00 \x00\x00\x004\x00\x00\x04<': {
        'unused_8': 0, 'unused_16': 292776232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1084},
    b'\x00\x00\x00\x00\x12$\x000\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xfc': {
        'unused_8': 0, 'unused_16': 304349232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1276},
    b'\x00\x00\x00\x00\x12P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd8': {
        'unused_8': 0, 'unused_16': 307232776, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 728},
    b'\x00\x00\x00\x00\x12\x8c\x15\xb8\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 311170488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\x12\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 0, 'unused_16': 311427080, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x00\x00\x00\x00\x12y~\xc0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xfc': {
        'unused_8': 0, 'unused_16': 309952192, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1276},
    b'\x00\x00\x00\x00\x12{\x03 \x00\x00\x00 \x00\x00\x004\x00\x00\x05@': {
        'unused_8': 0, 'unused_16': 310051616, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1344},
    b'\x00\x00\x00\x00\x13-/\x80\x00\x00\x00 \x00\x00\x004\x00\x00\x04<': {
        'unused_8': 0, 'unused_16': 321728384, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1084},
    b'\x00\x00\x00\x00\x14P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04@': {
        'unused_8': 0, 'unused_16': 340787209, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1088},
    b'\x00\x00\x00\x00\x14\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x8c': {
        'unused_8': 0, 'unused_16': 346030089, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1164},
    b'\x00\x00\x00\x00\x14\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x8c': {
        'unused_8': 0, 'unused_16': 347078665, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1164},
    b'\x00\x00\x00\x00\x14\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06x': {
        'unused_8': 0, 'unused_16': 349175817, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1656},
    b'\x00\x00\x00\x00\x14\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06x': {
        'unused_8': 0, 'unused_16': 351272969, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1656},
    b'\x00\x00\x00\x00\x15\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 365953032, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\x15\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x08': {
        'unused_8': 0, 'unused_16': 367001608, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1544},
    b'\x00\x00\x00\x00\x15jVx\x00\x00\x00 \x00\x00\x004\x00\x00\t$': {
        'unused_8': 0, 'unused_16': 359290488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2340},
    b'\x00\x00\x00\x00\x15p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x068': {
        'unused_8': 0, 'unused_16': 359661576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1592},
    b'\x00\x00\x00\x00\x16\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 384827400, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\x16p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xdc': {
        'unused_8': 0, 'unused_16': 376438792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 988},
    b'\x00\x00\x00\x00\x17 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x0c': {
        'unused_8': 0, 'unused_16': 387973128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2060},
    b'\x00\x00\x00\x00\x17\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\t\xb4': {
        'unused_8': 0, 'unused_16': 397410313, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2484},
    b'\x00\x00\x00\x00\x19@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05`': {
        'unused_8': 0, 'unused_16': 423624713, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1376},
    b'\x00\x00\x00\x00\x19\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04d': {
        'unused_8': 0, 'unused_16': 434110473, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1124},
    b'\x00\x00\x00\x00\x19\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xe4': {
        'unused_8': 0, 'unused_16': 435159049, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2276},
    b'\x00\x00\x00\x00\x1a\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 450887688, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\x1ap\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x14': {
        'unused_8': 0, 'unused_16': 443547656, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1300},
    b'\x00\x00\x00\x00\x1b0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x0f@': {
        'unused_8': 0, 'unused_16': 456130569, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3904},
    b'\x00\x00\x00\x00\x1c@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xb8': {
        'unused_8': 0, 'unused_16': 473956360, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2232},
    b'\x00\x00\x00\x00\x1cP\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xd0': {
        'unused_8': 0, 'unused_16': 475004937, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1744},
    b'\x00\x00\x00\x00\x1cP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xd8': {
        'unused_8': 0, 'unused_16': 475004936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1752},
    b'\x00\x00\x00\x00\x1c\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06 ': {
        'unused_8': 0, 'unused_16': 469762057, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1568},
    b'\x00\x00\x00\x00\x1c\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x074': {
        'unused_8': 0, 'unused_16': 470810632, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1844},
    b'\x00\x00\x00\x00\x1d\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05x': {
        'unused_8': 0, 'unused_16': 497025033, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1400},
    b'\x00\x00\x00\x00\x1d\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x04': {
        'unused_8': 0, 'unused_16': 500170761, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2052},
    b'\x00\x00\x00\x00\x1e\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xb4': {
        'unused_8': 0, 'unused_16': 504365065, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2228},
    b'\x00\x00\x00\x00\x1f \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 522190857, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\x1f\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xa8': {
        'unused_8': 0, 'unused_16': 521142281, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1704},
    b'\x00\x00\x00\x00\x1f\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06l': {
        'unused_8': 0, 'unused_16': 529530889, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1644},
    b'\x00\x00\x00\x00\x7fP\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 0, 'unused_16': 2135949321, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x00\x00\x00\x00\x7f\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xd8': {
        'unused_8': 0, 'unused_16': 2140143624, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1496},
    b'\x00\x00\x00\x00\x80@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xb0': {
        'unused_8': 0, 'unused_16': 2151677960, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1968},
    b'\x00\x00\x00\x00\x80`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 0, 'unused_16': 2153775112, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x00\x00\x00\x00\x81\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 2165309448, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\x81\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 2178940936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00\x81\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 2179989512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00\x82\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xcc': {
        'unused_8': 0, 'unused_16': 2192572424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1484},
    b'\x00\x00\x00\x00\x82\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06@': {
        'unused_8': 0, 'unused_16': 2196766728, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1600},
    b'\x00\x00\x00\x00\x83\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x00': {
        'unused_8': 0, 'unused_16': 2198863881, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1792},
    b'\x00\x00\x00\x00\x86\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x0eX': {
        'unused_8': 0, 'unused_16': 2248146953, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3672},
    b'\x00\x00\x00\x00\x86\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 0, 'unused_16': 2260729864, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x00\x00\x00\x00\x86\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 2262827016, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\x88P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xb8': {
        'unused_8': 0, 'unused_16': 2286944265, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1720},
    b'\x00\x00\x00\x00\x8b0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x9c': {
        'unused_8': 0, 'unused_16': 2335178761, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1692},
    b'\x00\x00\x00\x00\x8c\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0cH': {
        'unused_8': 0, 'unused_16': 2362441736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3144},
    b'\x00\x00\x00\x00\x8e\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x0c': {
        'unused_8': 0, 'unused_16': 2394947593, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2060},
    b'\x00\x00\x00\x00\x8f\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x08': {
        'unused_8': 0, 'unused_16': 2408579080, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2056},
    b'\x00\x00\x00\x00\x91P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd0': {
        'unused_8': 0, 'unused_16': 2437939209, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 976},
    b'\x00\x00\x00\x00\x91\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd8': {
        'unused_8': 0, 'unused_16': 2433744905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 984},
    b'\x00\x00\x00\x00\x91p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05D': {
        'unused_8': 0, 'unused_16': 2440036361, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1348},
    b'\x00\x00\x00\x00\x93\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06`': {
        'unused_8': 0, 'unused_16': 2478833672, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1632},
    b'\x00\x00\x00\x00\x93p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06H': {
        'unused_8': 0, 'unused_16': 2473590792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1608},
    b'\x00\x00\x00\x00\x94\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xe8': {
        'unused_8': 0, 'unused_16': 2484076552, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1512},
    b'\x00\x00\x00\x00\x94\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04p': {
        'unused_8': 0, 'unused_16': 2493513736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1136},
    b'\x00\x00\x00\x00\x95\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 0, 'unused_16': 2500853768, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'\x00\x00\x00\x00\x96@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x18': {
        'unused_8': 0, 'unused_16': 2520776713, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1304},
    b'\x00\x00\x00\x00\x97 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x13<': {
        'unused_8': 0, 'unused_16': 2535456776, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4924},
    b'\x00\x00\x00\x00\x99P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\\': {
        'unused_8': 0, 'unused_16': 2572156937, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1628},
    b'\x00\x00\x00\x00\x99\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xa8': {
        'unused_8': 0, 'unused_16': 2581594121, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1192},
    b'\x00\x00\x00\x00\x9b\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00#\xb0': {
        'unused_8': 0, 'unused_16': 2608857096, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 9136},
    b'\x00\x00\x00\x00\x9cp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b|': {
        'unused_8': 0, 'unused_16': 2624585736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2940},
    b'\x00\x00\x00\x00\x9fP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 2672820232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00\xa0\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\rh': {
        'unused_8': 0, 'unused_16': 2696937480, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3432},
    b'\x00\x00\x00\x00\xa0\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xe4': {
        'unused_8': 0, 'unused_16': 2699034632, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1508},
    b'\x00\x00\x00\x00\xa3\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01X': {
        'unused_8': 0, 'unused_16': 2747269128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 344},
    b'\x00\x00\x00\x00\xa3\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 2748317704, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xa3\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 2750414856, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xa4\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 2751463432, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xa4`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xe8': {
        'unused_8': 0, 'unused_16': 2757754888, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1512},
    b'\x00\x00\x00\x00\xa5@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\r\xe4': {
        'unused_8': 0, 'unused_16': 2772434952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3556},
    b'\x00\x00\x00\x00\xa6\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 2786066440, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xa6\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x9c': {
        'unused_8': 0, 'unused_16': 2797600776, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 668},
    b'\x00\x00\x00\x00\xa7 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x10': {
        'unused_8': 0, 'unused_16': 2803892232, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1552},
    b'\x00\x00\x00\x00\xa7\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07X': {
        'unused_8': 0, 'unused_16': 2815426568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1880},
    b'\x00\x00\x00\x00\xa80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x08': {
        'unused_8': 0, 'unused_16': 2821718025, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1288},
    b'\x00\x00\x00\x00\xa8`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x08': {
        'unused_8': 0, 'unused_16': 2824863752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1544},
    b'\x00\x00\x00\x00\xa8p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08<': {
        'unused_8': 0, 'unused_16': 2825912328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2108},
    b'\x00\x00\x00\x00\xa9\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06P': {
        'unused_8': 0, 'unused_16': 2835349513, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1616},
    b'\x00\x00\x00\x00\xa9\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04,': {
        'unused_8': 0, 'unused_16': 2845835272, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1068},
    b'\x00\x00\x00\x00\xaa@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xac': {
        'unused_8': 0, 'unused_16': 2856321033, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1196},
    b'\x00\x00\x00\x00\xaa\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05$': {
        'unused_8': 0, 'unused_16': 2862612488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1316},
    b'\x00\x00\x00\x00\xaa\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x14x': {
        'unused_8': 0, 'unused_16': 2866806792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5240},
    b'\x00\x00\x00\x00\xab\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0c\xfc': {
        'unused_8': 0, 'unused_16': 2868903944, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3324},
    b'\x00\x00\x00\x00\xacp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0e\x10': {
        'unused_8': 0, 'unused_16': 2893021192, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3600},
    b'\x00\x00\x00\x00\xaf\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x16\xbc': {
        'unused_8': 0, 'unused_16': 2937061385, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5820},
    b'\x00\x00\x00\x00\xaf\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xcc': {
        'unused_8': 0, 'unused_16': 2945449992, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1996},
    b'\x00\x00\x00\x00\xaf\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xc8': {
        'unused_8': 0, 'unused_16': 2949644297, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1736},
    b'\x00\x00\x00\x00\xaf`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06X': {
        'unused_8': 0, 'unused_16': 2942304265, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1624},
    b'\x00\x00\x00\x00\xb00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc4': {
        'unused_8': 0, 'unused_16': 2955935753, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 964},
    b'\x00\x00\x00\x00\xb0\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\n\x94': {
        'unused_8': 0, 'unused_16': 2965372936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2708},
    b'\x00\x00\x00\x00\xb1\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x88': {
        'unused_8': 0, 'unused_16': 2979004424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1160},
    b'\x00\x00\x00\x00\xb2 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc4': {
        'unused_8': 0, 'unused_16': 2988441609, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1220},
    b'\x00\x00\x00\x00\xb2\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01x': {
        'unused_8': 0, 'unused_16': 2986344456, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 376},
    b'\x00\x00\x00\x00\xb2\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc4': {
        'unused_8': 0, 'unused_16': 2996830217, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1220},
    b'\x00\x00\x00\x00\xb2\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x88': {
        'unused_8': 0, 'unused_16': 2999975945, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1160},
    b'\x00\x00\x00\x00\xb2p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x00': {
        'unused_8': 0, 'unused_16': 2993684489, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1280},
    b'\x00\x00\x00\x00\xb3\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 0, 'unused_16': 3013607432, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x00\x00\x00\x00\xb4`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc4': {
        'unused_8': 0, 'unused_16': 3026190344, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 964},
    b'\x00\x00\x00\x00\xb5\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07D': {
        'unused_8': 0, 'unused_16': 3048210440, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1860},
    b'\x00\x00\x00\x00\xb8\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\x14': {
        'unused_8': 0, 'unused_16': 3096444936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2836},
    b'\x00\x00\x00\x00\xba\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 3136290824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\xbag\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xd8': {
        'unused_8': 0, 'unused_16': 3127312390, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 216},
    b'\x00\x00\x00\x00\xbc\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xfc': {
        'unused_8': 0, 'unused_16': 3162505224, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1532},
    b'\x00\x00\x00\x00\xbc\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 3163553800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\xbc\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x8c': {
        'unused_8': 0, 'unused_16': 3166699529, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1676},
    b'\x00\x00\x00\x00\xbdP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04l': {
        'unused_8': 0, 'unused_16': 3176136712, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1132},
    b'\x00\x00\x00\x00\xbe\xb6\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04l': {
        'unused_8': 0, 'unused_16': 3199598599, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1132},
    b'\x00\x00\x00\x00\xbe\xfb\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03|': {
        'unused_8': 0, 'unused_16': 3204120583, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 892},
    b'\x00\x00\x00\x00\xbf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf8': {
        'unused_8': 0, 'unused_16': 3207593993, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1016},
    b'\x00\x00\x00\x00\xbf@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xf8': {
        'unused_8': 0, 'unused_16': 3208642568, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 248},
    b'\x00\x00\x00\x00\xbf\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\xf0': {
        'unused_8': 0, 'unused_16': 3212836872, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3056},
    b'\x00\x00\x00\x00\xbf`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x14x': {
        'unused_8': 0, 'unused_16': 3210739720, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5240},
    b'\x00\x00\x00\x00\xc2P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04@': {
        'unused_8': 0, 'unused_16': 3260022793, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1088},
    b'\x00\x00\x00\x00\xc2\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xc4': {
        'unused_8': 0, 'unused_16': 3254779912, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1476},
    b'\x00\x00\x00\x00\xc3\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x14': {
        'unused_8': 0, 'unused_16': 3280994313, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 788},
    b'\x00\x00\x00\x00\xc3`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\n\xf0': {
        'unused_8': 0, 'unused_16': 3277848585, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2800},
    b'\x00\x00\x00\x00\xc4\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x18': {
        'unused_8': 0, 'unused_16': 3299868680, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1048},
    b'\x00\x00\x00\x00\xc5\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xf8': {
        'unused_8': 0, 'unused_16': 3306160136, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1272},
    b'\x00\x00\x00\x00\xc5\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 0, 'unused_16': 3319791625, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'\x00\x00\x00\x00\xc5`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x0c': {
        'unused_8': 0, 'unused_16': 3311403017, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2060},
    b'\x00\x00\x00\x00\xc6P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x84': {
        'unused_8': 0, 'unused_16': 3327131656, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1412},
    b'\x00\x00\x00\x00\xc6\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08(': {
        'unused_8': 0, 'unused_16': 3333423113, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2088},
    b'\x00\x00\x00\x00\xc6\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04T': {
        'unused_8': 0, 'unused_16': 3337617417, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1108},
    b'\x00\x00\x00\x00\xc7P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xfc': {
        'unused_8': 0, 'unused_16': 3343908873, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1788},
    b'\x00\x00\x00\x00\xc9@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 3376414729, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\xce\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xa4': {
        'unused_8': 0, 'unused_16': 3467640840, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 420},
    b'\x00\x00\x00\x00\xd0\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 3489660936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\xd2\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc0': {
        'unused_8': 0, 'unused_16': 3538944009, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 960},
    b'\x00\x00\x00\x00\xd3\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 3552575496, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xd3\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 3554672648, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xd3\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 3555721224, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xd5 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x02L': {
        'unused_8': 0, 'unused_16': 3575644169, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 588},
    b'\x00\x00\x00\x00\xd5\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\\': {
        'unused_8': 0, 'unused_16': 3587178504, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1116},
    b'\x00\x00\x00\x00\xd7p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07h': {
        'unused_8': 0, 'unused_16': 3614441481, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1896},
    b'\x00\x00\x00\x00\xd9p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08h': {
        'unused_8': 0, 'unused_16': 3647995913, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2152},
    b'\x00\x00\x00\x00\xda\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08P': {
        'unused_8': 0, 'unused_16': 3658481672, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2128},
    b'\x00\x00\x00\x00\xdd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 3710910472, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xdd\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x90': {
        'unused_8': 0, 'unused_16': 3707764745, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1936},
    b'\x00\x00\x00\x00\xdf\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 0, 'unused_16': 3754950664, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x00\x00\x00\x00\xe0\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03T': {
        'unused_8': 0, 'unused_16': 3766485001, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 852},
    b'\x00\x00\x00\x00\xe6@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x0c': {
        'unused_8': 0, 'unused_16': 3862953993, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1548},
    b'\x00\x00\x00\x00\xe6\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xc4': {
        'unused_8': 0, 'unused_16': 3872391177, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 452},
    b'\x00\x00\x00\x00\xe6\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe0': {
        'unused_8': 0, 'unused_16': 3874488328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1248},
    b'\x00\x00\x00\x00\xe6`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x10': {
        'unused_8': 0, 'unused_16': 3865051145, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1296},
    b'\x00\x00\x00\x00\xe7P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05d': {
        'unused_8': 0, 'unused_16': 3880779785, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1380},
    b'\x00\x00\x00\x00\xe7P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03 ': {
        'unused_8': 0, 'unused_16': 3880779784, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 800},
    b'\x00\x00\x00\x00\xe7\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf8': {
        'unused_8': 0, 'unused_16': 3888119816, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1016},
    b'\x00\x00\x00\x00\xe7\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\\': {
        'unused_8': 0, 'unused_16': 3889168392, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1116},
    b'\x00\x00\x00\x00\xe7\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 3890216968, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\xe7`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x90': {
        'unused_8': 0, 'unused_16': 3881828361, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1680},
    b'\x00\x00\x00\x00\xe8@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc8': {
        'unused_8': 0, 'unused_16': 3896508424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1224},
    b'\x00\x00\x00\x00\xe8p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\r@': {
        'unused_8': 0, 'unused_16': 3899654152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3392},
    b'\x00\x00\x00\x00\xe9 \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x98': {
        'unused_8': 0, 'unused_16': 3911188488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1176},
    b'\x00\x00\x00\x00\xe9@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03p': {
        'unused_8': 0, 'unused_16': 3913285641, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 880},
    b'\x00\x00\x00\x00\xe9@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 0, 'unused_16': 3913285640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x00\x00\x00\x00\xe9P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05$': {
        'unused_8': 0, 'unused_16': 3914334216, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1316},
    b'\x00\x00\x00\x00\xe9\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 0, 'unused_16': 3909091336, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x00\x00\x00\x00\xe9\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x88': {
        'unused_8': 0, 'unused_16': 3919577096, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1928},
    b'\x00\x00\x00\x00\xe9\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07`': {
        'unused_8': 0, 'unused_16': 3920625672, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1888},
    b'\x00\x00\x00\x00\xe9\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x9c': {
        'unused_8': 0, 'unused_16': 3921674248, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 924},
    b'\x00\x00\x00\x00\xe9\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x9c': {
        'unused_8': 0, 'unused_16': 3922722824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1948},
    b'\x00\x00\x00\x00\xe9p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03 ': {
        'unused_8': 0, 'unused_16': 3916431368, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 800},
    b'\x00\x00\x00\x00\xea@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd8': {
        'unused_8': 0, 'unused_16': 3930062856, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 984},
    b'\x00\x00\x00\x00\xea\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x00': {
        'unused_8': 0, 'unused_16': 3926917128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1536},
    b'\x00\x00\x00\x00\xea\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05P': {
        'unused_8': 0, 'unused_16': 3936354312, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1360},
    b'\x00\x00\x00\x00\xea\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 0, 'unused_16': 3939500041, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x00\x00\x00\x00\xeap\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x1c': {
        'unused_8': 0, 'unused_16': 3933208584, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1052},
    b'\x00\x00\x00\x00\xeb\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05 ': {
        'unused_8': 0, 'unused_16': 3952082952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1312},
    b'\x00\x00\x00\x00\xeb\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xb4': {
        'unused_8': 0, 'unused_16': 3953131529, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2228},
    b'\x00\x00\x00\x00\xeb\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 3953131528, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\xeb\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x94': {
        'unused_8': 0, 'unused_16': 3954180104, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1940},
    b'\x00\x00\x00\x00\xeb\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04<': {
        'unused_8': 0, 'unused_16': 3956277256, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1084},
    b'\x00\x00\x00\x00\xeb\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 3958374408, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00\xec \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 0, 'unused_16': 3961520136, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x00\x00\x00\x00\xec0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf8': {
        'unused_8': 0, 'unused_16': 3962568712, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1016},
    b'\x00\x00\x00\x00\xecP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc4': {
        'unused_8': 0, 'unused_16': 3964665864, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1220},
    b'\x00\x00\x00\x00\xec\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x00': {
        'unused_8': 0, 'unused_16': 3967811593, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1536},
    b'\x00\x00\x00\x00\xec\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xc0': {
        'unused_8': 0, 'unused_16': 3967811592, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1728},
    b'\x00\x00\x00\x00\xec\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x054': {
        'unused_8': 0, 'unused_16': 3969908744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1332},
    b'\x00\x00\x00\x00\xec\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x04': {
        'unused_8': 0, 'unused_16': 3973054472, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1540},
    b'\x00\x00\x00\x00\xec`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x0c': {
        'unused_8': 0, 'unused_16': 3965714440, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1548},
    b'\x00\x00\x00\x00\xecp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05p': {
        'unused_8': 0, 'unused_16': 3966763016, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1392},
    b'\x00\x00\x00\x00\xed`\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 0, 'unused_16': 3982491658, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x00\x00\x00\x00\xee\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xd8': {
        'unused_8': 0, 'unused_16': 3994025993, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 472},
    b'\x00\x00\x00\x00\xee\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06p': {
        'unused_8': 0, 'unused_16': 4001366025, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1648},
    b'\x00\x00\x00\x00\xf1P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x14': {
        'unused_8': 0, 'unused_16': 4048551944, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1044},
    b'\x00\x00\x00\x00\xf1\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 4053794824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00\xf1\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 4054843400, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00\xf2\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04D': {
        'unused_8': 0, 'unused_16': 4069523465, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1092},
    b'\x00\x00\x00\x00\xf2\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08T': {
        'unused_8': 0, 'unused_16': 4071620617, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2132},
    b'\x00\x00\x00\x00\xf5\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08X': {
        'unused_8': 0, 'unused_16': 4111466505, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2136},
    b'\x00\x00\x00\x00\xf60\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03|': {
        'unused_8': 0, 'unused_16': 4130340873, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 892},
    b'\x00\x00\x00\x00\xf60\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x18': {
        'unused_8': 0, 'unused_16': 4130340872, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1560},
    b'\x00\x00\x00\x00\xf6P\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xf4': {
        'unused_8': 0, 'unused_16': 4132438024, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1268},
    b'\x00\x00\x00\x00\xf6\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x050': {
        'unused_8': 0, 'unused_16': 4135583753, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1328},
    b'\x00\x00\x00\x00\xf7\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xb8': {
        'unused_8': 0, 'unused_16': 4145020937, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1720},
    b'\x00\x00\x00\x00\xf7\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x078': {
        'unused_8': 0, 'unused_16': 4156555272, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1848},
    b'\x00\x00\x00\x00\xf9@\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd4': {
        'unused_8': 0, 'unused_16': 4181721098, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1236},
    b'\x00\x00\x00\x00\xf9P\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc4': {
        'unused_8': 0, 'unused_16': 4182769674, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1220},
    b'\x00\x00\x00\x00\xf9\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xdc': {
        'unused_8': 0, 'unused_16': 4178575368, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1500},
    b'\x00\x00\x00\x00\xf9\x80\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 0, 'unused_16': 4185915402, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x00\x00\x00\x00\xf9\x90\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x00': {
        'unused_8': 0, 'unused_16': 4186963978, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1280},
    b'\x00\x00\x00\x00\xf9\xa0\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 4188012554, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xf9\xb0\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 4189061130, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xf9\xd0\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 4191158282, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xf9\xe0\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 4192206858, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xf9\xf0\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 4193255434, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00\xf9`\x00\n\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x00': {
        'unused_8': 0, 'unused_16': 4183818250, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1280},
    b'\x00\x00\x00\x00\xfa\xd0\x00\x04\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 4207935492, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00\xfa\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03l': {
        'unused_8': 0, 'unused_16': 4207935496, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 876},
    b'\x00\x00\x00\x00\xfa\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 4210032648, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x00\xfb@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04h': {
        'unused_8': 0, 'unused_16': 4215275528, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1128},
    b'\x00\x00\x00\x00\xfb\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xf8': {
        'unused_8': 0, 'unused_16': 4219469832, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1784},
    b'\x00\x00\x00\x00\xfc@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03(': {
        'unused_8': 0, 'unused_16': 4232052744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 808},
    b'\x00\x00\x00\x00\xfc\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x88': {
        'unused_8': 0, 'unused_16': 4236247048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1160},
    b'\x00\x00\x00\x00\xfc\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xf0': {
        'unused_8': 0, 'unused_16': 4237295624, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1520},
    b'\x00\x00\x00\x00\xfc\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xd0': {
        'unused_8': 0, 'unused_16': 4243587080, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1488},
    b'\x00\x00\x00\x00\xfe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x80': {
        'unused_8': 0, 'unused_16': 4264558600, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2176},
    b'\x00\x00\x00\x00\xfe\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xc8': {
        'unused_8': 0, 'unused_16': 4276092936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1480},
    b'\x00\x00\x00\x00\xffP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x88': {
        'unused_8': 0, 'unused_16': 4283432968, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1160},
    b'\x00\x00\x00\x00\xff\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03h': {
        'unused_8': 0, 'unused_16': 4289724424, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 872},
    b'\x00\x00\x00\x00\xff`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07h': {
        'unused_8': 0, 'unused_16': 4284481544, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1896},
    b'\x00\x00\x00\x00]0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02l': {
        'unused_8': 0, 'unused_16': 1563426824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 620},
    b'\x00\x00\x00\x00^\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x14': {
        'unused_8': 0, 'unused_16': 1592786953, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1300},
    b'\x00\x00\x00\x00_\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 0, 'unused_16': 1593835529, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x00\x00\x00\x00_\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x9c': {
        'unused_8': 0, 'unused_16': 1607467016, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2204},
    b'\x00\x00\x00\x00_\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xb8': {
        'unused_8': 0, 'unused_16': 1608515592, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2232},
    b'\x00\x00\x00\x00`0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x11\xbc': {
        'unused_8': 0, 'unused_16': 1613758472, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4540},
    b'\x00\x00\x00\x00`@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\\': {
        'unused_8': 0, 'unused_16': 1614807049, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1628},
    b'\x00\x00\x00\x00`@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\nP': {
        'unused_8': 0, 'unused_16': 1614807048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2640},
    b'\x00\x00\x00\x00`\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\xd8': {
        'unused_8': 0, 'unused_16': 1610612744, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2520},
    b'\x00\x00\x00\x00`\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\xb0': {
        'unused_8': 0, 'unused_16': 1611661320, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2480},
    b'\x00\x00\x00\x00a\x80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xd4': {
        'unused_8': 0, 'unused_16': 1635778569, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1492},
    b'\x00\x00\x00\x00a\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xfc': {
        'unused_8': 0, 'unused_16': 1639972872, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1532},
    b'\x00\x00\x00\x00a\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x9c': {
        'unused_8': 0, 'unused_16': 1643118601, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2204},
    b'\x00\x00\x00\x00a\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd8': {
        'unused_8': 0, 'unused_16': 1643118600, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1240},
    b'\x00\x00\x00\x00b\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 0, 'unused_16': 1645215752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x00\x00\x00\x00c\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xf0': {
        'unused_8': 0, 'unused_16': 1673527304, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1520},
    b'\x00\x00\x00\x00d\x00\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01<': {
        'unused_8': 0, 'unused_16': 1677721606, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 316},
    b'\x00\x00\x00\x00f\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc4': {
        'unused_8': 0, 'unused_16': 1720713224, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 964},
    b'\x00\x00\x00\x00g0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 0, 'unused_16': 1731198984, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x00\x00\x00\x00g\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xa4': {
        'unused_8': 0, 'unused_16': 1737490440, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1700},
    b'\x00\x00\x00\x00g\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xe4': {
        'unused_8': 0, 'unused_16': 1740636168, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2276},
    b'\x00\x00\x00\x00h0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xf4': {
        'unused_8': 0, 'unused_16': 1747976200, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 756},
    b'\x00\x00\x00\x00i`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05L': {
        'unused_8': 0, 'unused_16': 1767899144, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1356},
    b'\x00\x00\x00\x00j\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\\': {
        'unused_8': 0, 'unused_16': 1788870664, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1628},
    b'\x00\x00\x00\x00j\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\n\xfc': {
        'unused_8': 0, 'unused_16': 1790967817, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2812},
    b'\x00\x00\x00\x00k\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08 ': {
        'unused_8': 0, 'unused_16': 1806696456, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2080},
    b'\x00\x00\x00\x00k`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xdc': {
        'unused_8': 0, 'unused_16': 1801453576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 988},
    b'\x00\x00\x00\x00l@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06X': {
        'unused_8': 0, 'unused_16': 1816133641, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1624},
    b'\x00\x00\x00\x00l\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07|': {
        'unused_8': 0, 'unused_16': 1827667977, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1916},
    b'\x00\x00\x00\x00n\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 0, 'unused_16': 1860173833, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x00\x00\x00\x00p@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\x0c': {
        'unused_8': 0, 'unused_16': 1883242505, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2828},
    b'\x00\x00\x00\x00p\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\t@': {
        'unused_8': 0, 'unused_16': 1892679689, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2368},
    b'\x00\x00\x00\x00q\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x0c': {
        'unused_8': 0, 'unused_16': 1905262600, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1548},
    b'\x00\x00\x00\x00q\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xe4': {
        'unused_8': 0, 'unused_16': 1906311177, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2020},
    b'\x00\x00\x00\x00q\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 0, 'unused_16': 1908408328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x00\x00\x00q\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x048': {
        'unused_8': 0, 'unused_16': 1909456905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1080},
    b'\x00\x00\x00\x00qp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd0': {
        'unused_8': 0, 'unused_16': 1903165448, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 976},
    b'\x00\x00\x00\x00s\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 0, 'unused_16': 1943011337, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x00\x00\x00\x00s\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xac': {
        'unused_8': 0, 'unused_16': 1945108488, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1964},
    b'\x00\x00\x00\x00t\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\nD': {
        'unused_8': 0, 'unused_16': 1947205641, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2628},
    b'\x00\x00\x00\x00tp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 0, 'unused_16': 1953497096, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x00\x00\x00\x00u\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 0, 'unused_16': 1962934281, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x00\x00\x00\x00u\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 0, 'unused_16': 1962934280, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x00\x00\x00\x00u\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08L': {
        'unused_8': 0, 'unused_16': 1976565768, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2124},
    b'\x00\x00\x00\x00vP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\x1c': {
        'unused_8': 0, 'unused_16': 1984954376, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2332},
    b'\x00\x00\x00\x00v\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01l': {
        'unused_8': 0, 'unused_16': 1980760072, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 364},
    b'\x00\x00\x00\x00wP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\\': {
        'unused_8': 0, 'unused_16': 2001731592, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1884},
    b'\x00\x00\x00\x00w\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05@': {
        'unused_8': 0, 'unused_16': 1996488713, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1344},
    b'\x00\x00\x00\x00w\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x90': {
        'unused_8': 0, 'unused_16': 2010120201, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1168},
    b'\x00\x00\x00\x00x\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x84': {
        'unused_8': 0, 'unused_16': 2023751688, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1924},
    b'\x00\x00\x00\x00y\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\x10': {
        'unused_8': 0, 'unused_16': 2041577480, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2320},
    b'\x00\x00\x00\x00{`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x0c': {
        'unused_8': 0, 'unused_16': 2069889032, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1804},
    b'\x00\x00\x00\x00{p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x0c': {
        'unused_8': 0, 'unused_16': 2070937608, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1804},
    b'\x00\x00\x00\x00|\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 0, 'unused_16': 2089811976, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'\x00\x00\x00\x01\xb8\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03T': {
        'unused_8': 1, 'unused_16': 3088056329, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 852},
    b'\x00\x00\x00\x10\xb3\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 16, 'unused_16': 3014656008, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x00\x00\x03\x00hP\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00-\xa8': {
        'unused_8': 768, 'unused_16': 1750073353, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 11688},
    b'\x00\x01\x00\x02T\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07`': {
        'unused_8': 65538, 'unused_16': 1409286152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1888},
    b'\x00\x04\x00\x00\xc7\xc0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06t': {
        'unused_8': 262144, 'unused_16': 3351248905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1652},
    b'\x00\x89\x85\xe4\xcb\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x8c': {
        'unused_8': 9012708, 'unused_16': 3418357768, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 652},
    b'\x00\x96\x9c\xa8J \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 9870504, 'unused_16': 1243611144, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x96\x9c\xa8\x9f \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 9870504, 'unused_16': 2669674504, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x00\x96\x9c\xa8k\x04\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x01x': {
        'unused_8': 9870504, 'unused_16': 1795424263, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 376},
    b'\x00\x98\xdf\xb8,\xb0\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x01x': {
        'unused_8': 10018744, 'unused_16': 749731847, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 376},
    b'\x00\xff\xff\x00\xfb@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 16776960, 'unused_16': 4215275528, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x00i\x00\x13\xfb\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x94': {
        'unused_8': 6881299, 'unused_16': 4220518408, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1684},
    b'\x00|<\xd0\x85\x9e\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xd8': {
        'unused_8': 8142032, 'unused_16': 2241724422, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 216},
    b'\x00|<\xd0\xdb\x13\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xd8': {
        'unused_8': 8142032, 'unused_16': 3675455494, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 216},
    b'\x00|v\x14\xe2\x12\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x0c': {
        'unused_8': 8156692, 'unused_16': 3792830470, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 268},
    b'\x01D\x0bLJ\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 21236556, 'unused_16': 1256194056, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\x01\x00\x00\x00\xe0\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xdc': {
        'unused_8': 16777216, 'unused_16': 3773825032, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 988},
    b'\x01\x01\xff\xff\xdc@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xa4': {
        'unused_8': 16908287, 'unused_16': 3695181833, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1188},
    b'\x01\x069\x0c\xd7\x9a\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x18': {
        'unused_8': 17185036, 'unused_16': 3617193990, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 280},
    b'\x02\x00\x00\x00\xa5\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xb8': {
        'unused_8': 33554432, 'unused_16': 2769289225, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 696},
    b'\x02\x00\x00\x00\xb7p\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03d': {
        'unused_8': 33554432, 'unused_16': 3077570569, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 868},
    b'\x03\x00\x00\x00\xb3\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 50331648, 'unused_16': 3012558856, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x04\x00\x00\x00\xd0\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03H': {
        'unused_8': 67108864, 'unused_16': 3501195272, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 840},
    b'\x04\x00\x00\x00\xfbP\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06X': {
        'unused_8': 67108864, 'unused_16': 4216324104, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1624},
    b'\x06\x02\x80\x01\xb8 \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03t': {
        'unused_8': 100827137, 'unused_16': 3089104905, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 884},
    b'\x06\x02\x80\x01\xf9\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xac': {
        'unused_8': 100827137, 'unused_16': 4192206856, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1196},
    b'\x06~\xb3\x01\xbf\x88\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x05<': {
        'unused_8': 108966657, 'unused_16': 3213361159, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1340},
    b'\x07\x00\x04\x00\xa7\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x05X': {
        'unused_8': 117441536, 'unused_16': 2811232265, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1368},
    b'\x08\x00\x00\x00\xa8\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 134217728, 'unused_16': 2832203785, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'\x08\x00\x00\x00r@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xe4': {
        'unused_8': 134217728, 'unused_16': 1916796936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2020},
    b'\x0c\x11 \x00\\B\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 202448896, 'unused_16': 1547829255, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'\x0c\x11 \x00\nL\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\nd': {
        'unused_8': 202448896, 'unused_16': 172752902, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2660},
    b'\x0c\x11 \x00\t\xd9\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xac': {
        'unused_8': 202448896, 'unused_16': 165216262, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1452},
    b'\x0c\x11 \x00\x8f[\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x0c\xb8': {
        'unused_8': 202448896, 'unused_16': 2405105670, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3256},
    b'\x0c\x11 \x00\xbf\xa3\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x05\\': {
        'unused_8': 202448896, 'unused_16': 3215130631, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1372},
    b'\x0c\x11 \x00\xc3\x8f\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\tT': {
        'unused_8': 202448896, 'unused_16': 3280928775, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2388},
    b'\x0c\x11 \x00a"\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0bD': {
        'unused_8': 202448896, 'unused_16': 1629618183, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2884},
    b'\x0c\x11 \x00a.\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x00': {
        'unused_8': 202448896, 'unused_16': 1630404615, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1536},
    b'\x10\x00\x00\x00\xb80\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 268435456, 'unused_16': 3090153481, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x13err\xa8\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xf0': {
        'unused_8': 325415538, 'unused_16': 2819620873, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1264},
    b'\x14Nat\x920\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xb4': {
        'unused_8': 340681076, 'unused_16': 2452619272, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1716},
    b'\x80d\xb5\x00\n\xb0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\rX': {
        'unused_8': 2154083584, 'unused_16': 179306504, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3416},
    b'\x80d\xe8\x00\xed\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xf0': {
        'unused_8': 2154096640, 'unused_16': 3977248777, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 752},
    b'\x840\xc0\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xf8': {
        'unused_8': 2217787394, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1528},
    b'\x84\x00\x15\x00\xea\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x14': {
        'unused_8': 2214597888, 'unused_16': 3937402889, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 788},
    b'\x84\xd0\xa8\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc8': {
        'unused_8': 2228267010, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 968},
    b'\x84p&\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x038': {
        'unused_8': 2221942274, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 824},
    b'\x84p+\x02\x10\xd6\xba\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x1c': {
        'unused_8': 2221943554, 'unused_16': 282507920, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 796},
    b'\x84p2\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x024': {
        'unused_8': 2221945346, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 564},
    b'\x84pA\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x02\\': {
        'unused_8': 2221949186, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 604},
    b'\x84p\x82\x01\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 2221965825, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x84p\x87\x01\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x02|': {
        'unused_8': 2221967105, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 636},
    b'\x84p\x92\x01\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x8c': {
        'unused_8': 2221969921, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 908},
    b'\x84p\x93\x01\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x02d': {
        'unused_8': 2221970177, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 612},
    b'\x84p\x94\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02h': {
        'unused_8': 2221970433, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 616},
    b'\x84p\x96\x01\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x84': {
        'unused_8': 2221970945, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 644},
    b'\x84p\x9f\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd0': {
        'unused_8': 2221973250, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1232},
    b'\x84p\xb3\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02h': {
        'unused_8': 2221978369, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 616},
    b'\x84p\xc4\x00\x10\xc7\xf8 \x00\x00\x00 \x00\x00\x004\x00\x00\x03L': {
        'unused_8': 2221982720, 'unused_16': 281540640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 844},
    b'\x84p\xc6\x00\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xc8': {
        'unused_8': 2221983232, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 712},
    b'\x84p\xc7\x00\x11!\x93\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf4': {
        'unused_8': 2221983488, 'unused_16': 287413008, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1012},
    b'\x84p\xca\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03L': {
        'unused_8': 2221984256, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 844},
    b'\x84p\xcb\x00\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03L': {
        'unused_8': 2221984512, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 844},
    b'\x84p\xcd\x00\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 2221985024, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'\x84p\xcd\x00\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xa4': {
        'unused_8': 2221985024, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 676},
    b'\x84p\xcf\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x07x': {
        'unused_8': 2221985536, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1912},
    b'\x84p\xd0\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x06|': {
        'unused_8': 2221985792, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1660},
    b'\x88%\xd5\x00\xa5\xc2\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xbc': {
        'unused_8': 2284180736, 'unused_16': 2780954630, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1980},
    b'\x88d\x05\x01\x16\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x10h': {
        'unused_8': 2288256257, 'unused_16': 378535944, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4200},
    b'\x88p#\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\n8': {
        'unused_8': 2289050370, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2616},
    b'\x88p/\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\n\xec': {
        'unused_8': 2289053442, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2796},
    b'\x88p2\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03d': {
        'unused_8': 2289054210, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 868},
    b'\x88p;\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x0b\xa0': {
        'unused_8': 2289056514, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2976},
    b'\x88p<\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x0b<': {
        'unused_8': 2289056770, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2876},
    b'\x88p>\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x06h': {
        'unused_8': 2289057282, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1640},
    b'\x88p@\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf0': {
        'unused_8': 2289057794, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1008},
    b'\x88pK\x02\x10\xd6\xaa\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xdc': {
        'unused_8': 2289060610, 'unused_16': 282503824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1244},
    b'\x88p\x7f\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc0': {
        'unused_8': 2289073922, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 960},
    b'\x88p\x80\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x04': {
        'unused_8': 2289074178, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1796},
    b'\x88p\x85\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\n8': {
        'unused_8': 2289075458, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2616},
    b'\x88p\x8c\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04T': {
        'unused_8': 2289077250, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1108},
    b'\x88p\x91\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xfc': {
        'unused_8': 2289078530, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1532},
    b'\x88p\x96\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x9c': {
        'unused_8': 2289079810, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1180},
    b'\x88p\x98\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x9c': {
        'unused_8': 2289080322, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1180},
    b'\x88p\xa7\x01\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xec': {
        'unused_8': 2289084161, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1772},
    b'\x88p\xa8\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe0': {
        'unused_8': 2289084418, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 992},
    b'\x88p\xac\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe8': {
        'unused_8': 2289085442, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1000},
    b'\x88p\xb2\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\t\xfc': {
        'unused_8': 2289086978, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2556},
    b'\x88p\xb3\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x9c': {
        'unused_8': 2289087234, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1180},
    b'\x88p\xcc\x00\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xec': {
        'unused_8': 2289093632, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1004},
    b'\x88p\xcf\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x05<': {
        'unused_8': 2289094402, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1340},
    b'\x88pa\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 2289066242, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'\x88pj\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xac': {
        'unused_8': 2289068546, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 940},
    b'\x88pr\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xb0': {
        'unused_8': 2289070594, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1200},
    b'\x88pv\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x04(': {
        'unused_8': 2289071618, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1064},
    b'\x88pw\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03H': {
        'unused_8': 2289071874, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 840},
    b'\x8cd\xc6\x00Q\x90\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 2355414528, 'unused_16': 1368391689, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x8cd\xc6\x00\x87\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 2355414528, 'unused_16': 2274361352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x8cd\xc6\x00\x8a\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 2355414528, 'unused_16': 2329935881, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x8cd\xc6\x00\xcc\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x18': {
        'unused_8': 2355414528, 'unused_16': 3423600648, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 280},
    b'\x8cd\xc6\x00n\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 2355414528, 'unused_16': 1846542344, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x8cd\xc6\x00o0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 2355414528, 'unused_16': 1865416712, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'\x8cp$\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x06T': {
        'unused_8': 2356159490, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1620},
    b'\x8cp$\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03X': {
        'unused_8': 2356159490, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 856},
    b'\x8cp&\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x18': {
        'unused_8': 2356160002, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1048},
    b'\x8cp)\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 2356160770, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'\x8cp,\x02\x10\xd6\xba\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03d': {
        'unused_8': 2356161538, 'unused_16': 282507920, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 868},
    b'\x8cp.\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07L': {
        'unused_8': 2356162050, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1868},
    b'\x8cp0\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04T': {
        'unused_8': 2356162562, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1108},
    b'\x8cp1\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 2356162818, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x8cp3\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 2356163330, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x8cp4\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x04': {
        'unused_8': 2356163586, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1028},
    b'\x8cp5\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x08': {
        'unused_8': 2356163842, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1288},
    b'\x8cp9\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xe4': {
        'unused_8': 2356164866, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1508},
    b'\x8cp9\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x02H': {
        'unused_8': 2356164866, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 584},
    b'\x8cp;\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xd4': {
        'unused_8': 2356165378, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1748},
    b'\x8cp=\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x17X': {
        'unused_8': 2356165890, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5976},
    b'\x8cp@\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 2356166658, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'\x8cp@\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xdc': {
        'unused_8': 2356166658, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1500},
    b'\x8cpB\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07L': {
        'unused_8': 2356167170, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1868},
    b'\x8cpB\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf8': {
        'unused_8': 2356167170, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1016},
    b'\x8cpB\x02\x10\xd6\xaa\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 2356167170, 'unused_16': 282503824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x8cpD\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x04': {
        'unused_8': 2356167682, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1028},
    b'\x8cpF\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xb8': {
        'unused_8': 2356168194, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1208},
    b'\x8cpL\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x08': {
        'unused_8': 2356169730, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 776},
    b'\x8cpS\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07$': {
        'unused_8': 2356171522, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1828},
    b'\x8cpS\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 2356171522, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x8cp\\\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x078': {
        'unused_8': 2356173826, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1848},
    b'\x8cp\x08\x02\x10\xd6\xaa\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x98': {
        'unused_8': 2356152322, 'unused_16': 282503824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1176},
    b'\x8cp\x14\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xa8': {
        'unused_8': 2356155394, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1960},
    b'\x8cp\x17\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03l': {
        'unused_8': 2356156162, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 876},
    b'\x8cp\x1f\x02\x10\xc2\x8c0\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xb0': {
        'unused_8': 2356158210, 'unused_16': 281185328, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2224},
    b'\x8cp\x1f\x02\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03X': {
        'unused_8': 2356158210, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 856},
    b'\x8cp\x94\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd4': {
        'unused_8': 2356188162, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 980},
    b'\x8cp\xa3\x01\x10\xd6\xaa\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x0f\xec': {
        'unused_8': 2356192001, 'unused_16': 282503824, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 4076},
    b'\x8cp\xcb\x00\x10\xcaS`\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x9c': {
        'unused_8': 2356202240, 'unused_16': 281695072, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 924},
    b'\x8cp\xcd\x00\x10\xcf@p\x00\x00\x00 \x00\x00\x004\x00\x00\x03P': {
        'unused_8': 2356202752, 'unused_16': 282017904, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 848},
    b'\x8cp\xd1\x02\x10\xd6\xba\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03<': {
        'unused_8': 2356203778, 'unused_16': 282507920, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 828},
    b'\x8cp\xdf\x01\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x08': {
        'unused_8': 2356207361, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 520},
    b'\x90p(\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x1c': {
        'unused_8': 2423269378, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 796},
    b'\x90p@\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 2423275522, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'\x90pB\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xb8': {
        'unused_8': 2423276034, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1208},
    b'\x90pC\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x05l': {
        'unused_8': 2423276290, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1388},
    b'\x90pK\x02\x10\xca\xccp\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xec': {
        'unused_8': 2423278338, 'unused_16': 281726064, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1260},
    b'\x90pY\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x030': {
        'unused_8': 2423281922, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 816},
    b'\x90pZ\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03P': {
        'unused_8': 2423282178, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 848},
    b'\x90p\x82\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xbc': {
        'unused_8': 2423292417, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 956},
    b'\x90p\x82\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x9c': {
        'unused_8': 2423292418, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1180},
    b'\x90p\x83\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x80': {
        'unused_8': 2423292673, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 896},
    b'\x90p\x84\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04$': {
        'unused_8': 2423292930, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1060},
    b'\x90p\x85\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x84': {
        'unused_8': 2423293185, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1156},
    b'\x90p\x85\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x048': {
        'unused_8': 2423293186, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1080},
    b'\x90p\x86\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x08': {
        'unused_8': 2423293442, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1032},
    b'\x90p\x88\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 2423293953, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'\x90p\x89\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd4': {
        'unused_8': 2423294210, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 980},
    b'\x90p\x8c\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xbc': {
        'unused_8': 2423294977, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 956},
    b'\x90p\x8d\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x9c': {
        'unused_8': 2423295234, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2204},
    b'\x90p\x8e\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 2423295489, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x90p\x8e\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04L': {
        'unused_8': 2423295490, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1100},
    b'\x90p\x90\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x8c': {
        'unused_8': 2423296002, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 652},
    b'\x90p\x95\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xd0': {
        'unused_8': 2423297281, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 976},
    b'\x90p\x96\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04H': {
        'unused_8': 2423297537, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1096},
    b'\x90p\x97\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc0': {
        'unused_8': 2423297793, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1216},
    b'\x90p\x9a\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x80': {
        'unused_8': 2423298561, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 896},
    b'\x90p\x9c\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 2423299073, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'\x90p\x9d\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd4': {
        'unused_8': 2423299329, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1236},
    b'\x90p\x9e\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04T': {
        'unused_8': 2423299585, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1108},
    b'\x90p\xa3\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf8': {
        'unused_8': 2423300865, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1016},
    b'\x90p\xa5\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04|': {
        'unused_8': 2423301377, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1148},
    b'\x90p\xa7\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x80': {
        'unused_8': 2423301889, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 896},
    b'\x90p\xa8\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 2423302145, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\x90p\xa9\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x044': {
        'unused_8': 2423302401, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1076},
    b'\x90p\xad\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03|': {
        'unused_8': 2423303426, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 892},
    b'\x90p\xb8\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe8': {
        'unused_8': 2423306241, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1000},
    b'\x90p\xbc\x01\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04l': {
        'unused_8': 2423307265, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1132},
    b'\x90p\xbf\x01\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xdc': {
        'unused_8': 2423308033, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 732},
    b'\x90p\xc4\x00\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xc0': {
        'unused_8': 2423309312, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 704},
    b'\x90p\xc7\x00\x11!\x93\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x048': {
        'unused_8': 2423310080, 'unused_16': 287413008, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1080},
    b'\x90p\xc8\x00\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xb0': {
        'unused_8': 2423310336, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 944},
    b'\x90p\xc8\x01\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03h': {
        'unused_8': 2423310337, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 872},
    b'\x90p\xc8\x01\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x08': {
        'unused_8': 2423310337, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 520},
    b'\x90p\xc9\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xa4': {
        'unused_8': 2423310592, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 932},
    b'\x90p\xca\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04x': {
        'unused_8': 2423310848, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1144},
    b'\x90p\xca\x01\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe4': {
        'unused_8': 2423310849, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 996},
    b'\x90p\xcb\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03L': {
        'unused_8': 2423311104, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 844},
    b'\x90p\xcc\x00\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe0': {
        'unused_8': 2423311360, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 992},
    b'\x90p\xcd\x00\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x03@': {
        'unused_8': 2423311616, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 832},
    b'\x90p\xce\x01\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04l': {
        'unused_8': 2423311873, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1132},
    b'\x90p\xd0\x00\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04l': {
        'unused_8': 2423312384, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1132},
    b'\x90p\xd1\x01\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xcc': {
        'unused_8': 2423312641, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 972},
    b'\x90p\xd2\x00\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x0c': {
        'unused_8': 2423312896, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1292},
    b'\x90p\xdc\x01\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x10': {
        'unused_8': 2423315457, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1040},
    b'\x90p\xde\x01\x10\xc8.\x90\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x10': {
        'unused_8': 2423315969, 'unused_16': 281554576, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1040},
    b'\x90p\xe4\x01\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xdc': {
        'unused_8': 2423317505, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 732},
    b'\x90pe\x02\x10\xca\xdd0\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x00': {
        'unused_8': 2423284994, 'unused_16': 281730352, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1280},
    b'\x90pp\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x98': {
        'unused_8': 2423287810, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 920},
    b'\x90pr\x02\x10\x85:0\x00\x00\x00 \x00\x00\x004\x00\x00\x03 ': {
        'unused_8': 2423288322, 'unused_16': 277166640, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 800},
    b'\x90py\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x04L': {
        'unused_8': 2423290114, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1100},
    b'\x90p|\x02\x10\x85a\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x04': {
        'unused_8': 2423290882, 'unused_16': 277176800, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 772},
    b'\x94d\xb5\x00/\x80\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xf8': {
        'unused_8': 2489627904, 'unused_16': 796917766, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 248},
    b'\x94d\xb5\x00/\x82\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xf8': {
        'unused_8': 2489627904, 'unused_16': 797048838, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 248},
    b'\xa8d\xb5\x00q\x94\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x88': {
        'unused_8': 2825172224, 'unused_16': 1905524743, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1160},
    b'\xb4\xe5\x15\x001\xd5\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3034912000, 'unused_16': 836042758, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xb6V\x03\nS \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00!\x08': {
        'unused_8': 3059090186, 'unused_16': 1394606089, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 8456},
    b'\xc1\x03\x00\x03\xea\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04 ': {
        'unused_8': 3238199299, 'unused_16': 3934257160, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1056},
    b'\xc4\x9a@\x0f\x9c\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07<': {
        'unused_8': 3298443279, 'unused_16': 2632974344, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1852},
    b'\xc8d\xb5\x00\xd9\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x1c': {
        'unused_8': 3362043136, 'unused_16': 3653238792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2076},
    b'\xccd\xb5\x00\x00\x00\x00\x16\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xd8': {
        'unused_8': 3429152000, 'unused_16': 22, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 216},
    b'\xcd\xcd\xcd\xcd\x05\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x90': {
        'unused_8': 3452816845, 'unused_16': 96469000, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1168},
    b'\xd0d\xb5\x00\x15\xca\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0bH': {
        'unused_8': 3496260864, 'unused_16': 365559815, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2888},
    b'\xd0d\xb5\x00p1\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x1c': {
        'unused_8': 3496260864, 'unused_16': 1882259463, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 796},
    b'\xd0d\xb5\x00p9\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06 ': {
        'unused_8': 3496260864, 'unused_16': 1882783751, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1568},
    b'\xd0d\xb5\x00p\xa9\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06@': {
        'unused_8': 3496260864, 'unused_16': 1890123783, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1600},
    b'\xd0d\xb5\x00p\xb7\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x07l': {
        'unused_8': 3496260864, 'unused_16': 1891041287, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1900},
    b'\xd8d\x06\x01\x83\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x88': {
        'unused_8': 3630433793, 'unused_16': 2209349641, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 648},
    b'\xd8d\xb5\x00\x00\x00\x00\x19\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xb8': {
        'unused_8': 3630478592, 'unused_16': 25, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 184},
    b'\xd8d\xb5\x00\x00\x00\x00\x1c\x00\x00\x00 \x00\x00\x004\x00\x00\x01<': {
        'unused_8': 3630478592, 'unused_16': 28, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 316},
    b'\xd8d\xb5\x00\x11\x13\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x05\xfc': {
        'unused_8': 3630478592, 'unused_16': 286457862, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1532},
    b'\xd8d\xb5\x00\x16I\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xa8': {
        'unused_8': 3630478592, 'unused_16': 373882886, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1704},
    b'\xd8d\xb5\x00\x1a\x96\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xdc': {
        'unused_8': 3630478592, 'unused_16': 446038022, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2268},
    b'\xd8d\xb5\x00\xcd\xf1\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xd8': {
        'unused_8': 3630478592, 'unused_16': 3455123462, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 472},
    b'\xd8d\xb5\x00\xd4\x81\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x0c': {
        'unused_8': 3630478592, 'unused_16': 3565223943, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1548},
    b'\xd8d\xb5\x00j\xd3\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xac': {
        'unused_8': 3630478592, 'unused_16': 1792212999, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2220},
    b'\xd8d\xb5\x00m&\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\n\x04': {
        'unused_8': 3630478592, 'unused_16': 1831206919, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2564},
    b'\xd8d\xb5\x00m1\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0f\x14': {
        'unused_8': 3630478592, 'unused_16': 1831927815, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3860},
    b'\xd8d\xb5\x00m\xc9\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x13\x98': {
        'unused_8': 3630478592, 'unused_16': 1841889287, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 5016},
    b'\xd8d\xb5\x00mj\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\r\x80': {
        'unused_8': 3630478592, 'unused_16': 1835663367, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3456},
    b'\xd8d\xb5\x00n\xd8\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0ed': {
        'unused_8': 3630478592, 'unused_16': 1859649543, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3684},
    b'\xd8d\xb5\x00n\xff\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0c\\': {
        'unused_8': 3630478592, 'unused_16': 1862205447, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3164},
    b'\xd8d\xb5\x00n`\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x070': {
        'unused_8': 3630478592, 'unused_16': 1851785223, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1840},
    b'\xd8d\xb5\x00no\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xcc': {
        'unused_8': 3630478592, 'unused_16': 1852768263, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 716},
    b'\xd8d\xb5\x00o\x1e\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0cT': {
        'unused_8': 3630478592, 'unused_16': 1864237063, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3156},
    b'\xd8d\xb5\x00od\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04$': {
        'unused_8': 3630478592, 'unused_16': 1868824583, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1060},
    b'\xd8d\xb5\x00pK\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x1c': {
        'unused_8': 3630478592, 'unused_16': 1883963399, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 796},
    b'\xd8d\xb5\x00pS\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04\\': {
        'unused_8': 3630478592, 'unused_16': 1884487687, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1116},
    b'\xd8d\xb5\x00p\xc0\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xf4': {
        'unused_8': 3630478592, 'unused_16': 1891631111, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1780},
    b'\xd8d\xb5\x00pu\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 3630478592, 'unused_16': 1886715911, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'\xd8d\xb5\x00q#\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\t\xdc': {
        'unused_8': 3630478592, 'unused_16': 1898119175, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2524},
    b'\xd8d\xb5\x00q\x8b\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xc8': {
        'unused_8': 3630478592, 'unused_16': 1904934919, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2248},
    b'\xd8d\xb5\x00q\x9b\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x0b(': {
        'unused_8': 3630478592, 'unused_16': 1905983495, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2856},
    b'\xd8d\xb5\x00qw\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03D': {
        'unused_8': 3630478592, 'unused_16': 1903624199, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 836},
    b'\xdd\x00\x00\x00\x00\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x064': {
        'unused_8': 3707764736, 'unused_16': 15728648, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1588},
    b'\xe0\x05\x15\x00w\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\nL': {
        'unused_8': 3758429440, 'unused_16': 2009071624, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2636},
    b'\xe8\x06\x15\x00N \x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 3892712704, 'unused_16': 1310720009, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'\xeb\xeb\xeb\xeb=\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 1031798792, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xeb\xeb\xeb\xebHp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 1215299592, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xeb\xeb\xeb\xebI\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 1238368264, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xeb\xeb\xeb\xeb\x01\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 26214408, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xeb\xeb\xeb\xeb\x1e\xe0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 517996553, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xeb\xeb\xeb\xeb\x9f\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 3958107115, 'unused_16': 2668625928, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'\xf4\xb5\x1f\x00\x00\x06]\xc4\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe8': {
        'unused_8': 4105510656, 'unused_16': 417220, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1000},
    b'\xf4\xb5\x1f\x00\x8a\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe4': {
        'unused_8': 4105510656, 'unused_16': 2327838728, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1252},
    b'\xf4\xb5\x1f\x00\xbbP\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xe4': {
        'unused_8': 4105510656, 'unused_16': 3142582281, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1252},
    b'\xf6\xff\x1a\x02\xf5\xab\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x05(': {
        'unused_8': 4143913474, 'unused_16': 4121624582, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1320},
    b'\xff\xff\xff\x00c@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0b`': {
        'unused_8': 4294967040, 'unused_16': 1665138696, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2912},
    b'\xff\xff\xff\xff[p\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04,': {
        'unused_8': 4294967295, 'unused_16': 1534066696, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1068},
    b'\xff\xff\xff\xff\xbf7\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x06\xc4': {
        'unused_8': 4294967295, 'unused_16': 3208052743, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1732},
    b'`d\x04\x01W\x90\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\r\x04': {
        'unused_8': 1617167361, 'unused_16': 1469054984, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3332},
    b'`d\x04\x01\x17\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\t\x08': {
        'unused_8': 1617167361, 'unused_16': 401604617, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2312},
    b'`d\x04\x01\xa5\xdd\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x03 ': {
        'unused_8': 1617167361, 'unused_16': 2782724102, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 800},
    b'`d\x04\x01\xa5\xeb\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x94': {
        'unused_8': 1617167361, 'unused_16': 2783641606, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 660},
    b'`d\x04\x01\xa6\x13\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\n\xac': {
        'unused_8': 1617167361, 'unused_16': 2786263046, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2732},
    b'`d\x04\x01\xbd\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03|': {
        'unused_8': 1617167361, 'unused_16': 3179282440, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 892},
    b'`d\x04\x01\xbe`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xdc': {
        'unused_8': 1617167361, 'unused_16': 3193962504, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 732},
    b'`pY\x01\x10E3\x10\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x9c': {
        'unused_8': 1617975553, 'unused_16': 272970512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 668},
    b'`p\xa7\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x05@': {
        'unused_8': 1617995520, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1344},
    b'`p\xd9\x00\x10E\xdb\xe8\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x18': {
        'unused_8': 1618008320, 'unused_16': 273013736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1048},
    b'`p\xf9\x00\x10E\xbc\xa8\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xa0': {
        'unused_8': 1618016512, 'unused_16': 273005736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 416},
    b'`p\xfc\x00\x10E\xbc\xa8\x00\x00\x00 \x00\x00\x004\x00\x00\x02$': {
        'unused_8': 1618017280, 'unused_16': 273005736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 548},
    b'abVI\x92\n\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x01X': {
        'unused_8': 1633834569, 'unused_16': 2450128902, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 344},
    b'alle\xb7\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 1634495589, 'unused_16': 3080716297, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'b\x00\x00\x00-\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 1644167168, 'unused_16': 766509065, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'b\x00\x00\x003\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x10': {
        'unused_8': 1644167168, 'unused_16': 868220936, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1040},
    b'b\x00\x00\x00C\x93\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x02l': {
        'unused_8': 1644167168, 'unused_16': 1133707271, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 620},
    b'b\x00\x00\x00C\xb7\x00\x07\x00\x00\x00 \x00\x00\x004\x00\x00\x03t': {
        'unused_8': 1644167168, 'unused_16': 1136066567, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 884},
    b'b\x00\x00\x00H[\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xe4': {
        'unused_8': 1644167168, 'unused_16': 1213923334, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2020},
    b'b\x00\x00\x00I\x06\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x0c': {
        'unused_8': 1644167168, 'unused_16': 1225129990, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1036},
    b'b\x00\x00\x00I\x0f\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 1644167168, 'unused_16': 1225719814, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'b\x00\x00\x00X\xd0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x04': {
        'unused_8': 1644167168, 'unused_16': 1490026505, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1540},
    b'b\x00\x00\x00\x00\x07\xe0\xb2\x00\x00\x00 \x00\x00\x004\x00\x00\x07$': {
        'unused_8': 1644167168, 'unused_16': 516274, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1828},
    b'b\x00\x00\x00\x1c\xf8\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xc4': {
        'unused_8': 1644167168, 'unused_16': 486014982, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1220},
    b'b\x00\x00\x00\x1dX\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 1644167168, 'unused_16': 492306438, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'b\x00\x00\x00\x1d\x07\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xfc': {
        'unused_8': 1644167168, 'unused_16': 486998022, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1020},
    b'b\x00\x00\x00\x1d\x10\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x04(': {
        'unused_8': 1644167168, 'unused_16': 487587846, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1064},
    b'b\x00\x00\x00\x1d\xc1\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x03t': {
        'unused_8': 1644167168, 'unused_16': 499187718, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 884},
    b'b\x00\x00\x00\x1d\xc7\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xfc': {
        'unused_8': 1644167168, 'unused_16': 499580934, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1020},
    b'b\x00\x00\x00\x1dd\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x98': {
        'unused_8': 1644167168, 'unused_16': 493092870, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1432},
    b'b\x00\x00\x00\x1dj\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 1644167168, 'unused_16': 493486086, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'b\x00\x00\x00\x81@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03x': {
        'unused_8': 1644167168, 'unused_16': 2168455176, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 888},
    b'b\x00\x00\x00\x833\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x034': {
        'unused_8': 1644167168, 'unused_16': 2201157638, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 820},
    b'b\x00\x00\x00\x83:\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xc4': {
        'unused_8': 1644167168, 'unused_16': 2201616390, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 964},
    b'b\x00\x00\x00\x83<\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 1644167168, 'unused_16': 2201747462, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'ct o\x97\xf0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xfc': {
        'unused_8': 1668554863, 'unused_16': 2549088265, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1276},
    b'dp\xa3\x00\x10`UP\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x94': {
        'unused_8': 1685103360, 'unused_16': 274748752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 660},
    b'dp\xa7\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xd4': {
        'unused_8': 1685104384, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 468},
    b'dp\xa7\x00\x10t\xf9\x08\x00\x00\x00 \x00\x00\x004\x00\x00\r\xb4': {
        'unused_8': 1685104384, 'unused_16': 276101384, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3508},
    b'dp\xab\x00\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x9c': {
        'unused_8': 1685105408, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 924},
    b'dp\xae\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03`': {
        'unused_8': 1685106176, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 864},
    b'dp\xd5\x00\x10^FP\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x94': {
        'unused_8': 1685116160, 'unused_16': 274613840, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 660},
    b'dp\xda\x00\x10G\xf4\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x02l': {
        'unused_8': 1685117440, 'unused_16': 273151184, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 620},
    b'e\x12Fl\x90\x10\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x018': {
        'unused_8': 1695696492, 'unused_16': 2416967688, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 312},
    b'en B\xb7\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x94': {
        'unused_8': 1701716034, 'unused_16': 3081764873, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 916},
    b'gger\xb8P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03t': {
        'unused_8': 1734829426, 'unused_16': 3092250633, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 884},
    b'hl\xd3\x01``\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x04\xd4': {
        'unused_8': 1751962369, 'unused_16': 1616904200, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1236},
    b'hpR\x02\x10\x7f\xe0\xb0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xf4': {
        'unused_8': 1752191490, 'unused_16': 276816048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1012},
    b'hp\x03\x01\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe0': {
        'unused_8': 1752171265, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 992},
    b'hp\x9b\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x02X': {
        'unused_8': 1752210176, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 600},
    b'hp\x9f\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x03$': {
        'unused_8': 1752211201, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 804},
    b'hp\xa3\x00\x10_\xd2\x00\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x80': {
        'unused_8': 1752212224, 'unused_16': 274715136, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 640},
    b'hp\xa3\x00\x10`UP\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 1752212224, 'unused_16': 274748752, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'hp\xa3\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xe0': {
        'unused_8': 1752212224, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 992},
    b'hp\xa4\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x90': {
        'unused_8': 1752212480, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 912},
    b'hp\xa4\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x88': {
        'unused_8': 1752212480, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 904},
    b'hp\xa6\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x03T': {
        'unused_8': 1752212992, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 852},
    b'hp\xa8\x00\x10t\xf9\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\xf4': {
        'unused_8': 1752213504, 'unused_16': 276101384, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 500},
    b'hp\xab\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x060': {
        'unused_8': 1752214272, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1584},
    b'hp\xac\x00\x10\x7f\xe0\xb0\x00\x00\x00 \x00\x00\x004\x00\x00\x03,': {
        'unused_8': 1752214528, 'unused_16': 276816048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 812},
    b'hp\xad\x00\x10}\xdb\xd0\x00\x00\x00 \x00\x00\x004\x00\x00\x04\x1c': {
        'unused_8': 1752214784, 'unused_16': 276683728, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1052},
    b'hp\xae\x00\x10e\xc3\xe0\x00\x00\x00 \x00\x00\x004\x00\x00\x03h': {
        'unused_8': 1752215040, 'unused_16': 275104736, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 872},
    b'hp\xae\x00\x10e\xd3\xf0\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x0c': {
        'unused_8': 1752215040, 'unused_16': 275108848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 780},
    b'hp\xae\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x02\\': {
        'unused_8': 1752215041, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 604},
    b'hp\xb0\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x84': {
        'unused_8': 1752215553, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 644},
    b'hp\xb4\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x04P': {
        'unused_8': 1752216577, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1104},
    b'hp\xb6\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x02\\': {
        'unused_8': 1752217089, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 604},
    b'hp\xba\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x04': {
        'unused_8': 1752218113, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 772},
    b'hp\xbc\x00\x10`\x95`\x00\x00\x00 \x00\x00\x004\x00\x00\x03L': {
        'unused_8': 1752218624, 'unused_16': 274765152, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 844},
    b'hp\xbc\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x05,': {
        'unused_8': 1752218625, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1324},
    b'hp\xc5\x01\x10u\x08H\x00\x00\x00 \x00\x00\x004\x00\x00\x038': {
        'unused_8': 1752220929, 'unused_16': 276105288, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 824},
    b'hp\xd5\x00\x10`\x9a@\x00\x00\x00 \x00\x00\x004\x00\x00\x02\xd0': {
        'unused_8': 1752225024, 'unused_16': 274766400, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 720},
    b'hp\xdb\x00\x10Z\x04\x80\x00\x00\x00 \x00\x00\x004\x00\x00\x020': {
        'unused_8': 1752226560, 'unused_16': 274334848, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 560},
    b'hp{\x02\x10\x7f\xe0\xb0\x00\x00\x00 \x00\x00\x004\x00\x00\x02\x80': {
        'unused_8': 1752201986, 'unused_16': 276816048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 640},
    b'ion \xea`\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x078': {
        'unused_8': 1768910368, 'unused_16': 3932160009, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1848},
    b'iona\xe0P\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x14': {
        'unused_8': 1768910433, 'unused_16': 3763339273, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 788},
    b'ject\xce\xb0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07`': {
        'unused_8': 1785029492, 'unused_16': 3467640841, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1888},
    b'k\x11Mo\xba\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x05\x94': {
        'unused_8': 1796296047, 'unused_16': 3135242248, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1428},
    b'l\x05\x89\x00L\x80\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x80': {
        'unused_8': 1812302080, 'unused_16': 1283457032, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1920},
    b'nitiH\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\x0c': {
        'unused_8': 1852404841, 'unused_16': 1221591048, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2316},
    b'oftFy@\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\x94': {
        'unused_8': 1868985414, 'unused_16': 2034237448, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1940},
    b'ope.]\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x01\x98': {
        'unused_8': 1869636910, 'unused_16': 1560281096, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 408},
    b'ore \x1c0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\xe0': {
        'unused_8': 1869767968, 'unused_16': 472907784, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2272},
    b'ore\x05Z\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06t': {
        'unused_8': 1869767941, 'unused_16': 1525678088, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1652},
    b'ore\x05\xca\xd0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xa0': {
        'unused_8': 1869767941, 'unused_16': 3402629128, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1952},
    b'p: @,0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x18': {
        'unused_8': 1882857536, 'unused_16': 741343240, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2072},
    b'pCor/\xa0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04|': {
        'unused_8': 1883467634, 'unused_16': 799014921, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1148},
    b'ray\x0e\xd9\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0f\x98': {
        'unused_8': 1918990606, 'unused_16': 3640655880, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3992},
    b'rm G\x18\xa0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x07<': {
        'unused_8': 1919754311, 'unused_16': 413138952, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1852},
    b's\tLabp\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x02,': {
        'unused_8': 1929989217, 'unused_16': 1651507208, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 556},
    b's\x07de\x92@\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x07\xd4': {
        'unused_8': 1929864293, 'unused_16': 2453667849, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2004},
    b's\x07de\xe38\x00\x06\x00\x00\x00 \x00\x00\x004\x00\x00\x00\xd8': {
        'unused_8': 1929864293, 'unused_16': 3812098054, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 216},
    b's\x13Te\xbc\xf0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x03\xb8': {
        'unused_8': 1930646629, 'unused_16': 3169845256, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 952},
    b'scri\xee\x00\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x0c<': {
        'unused_8': 1935897193, 'unused_16': 3992977416, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 3132},
    b'str.\xb4\x00\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x04x': {
        'unused_8': 1937011246, 'unused_16': 3019898889, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1144},
    b'stru>\x10\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03 ': {
        'unused_8': 1937011317, 'unused_16': 1041235977, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 800},
    b'stru\x8d\xe0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x06\x98': {
        'unused_8': 1937011317, 'unused_16': 2380267528, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1688},
    b't th\xfb\xc0\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x060': {
        'unused_8': 1948284008, 'unused_16': 4223664136, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 1584},
    b'ttin\x1c \x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\x08\x90': {
        'unused_8': 1953786222, 'unused_16': 471859208, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2192},
    b'ttin\x1c`\x00\x08\x00\x00\x00 \x00\x00\x004\x00\x00\t\xf8': {
        'unused_8': 1953786222, 'unused_16': 476053512, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 2552},
    b'xd\xd7\x00l0\x00\t\x00\x00\x00 \x00\x00\x004\x00\x00\x03\x88': {
        'unused_8': 2019874560, 'unused_16': 1815085065, 'file_header_size': 32, 'metadata_header_size': 52, 'names_offset': 904},
}


def test_MetadataHeader():

    for test_index, header_bytes in enumerate(TEST_SETS):
        header = MetadataHeader().from_bytes(header_bytes)
        assert header.unused_8 == TEST_SETS[header_bytes]['unused_8']
        assert header.unused_16 == TEST_SETS[header_bytes]['unused_16']
        assert header.file_header_size == TEST_SETS[header_bytes]['file_header_size']
        assert header.metadata_header_size == TEST_SETS[header_bytes]['metadata_header_size']
        assert header.names_offset == TEST_SETS[header_bytes]['names_offset']
        header.validate(Header(), header.names_offset)
        expected_repr = f"MetadataHeader({{unused_8 = {header.unused_8}, unused_16 = {header.unused_16}, file_header_size = {header.file_header_size}, metadata_header_size = {header.metadata_header_size}, names_offset = {header.names_offset}}})"
        assert repr(header) == expected_repr


if __name__ == "__main__":
    test_MetadataHeader()
