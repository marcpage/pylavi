"""
    Parses a LabVIEW resource file
"""

import argparse
import json
import sys

import pylavi.file


def parse_args(command_line=None):
    """Interpret command line arguments"""
    command_line = command_line or sys.argv[1:]
    parser = argparse.ArgumentParser(description="Converts LabVIEW Resources to text")
    parser.add_argument(
        "-d",
        "--disassemble",
        dest="disassemble",
        action="store_true",
        help="Disassemble the resource file into text",
    )
    parser.add_argument("input_file")
    parser.add_argument(
        "-o", "--out", dest="output_file", type=str, help="Path to output the results"
    )
    args = parser.parse_args(args=command_line)
    return args


def main(args=None):
    """run the (dis)assembler"""
    args = args or parse_args()
    resources = pylavi.file.Resources.load(args.input_file)
    output = {
        "path": args.input_file,
        "type": resources.file_type.to_string(),
        "creator": resources.file_creator.to_string(),
        "resources": {},
    }

    for resource_type in resources.types():
        output["resources"][resource_type] = []

        for identifier, name, data in resources.get_resources(resource_type):
            output["resources"][resource_type].append(
                {
                    "id": identifier,
                    "name": name.decode("ascii") if name else name,
                    "data": data.hex(),
                }
            )

    if args.output_file:
        print(output)
        with open(args.output_file, "w", encoding="utf-8") as output_file:
            json.dump(output, output_file, indent=2, sort_keys=True)
    else:
        json.dump(output, sys.stdout, indent=2, sort_keys=True)


if __name__ == "__main__":
    main(parse_args())
