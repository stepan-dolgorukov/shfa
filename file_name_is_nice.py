def file_name_is_nice(name: str):
    if not isinstance(name, str):
        return False

    if not name:
        return False

    return True