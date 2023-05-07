import os.path

from accessify import private
from enum import StrEnum, Enum

class CheckMessage(StrEnum):
    CORRECT = "Хорошо",
    NO_FILE_NAME = "Не указано имя файла",
    FILE_DOESNT_EXIST = "Файл не существует",
    NO_ACTION = "Не указано действие",
    INCORRECT_ACTION = "Указано некорректное действие"

class Conclusion(Enum):
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
        self.conclusion = None

    def get_conclusion(self):
        """Получить заключение по корректности аргументов.
        Аргументы либо верны, либо не верны.
        """

        if self.message is None:
            self.message = self.check_arg_action()

            if CheckMessage.CORRECT == self.message:
                self.message = self.check_arg_filename()

        if CheckMessage.CORRECT == self.message:
            return Conclusion.POSITIVE
        
        return Conclusion.NEGATIVE

    def get_message(self):
        """Получить сообщение проверки."""

        if self.conclusion is None:
            self.conclusion = self.get_conclusion()

        return self.message

    @private
    def check_arg_filename(self):
        """Проверить аргумент «имя файла»."""

        if self.args.filename is None:
            return CheckMessage.NO_FILE_NAME

        if not os.path.exists(self.args.filename):
            return CheckMessage.FILE_DOESNT_EXIST

        return CheckMessage.CORRECT

    @private
    def check_arg_action(self):
        """Проверить аргумент «действие над файлом».
        Файл можно либо закодировать, либо раскодировать.
        """

        if self.args.action is None:
            return CheckMessage.NO_ACTION

        if self.args.action not in {'e', 'd'}:
            return CheckMessage.INCORRECT_ACTION

        return CheckMessage.CORRECT
