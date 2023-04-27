#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader

from argparser import ArgParser
from argchecker import ArgChecker

def encode(filename):
    data = ""
    with open(filename) as file:
        data = file.read()

    writer = CompressionWriter(data, filename + '.compressed')
    writer.write()

def decode(filename):
    data = None

    try:
        reader = DecompressionReader(filename)
        data = reader.read()
    except Exception:
        raise ValueError

    return data

if __name__ == '__main__':
    args = ArgParser().parse()
    checker = ArgChecker(args)

    if True != checker.conclusion():
        print(checker.check_message())
        exit()

    if args.action == 'e':
        encode(args.filename)

    if args.action == 'd':
        try:
            data = decode(args.filename)
        except Exception:
            print("Не удалось раскодировать строку")
