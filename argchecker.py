import os.path

from accessify import private

class ArgChecker():
    def __init__(self, args):
        self.args = args
        self.message = None

    def check(self):
        if None is self.message:
            self.check_arg_action()

            if "Хорошо" == self.message:
                self.check_arg_filename()

        return self.message

    def conclusion(self):
        if None is self.message:
            self.check()

        return "Хорошо" == self.message

    def check_message(self):
        if None is self.message:
            self.check()

        return self.message

    @private
    def check_arg_filename(self):
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
        if self.args.action is None:
            self.message = "Не указано действие"
            return

        if self.args.action not in {'e', 'd'}:
            self.message = "Указано некорректное действие"
            return

        self.message = "Хорошо"
        return
