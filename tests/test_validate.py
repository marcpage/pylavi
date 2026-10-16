#!/usr/bin/env python3

import os
import struct
import types

from pylavi.validate import parse_args, main, start_finding_files, find_problems
from pylavi.validate import parse_config_file, patch_up_args, reentrancy_settings
from pylavi.validate import REENTRANCY_CHOICES, NON_REENTRANT, SHARED_REENTRANT
from pylavi.validate import PREALLOCATE_REENTRANT, INLINE_REENTRANT, excluded_from_reentrancy
from pylavi.file import Resources
from pylavi.resource_types import TypeLVSR


def test_arguments():
    args = parse_args([])
    assert args.lt is None
    assert args.gt is None
    assert args.eq is None
    assert not args.no_release
    assert args.no_beta
    assert args.no_alpha
    assert args.no_development
    assert args.no_invalid
    assert args.path == ['.']
    assert args.skip == []
    assert args.extension == Resources.EXTENSIONS


def test_find_files():
    args = parse_config_file(parse_args(('-p', 'tests', '-p', 'pylavi', '-p', __file__)))
    files = start_finding_files(args)
    file_list = set()

    while True:
        next_path = files.get()

        if next_path is None:
            break

        file_list.add(next_path[1])

    assert EXPECTED_FILES - file_list == set(), EXPECTED_FILES - file_list


def test_run():
    assert main(parse_args(['-v', '-v', '--path', os.path.join('tests', 'empty.vi')])) ==0
    assert main(parse_args(['-q', '--password', '--path', os.path.join('tests', 'empty.vi')])) == 1
    assert main(parse_args(['-q', '--no-password', '--path', os.path.split(os.path.split(__file__)[0])[0]])) == 1
    assert main(parse_args(['--path-length', '14', '--path',  os.path.join('tests', 'empty.vi')])) == 0
    assert main(parse_args(['-q', '--path-length', '13', '--path',  os.path.join('tests', 'empty.vi')])) == 1
    assert main(parse_args(['--config', os.path.join('tests', 'args.yaml')])) == 1
    assert main(parse_args(['--config', os.path.join('tests', 'test.yaml')])) == 0
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    assert main(parse_args(['-v', '-v', '-v', '--no-password', '--skip', os.path.join(root_dir, 'tests', '*'), '--path', os.path.split(os.path.split(__file__)[0])[0]])) == 0
    test_vi_set = [
        '-p', os.path.join('tests', 'empty.vi'),
        '-p', os.path.join('tests', 'empty_beta.vi'),
        '-p', os.path.join('tests', 'empty_alpha.vi'),
        '-p', os.path.join('tests', 'empty_dev.vi'),
        '-p', os.path.join('tests', 'empty_invalid.vi'),
    ]
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-x', '.py', '-p', __file__]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-x', '.no way this exists', '-p', __file__]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-g', '99', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-l', '2', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-e', '6', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-e', '21', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-r', *test_vi_set]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-b', *test_vi_set]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-d', *test_vi_set]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-a', *test_vi_set]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-i', *test_vi_set]))), parse_args(['-q']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--code', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--code', '-p', os.path.join('tests', 'empty_separate_code.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-code', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-code', '-p', os.path.join('tests', 'empty_separate_code.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--breakpoints', '-p', os.path.join('tests', 'add.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--breakpoints', '-p', os.path.join('tests', 'add_breakpoints.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--autoerr', '-p', os.path.join('tests', 'empty_no_auto_err.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--autoerr', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-password', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--not-locked', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--password', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--locked', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-password', '-p', os.path.join('tests', 'empty_locked.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--not-locked', '-p', os.path.join('tests', 'empty_locked.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--password', '-p', os.path.join('tests', 'empty_locked.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--locked', '-p', os.path.join('tests', 'empty_locked.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-password', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--not-locked', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--password', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--locked', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--password-match', 'password', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--password-match', 'Setec Astronomy', '-p', os.path.join('tests', 'empty_password.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--password-match', 'password', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--password-match', '', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--debuggable', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--not-debuggable', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--debuggable', '-p', os.path.join('tests', 'empty_no_debugging.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--not-debuggable', '-p', os.path.join('tests', 'empty_no_debugging.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--run-on-open', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-run-on-open', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--run-on-open', '-p', os.path.join('tests', 'empty_run_on_open.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-run-on-open', '-p', os.path.join('tests', 'empty_run_on_open.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--suspend-on-run', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-suspend-on-run', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--suspend-on-run', '-p', os.path.join('tests', 'empty_suspend_when_called.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-suspend-on-run', '-p', os.path.join('tests', 'empty_suspend_when_called.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--clear-indicators', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--no-clear-indicators', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['--clear-indicators', '-p', os.path.join('tests', 'empty_clear_indicators.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-clear-indicators', '-p', os.path.join('tests', 'empty_clear_indicators.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-v', '-v', '--no-absolute-path', '-p', os.path.join('tests', 'relative_link.vi')]))), parse_args(['-v']))
    assert len(problems) == 0, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--no-absolute-path', '-p', os.path.join('tests', 'absolute_link_PTH.vi')]))), parse_args(['-v']))
    assert len(problems) == 1, problems
    problems = find_problems(start_finding_files(parse_config_file(parse_args(['-q', '--locked', '--no-code', '-p', os.path.join('tests', 'empty.vi')]))), parse_args(['-v']))
    assert len(problems) == 2, problems
    print(problems)


EXPECTED_FILES = {
    'pylavi/__init__.py',
    'pylavi/assembler.py',
    'pylavi/data_types.py',
    'pylavi/file.py',
    'pylavi/resource_types.py',
    'pylavi/validate.py',
    'tests/empty.vi',
    'tests/test_assembler.py',
    'tests/test_data_type_PString.py',
    'tests/test_data_type_Version.py',
    'tests/test_data_type_FourCharCode.py',
    'tests/test_file_Header.py',
    'tests/test_file_MetadataHeader.py',
    'tests/test_file_ResourceMetadata.py',
    'tests/test_file_Resources.py',
    'tests/test_file_TypeInfo.py',
    'tests/test_resource_type_vers.py',
    'tests/test_validate.py',
}


def reentrancy_problems(path, *options):
    args = parse_args(['-q', '-p', path, *options])
    return find_problems(start_finding_files(parse_config_file(args)), parse_args(['-q']))


def lvsr_with_flags(word0, word1):
    return TypeLVSR().from_bytes(b'\x14\x00\x80\x00' + struct.pack('>II', word0, word1) + bytes(24))


def test_reentrancy_settings():
    for word0, word1, expected in REENTRANCY_SETTINGS_CASES:
        settings = reentrancy_settings(lvsr_with_flags(word0, word1))
        assert settings == expected, (hex(word0), hex(word1), settings)

    assert reentrancy_settings(TypeLVSR().from_bytes(b'\x14\x00\x80\x00\x00\x00')) is None


def test_reentrancy():
    for version in ('23.0', '26.0'):
        for name, settings in REENTRANCY_VI_CASES.items():
            path = os.path.join('tests', 'reentrancy', version, name)
            lvsr = TypeLVSR().from_bytes(Resources.load(path).get_resources('LVSR')[0][2])
            assert reentrancy_settings(lvsr) == settings, path

            for choice in REENTRANCY_CHOICES:
                problems = reentrancy_problems(path, '--reentrancy', choice)
                assert len(problems) == (0 if choice in settings else 1), (path, choice)

            allowed = [item for choice in settings for item in ('--reentrancy', choice)]
            assert not reentrancy_problems(path, *allowed), path

    inline = os.path.join('tests', 'reentrancy', '23.0', 'Inline.vi')
    assert not reentrancy_problems(inline, '--reentrancy', SHARED_REENTRANT, '--reentrancy', INLINE_REENTRANT)
    assert reentrancy_problems(inline, '--reentrancy', NON_REENTRANT, '--reentrancy', PREALLOCATE_REENTRANT)
    problems = reentrancy_problems(os.path.join('tests', 'reentrancy', '23.0', 'Inline - preallocate.vi'), '--reentrancy', SHARED_REENTRANT)
    assert 'Reentrancy is inline, preallocate' in str(problems[0])
    assert not reentrancy_problems(inline, '--breakpoints')


def vi_resources(file_type='LVIN', **counts):
    counts = {'BDPW': 1, 'CPST': 0, **counts}
    return types.SimpleNamespace(
        file_type=types.SimpleNamespace(to_string=lambda: file_type),
        count_type=lambda resource_type: counts.get(resource_type, 0),
    )


def test_excluded_from_reentrancy():
    for version in ('23.0', '26.0'):
        for name in REENTRANCY_VI_CASES:
            assert not excluded_from_reentrancy(Resources.load(os.path.join('tests', 'reentrancy', version, name)))

    assert not excluded_from_reentrancy(vi_resources())
    assert excluded_from_reentrancy(vi_resources(file_type='LVCC'))  # control
    assert excluded_from_reentrancy(vi_resources(BDPW=0))  # no block diagram (global)
    assert excluded_from_reentrancy(vi_resources(CPST=1))  # polymorphic


def test_reentrancy_arguments():
    args = patch_up_args(parse_args(['--reentrancy', 'shared']))
    assert args.reentrancy == ['shared']
    assert not args.no_beta
    assert not args.path_length
    assert parse_args(['-q']).reentrancy == []

    args = parse_args(['-q'])
    args.reentrancy = 'inline'
    assert patch_up_args(args).reentrancy == ['inline']

    args = parse_args(['-q'])
    args.reentrancy = ['bogus']
    try:
        patch_up_args(args)
        assert False, 'invalid reentrancy accepted'
    except AssertionError as error:
        assert 'Invalid reentrancy' in str(error)

    try:
        parse_args(['--reentrancy', 'bogus'])
        assert False, 'invalid reentrancy accepted'
    except SystemExit:
        pass


# (flag word 0, flag word 1, expected settings)
REENTRANCY_SETTINGS_CASES = [
    (0x00000000, 0x20000600, {NON_REENTRANT}),
    (0x01000000, 0x20000600, {PREALLOCATE_REENTRANT}),
    (0x01000080, 0x20000600, {SHARED_REENTRANT}),
    (0x01000080, 0x00020600, {INLINE_REENTRANT, SHARED_REENTRANT}),
    (0x01000000, 0x00020600, {INLINE_REENTRANT, PREALLOCATE_REENTRANT}),
    (0x04000020, 0x20000600, {PREALLOCATE_REENTRANT}),
    (0x000000A0, 0x00000600, {SHARED_REENTRANT}),
    (0x040000A0, 0x20000400, {SHARED_REENTRANT}),
    (0x40000180, 0x00000400, {NON_REENTRANT}),
    (0x00000080, 0x00000400, {NON_REENTRANT}),
    (0x00100000, 0x20000400, {NON_REENTRANT}),
]

REENTRANCY_VI_CASES = {
    'Non-Reentrant.vi': {NON_REENTRANT},
    'Preallocate-Reentrant.vi': {PREALLOCATE_REENTRANT},
    'Shared-Reentrant.vi': {SHARED_REENTRANT},
    'Inline.vi': {INLINE_REENTRANT, SHARED_REENTRANT},
    'Inline - preallocate.vi': {INLINE_REENTRANT, PREALLOCATE_REENTRANT},
}


if __name__ == "__main__":
    test_arguments()
    test_find_files()
    test_run()
    test_reentrancy_settings()
    test_reentrancy()
    test_excluded_from_reentrancy()
    test_reentrancy_arguments()
