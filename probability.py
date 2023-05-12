from collections import Counter

def byte_probability(data: bytes):
    if not isinstance(data, bytes):
        raise ValueError("Допустимы только байтовые строки")

    if not data:
        raise ValueError("Пустая строка байтов")

    byte_count  = Counter(data)
    return {byte: byte_count[byte] / len(data) for byte in byte_count}