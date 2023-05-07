import argparse
from argchecker import Action

class ArgParser:
    """Разбирающий аргументы."""

    def __init__(self):
        self.args = None

        self.parser = argparse.ArgumentParser(prog="Архиватор «Shannon-Fano»")
        self.parser.add_argument("--filename", "-f", nargs='?')
        self.parser.add_argument("--action", "-a", nargs='?')

    def parse(self):
        """Разобрать аргументы."""

        if self.args is None:
            self.args = self.parser.parse_args()

        if self.args.action in {'e', 'encode'}:
            self.args.action = Action.ENCODE

        if self.args.action in {'d', 'decode'}:
            self.args.action = Action.DECODE

        return self.args

    def brief(self):
        """Получить инструкцию как пользоваться программой"""
        return self.parser.format_help()

    def action(self) -> Action:
        return self.args.action