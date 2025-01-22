import sys
import argparse
import subprocess
from eolab_px4 import CACHE_DIR, PX4_DIR
from eolab_px4.commands import Command, BuildCommand


OPTIONS: dict[str, type[Command]] = {
    "build": BuildCommand,
}

def main() -> int:

    parser = argparse.ArgumentParser(
        prog="eolab_px4",
        description="A simple tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    for command_name, command_cls in OPTIONS.items():
        subparser = subparsers.add_parser(command_name, help=f"{command_name} command")
        command_cls().add_arguments(subparser)

    args = parser.parse_args()

    command_cls = OPTIONS.get(args.command)
    if command_cls:
        command_cls().execute(args)
    else:
        parser.error(f"Unknown command: {args.command}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
