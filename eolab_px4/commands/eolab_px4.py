import sys
import argparse
import subprocess
from eolab_px4 import CACHE_DIR, PX4_DIR
from eolab_px4.commands import Command, BuildCommand


OPTIONS: dict[str, type[Command]] = {
    "build": BuildCommand,
}

def git_clone_px4():

    if PX4_DIR.exists():
        print("PX4 already there skipping clone.")
        return

    try:
        # Cloning the repository using git
        print(f"Cloning the PX4-Autopilot into {PX4_DIR}...")
        subprocess.run(["git", "clone", "https://github.com/PX4/PX4-Autopilot.git", PX4_DIR, "--recursive"], check=True)
        print(f"Repository cloned successfully into {PX4_DIR}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while cloning PX4-Autopilot: {e}")


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
