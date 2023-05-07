import argparse
from argchecker import Action

class ArgParser:
    """Разбирающий аргументы."""

    def __init__(self):
        self.args = None

        self.action_key_values = {
            Action.ENCODE: ['e', 'encode', 'enc', 'en'],
            Action.DECODE: ['d', 'decode', 'dec', 'de']
        }

        self.parser = argparse.ArgumentParser(prog="Архиватор «Shannon-Fano»")
        self.parser.add_argument("--filename", "-f", nargs=1)

        self.parser.add_argument("--action", "-a", nargs=1,
            choices=self.action_key_values[Action.ENCODE] +
                    self.action_key_values[Action.DECODE])

    def parse(self):
        """Разобрать аргументы."""

        if self.args is None:
            self.args = self.parser.parse_args()

        if self.args.action in self.action_key_values[Action.ENCODE]:
            self.args.action = Action.ENCODE

        if self.args.action in self.action_key_values[Action.DECODE]:
            self.args.action = Action.DECODE

        return self.args

    def brief(self):
        """Получить инструкцию как пользоваться программой"""
        return self.parser.format_help()

    def action(self) -> Action:
        return self.args.action