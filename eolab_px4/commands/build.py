from argparse import ArgumentParser, Namespace
from eolab_px4.commands import Command

class BuildCommand(Command):

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("--option", help="An option for the build command")

    def execute(self, args: Namespace) -> None:
        print("Running 'build' command")
        print(f"Options: {args.option}")
