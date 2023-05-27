import hashlib

def hashcode(data: bytes) -> str:
    if not isinstance(data, bytes):
        raise TypeError("Информация должна быть типа «bytes»")

    hasher = hashlib.new("sha256", data)
    return hasher.hexdigest()