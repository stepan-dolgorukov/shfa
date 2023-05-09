from collections import Counter

def byte_probability(data: bytes):
    probability = {}
    byte_count = Counter(data)
    return {byte: byte_count[byte] / len(data) for byte in byte_count}