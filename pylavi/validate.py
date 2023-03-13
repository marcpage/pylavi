"""
    Checks LabVIEW resource file(s) for given criteria
"""


import argparse
import os
import queue
import sys
import threading

from pylavi.file import Resources
from pylavi.resource_types import Typevers
from pylavi.data_types import Version


def parse_args(command_line=None):
    """Interpret command line arguments"""
    command_line = command_line or sys.argv[1:]
    parser = argparse.ArgumentParser(description="Validates LabVIEW resource files")
    parser.add_argument(
        "-l", "--lt", type=str, help="LabVIEW version must be less than this"
    )
    parser.add_argument(
        "-g", "--gt", type=str, help="LabVIEW version must be greater than this"
    )
    parser.add_argument("-e", "--eq", type=str, help="LabVIEW version must this")
    parser.add_argument(
        "-r",
        "--no-release",
        action="store_true",
        help="LabVIEW version must not be release",
    )
    parser.add_argument(
        "-b", "--no-beta", action="store_true", help="LabVIEW version must not be beta"
    )
    parser.add_argument(
        "-a",
        "--no-alpha",
        action="store_true",
        help="LabVIEW version must not be alpha",
    )
    parser.add_argument(
        "-d",
        "--no-development",
        action="store_true",
        help="LabVIEW version must not be development",
    )
    parser.add_argument(
        "-i",
        "--no-invalid",
        action="store_true",
        help="LabVIEW version must be a valid phase",
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        action="append",
        help="Path to scan for files (or a file path) (defaults to current directory)",
    )
    parser.add_argument(
        "-s",
        "--skip",
        type=str,
        action="append",
        help="Path to not scan for files (or a file to ignore)",
    )
    parser.add_argument(
        "-x",
        "--extension",
        type=str,
        action="append",
        help="File extensions to evaluate (defaults to all known)",
    )
    args = parser.parse_args(args=command_line)
    args.path = args.path or [""]
    args.skip = args.skip or []
    has_comparison = args.lt or args.gt or args.eq
    has_phase = (
        args.no_release
        or args.no_beta
        or args.no_alpha
        or args.no_development
        or args.no_invalid
    )

    if not has_comparison and not has_phase:
        args.no_beta = True
        args.no_alpha = True
        args.no_development = True
        args.no_invalid = True

    if not args.extension:
        args.extension = Resources.EXTENSIONS

    return args


def find_files(found_queue, paths):
    """Find files in given paths and put them in the queue"""
    for path in paths:
        if os.path.isfile(path):
            found_queue.put(path)
        else:
            for root, _, files in os.walk(path):
                for file in files:
                    found_queue.put(os.path.join(root, file))

    found_queue.put(None)


def start_finding_files(*paths):
    """Start the find_files function running in the background finding files"""
    found = queue.Queue()
    thread = threading.Thread(target=find_files, args=(found, paths), daemon=True)
    thread.start()
    return found


def validate(args, resources, problems, next_path):
    """Validate that the given resources file is valid"""
    versions = [Typevers().from_bytes(r[2]) for r in resources.get_resources("vers")]
    problem_count = len(problems)

    for version in versions:
        version_string = version.version.to_string()
        phase = version.version.phase()

        if args.gt and version < args.gt:
            problems.append((f"<{args.gt}", version_string, next_path))
            break

        if args.lt and not version < args.lt:
            problems.append((f">{args.lt}", version_string, next_path))
            break

        if args.eq and not version == args.eq:
            problems.append((f"!={args.eq}", version_string, next_path))
            break

        if args.no_release and phase == Version.RELEASE:
            problems.append(("no-release", version_string, next_path))
            break

        if args.no_beta and phase == Version.BETA:
            problems.append(("no-beta", version_string, next_path))
            break

        if args.no_alpha and phase == Version.ALPHA:
            problems.append(("no-alpha", version_string, next_path))
            break

        if args.no_development and phase == Version.DEVELOPMENT:
            problems.append(("no-development", version_string, next_path))
            break

        if args.no_invalid and (phase > Version.RELEASE or phase == 0):
            problems.append(("no-invalid", version_string, next_path))
            break

    if len(problems) > problem_count:
        print(
            f"FAIL: {problems[-1][0]} saved in version {problems[-1][1]}: {problems[-1][2]}"
        )


def find_problems(args, files):
    """Searchs for problems files and returns them"""
    problems = []

    while True:
        next_path = files.get()

        if next_path is None:
            break

        if os.path.splitext(next_path)[1] not in args.extension:
            continue

        try:
            validate(args, Resources.load(next_path), problems, next_path)

        except AssertionError as error:
            problems.append((error, "", next_path))
            print(
                f"FAIL: {problems[-1][0]} saved in version {problems[-1][1]}: {problems[-1][2]}"
            )

    return problems


def main(args=None):
    """run the (dis)assembler"""
    args = args or parse_args()
    files = start_finding_files(*args.path)
    problems = find_problems(args, files)

    if len(problems) > 0:
        print(f"{len(problems)} problems encounted")
        sys.exit(1)


if __name__ == "__main__":
    main(parse_args())
