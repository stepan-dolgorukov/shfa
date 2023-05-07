import os.path

from accessify import private
from enum import StrEnum, Enum

class CheckMessage(StrEnum):
    CORRECT = "Хорошо",
    NO_FILE_NAME = "Не указано имя файла",
    FILE_DOESNT_EXIST = "Файл не существует",
    NO_ACTION = "Не указано действие",
    INCORRECT_ACTION = "Указано некорректное действие"

class Conclusions(Enum):
    NEGATIVE = False
    POSITIVE = True

class ArgChecker:
    """Проверяет переданные аргументы на выполнение условий,
    необходимых для дальнейшей работы программы shfa.
    """

    def __init__(self, args):
        """args -- аргументы, отправленные на проверку."""

        self.args = args
        self.message = None

    def check(self):
        """Проверить аргументы, вернуть сообщение проверки."""

        if self.message is None:
            self.check_arg_action()

            if CheckMessage.CORRECT == self.message:
                self.check_arg_filename()

        return self.message

    def conclusion(self):
        """Получить заключение по корректности аргументов.
        Аргументы либо верны, либо не верны.
        """

        if self.message is None:
            self.check()

        return CheckMessage.CORRECT == self.message

    def check_message(self):
        """Получить сообщение проверки."""

        if self.message is None:
            self.check()

        return self.message

    @private
    def check_arg_filename(self):
        """Проверить аргумент «имя файла»."""

        if self.args.filename is None:
            self.message = CheckMessage.NO_FILE_NAME
            return

        if not os.path.exists(self.args.filename):
            self.message = CheckMessage.FILE_DOESNT_EXIST
            return

        self.message = CheckMessage.CORRECT
        return

    @private
    def check_arg_action(self):
        """Проверить аргумент «действие над файлом».
        Файл можно либо закодировать, либо раскодировать.
        """

        if self.args.action is None:
            self.message = CheckMessage.NO_ACTION
            return

        if self.args.action not in {'e', 'd'}:
            self.message = CheckMessage.INCORRECT_ACTION
            return

        self.message = CheckMessage.CORRECT
        return
