#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader

from argparser import ArgParser
from argchecker import ArgChecker, Conclusion, Action

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
    parser = ArgParser()
    args = parser.parse()
    checker = ArgChecker(args)

    if Conclusion.POSITIVE != checker.get_conclusion():
        print(checker.get_message())
        print(parser.brief())
        exit(1)

    if parser.args.action == Action.ENCODE:
        encode(args.filename)

    if parser.args.action == Action.DECODE:
        try:
            data = decode(args.filename)
            print(data)
        except Exception:
            print("Не удалось раскодировать строку")
