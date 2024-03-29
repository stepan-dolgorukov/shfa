class NotNiceFileName(Exception):
    """Исключение «Не хорошее имя файла»."""


def file_name_is_nice(name: str) -> bool:
    if not isinstance(name, str):
        return False

    if not name:
        return False

    return True
