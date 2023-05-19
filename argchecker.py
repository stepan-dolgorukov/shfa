import os.path

from accessify import private
from enum import StrEnum, Enum
from argparse import Namespace


class CheckMessage(StrEnum):
    """Человекопонятные сообщения проверки."""

    CORRECT = "Хорошо",
    NO_FILE_NAME = "Не указано имя файла",
    FILE_DOESNT_EXIST = "Файл не существует",
    NO_ACTION = "Не указано действие",
    INCORRECT_ACTION = "Указано некорректное действие",
    NO_OUTPUT_FILE_NAME = "Не указано имя файла вывода",
    OUTPUT_FILE_EXIST = "Выходной файл уже существует"


class Conclusion(Enum):
    """Заключения проверки.
    Проверка либо пройдена, либо нет.
    """

    NEGATIVE = False
    POSITIVE = True


class Action(Enum):
    """Действия над файлом.
    Файл можно либо закодировать, либо раскодировать.
    """

    ENCODE = 0,
    DECODE = 1


class ArgChecker:
    """Проверяет переданные аргументы на выполнение условий,
    необходимых для дальнейшей работы программы shfa.
    """

    def __init__(self, args):
        """args -- аргументы, отправленные на проверку."""

        if not isinstance(args, Namespace):
            raise ValueError("Поддерживается только argparse.Namespace")

        self.args = args
        self.message = None
        self.conclusion = None

    def get_conclusion(self) -> Conclusion:
        """Получить заключение по корректности аргументов.
        Аргументы либо верны, либо не верны.
        """

        if self.message is None:
            self.message = self.check_arg_action()

            if CheckMessage.CORRECT == self.message:
                self.message = self.check_arg_filename()

            if CheckMessage.CORRECT == self.message:
                self.message = self.check_arg_output()

        if CheckMessage.CORRECT == self.message:
            return Conclusion.POSITIVE

        return Conclusion.NEGATIVE

    def get_message(self) -> CheckMessage:
        """Получить сообщение проверки."""

        if self.conclusion is None:
            self.conclusion = self.get_conclusion()

        return self.message

    @private
    def file_exists(self, filename: str) -> bool:
        """Узнать, существует ли файл."""

        return os.path.exists(filename)

    @private
    def check_arg_filename(self) -> CheckMessage:
        """Проверить аргумент «имя файла»."""

        if self.args.filename is None:
            return CheckMessage.NO_FILE_NAME

        if not self.file_exists(self.args.filename):
            return CheckMessage.FILE_DOESNT_EXIST

        return CheckMessage.CORRECT

    @private
    def check_arg_action(self) -> CheckMessage:
        """Проверить аргумент «действие над файлом».
        Файл можно либо закодировать, либо раскодировать.
        """

        if self.args.action is None:
            return CheckMessage.NO_ACTION

        if not isinstance(self.args.action, Action):
            return CheckMessage.INCORRECT_ACTION

        return CheckMessage.CORRECT

    @private
    def check_arg_output(self) -> CheckMessage:
        """Проверить аргумент «имя файла выхода»"""

        if self.args.output is None:
            return CheckMessage.NO_OUTPUT_FILE_NAME

        if self.file_exists(self.args.output):
            return CheckMessage.OUTPUT_FILE_EXIST

        return CheckMessage.CORRECT
