from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace

class Command(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def add_arguments(self, parser: ArgumentParser):
        pass

    @abstractmethod
    def execute(self, args: Namespace):
        pass
