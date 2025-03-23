import sys
import argparse
from drones_cli.commands import Command, BuildCommand, SimCommand


OPTIONS: dict[str, type[Command]] = {
    "build": BuildCommand,
    "sim": SimCommand
}

def main() -> int:

    parser = argparse.ArgumentParser(
        prog="eolab-px4",
        description="A simple tool to work with eolab drones"
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
