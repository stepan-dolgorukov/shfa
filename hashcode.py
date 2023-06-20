import hashlib


def hashcode(data: bytes) -> str:
    """Вычисление хэш-кода указанной байтовой строки.

    data -- информация, хэш-код которой требуется вычислить.
    """

    if not isinstance(data, bytes):
        raise TypeError("Информация должна быть типа «bytes»")

    hasher = hashlib.new("sha256", data)
    return hasher.hexdigest()
