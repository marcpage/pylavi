#!/usr/bin/env python3


import os

from pylavi.file import Resources


def test_empty_vi():
    vi_path = os.path.join(os.path.split(__file__)[0], 'empty.vi')
    resources = Resources.load(vi_path)
    assert set(resources.types()) == set(EMPTY_VI_TYPES), [set(resources.types()), set(EMPTY_VI_TYPES)]
    assert resources.count_type('vers') == 5, resources.count_type('vers')
    assert resources.count_type('LVSR') == 1, resources.count_type('LVSR')
    assert set(resources.get_ids('vers')) == VERS_IDS
    assert resources.get_names('LVSR') == [b'empty.vi'], resources.get_names('LVSR')
    assert set(resources.get_resources('vers')) == VERS_RESOURCES
    assert resources.get_resource('vers', 8) == b'!\x00\x80\x00\x00\x00\x0421.0\x00'
    assert resources.get_resource('LVSR', name='empty.vi') == LVSR_DATA

VERS_IDS = {4, 7, 8, 9, 10}

VERS_RESOURCES = {
    (4, None, b'!\x00\x80\x00\x00\x00\x0421.0\x00'),
    (7, None, b'!\x00\x80\x00\x00\x00\x0421.0\x00'),
    (8, None, b'!\x00\x80\x00\x00\x00\x0421.0\x00'),
    (9, None, b'!\x00\x80\x00\x00\x00\x0421.0\x00'),
    (10, None, b'!\x00\x80\x00\x00\x00\x0421.0\x00')}

EMPTY_VI_TYPES = {
    'LVSR', 'RTSG', 'CCST', 'LIvi', 'CONP', 'TM80', 'DFDS', 'LIds', 'VICD', 'GCDI',
    'vers', 'SCSR', 'DLDR', 'FPTD', 'CPMp', 'NUID', 'SUID', 'BNID', 'GCPR', 'BDPW',
    'ICON', 'icl8', 'CPC2', 'LIfp', 'FPEx', 'FPHb', 'FPSE', 'VPDP', 'LIbd', 'BDEx',
    'BDHb', 'BDSE', 'DTHP', 'MUID', 'HIST', 'VCTP', 'FTAB'}

LVSR_DATA = b'!\x00\x80\x00\x00\x00\x00\x00 \x00\x02\x00\x00\x00\x00\x04\x00\x03\x00<\x00\x00\x00\x1f@\x80\x02\x00\x00\x00\x00\x01\x00\x01\x00\x02\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xff\xff\xff\xff\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~'

if __name__ == "__main__":
    test_empty_vi()
