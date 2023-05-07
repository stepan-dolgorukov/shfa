import os.path

from accessify import private

class ArgChecker():
    """Проверяет переданные аргументы на выполнение условий,
    необходимых для дальнейшей работы программы shfa.
    """

    def __init__(self, args):
        """args -- аргументы, отправленные на проверку."""

        self.args = args
        self.message = None

    def check(self):
        """Проверить аргументы, вернуть сообщение проверки."""

        if None is self.message:
            self.check_arg_action()

            if "Хорошо" == self.message:
                self.check_arg_filename()

        return self.message

    def conclusion(self):
        """Получить заключение по корректности аргументов.
        Аргументы либо верны, либо не верны.
        """

        if None is self.message:
            self.check()

        return "Хорошо" == self.message

    def check_message(self):
        """Получить сообщение проверки."""

        if None is self.message:
            self.check()

        return self.message

    @private
    def check_arg_filename(self):
        """Проверить аргумент «имя файла»."""

        if self.args.filename is None:
            self.message = "Не указано имя файла"
            return

        if not os.path.exists(self.args.filename):
            self.message = "Файл не существует"
            return

        self.message = "Хорошо"
        return

    @private
    def check_arg_action(self):
        """Проверить аргумент «действие над файлом».
        Файл можно либо закодировать, либо раскодировать.
        """

        if self.args.action is None:
            self.message = "Не указано действие"
            return

        if self.args.action not in {'e', 'd'}:
            self.message = "Указано некорректное действие"
            return

        self.message = "Хорошо"
        return
