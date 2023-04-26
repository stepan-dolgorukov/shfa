import os.path

class ArgChecker():
    def __init__(self, args):
        self.args = args

    def check(self):
        if self.args.filename is None:
            return "Не указано имя файла"

        if not os.path.exists(self.args.filename):
            return "Файл не существует"

        if self.args.action is None:
            return "Не указано действие"

        if self.args.action not in {'e', 'd'}:
            return "Указано некорректное действие"

        return "Хорошо"
