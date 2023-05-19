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

        self.parser = argparse.ArgumentParser(
            description="Архиватор «Shannon-Fano»")

        self.parser.add_argument("--filename", "-f", nargs='?',
                                 help="Имя файла ввода")

        self.parser.add_argument("--action", "-a", nargs='?',
                                 choices=self.action_key_values[Action.ENCODE] +
                                 self.action_key_values[Action.DECODE],
                                 help="Действие, которое требуется совершить над файлом "
                                 "ввода")

        self.parser.add_argument("--output", "-o", nargs='?',
                                 help="Имя файла вывода")

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
