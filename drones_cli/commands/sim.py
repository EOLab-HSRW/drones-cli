from argparse import ArgumentParser, Namespace
from drones_cli.commands import Command

class SimCommand(Command):

    def add_arguments(self, parser: ArgumentParser):
        return super().add_arguments(parser)

    def execute(self, args: Namespace):

        return super().execute(args)
