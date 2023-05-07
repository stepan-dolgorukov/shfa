#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader

from argparser import ArgParser
from argchecker import ArgChecker, Conclusions

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

    if Conclusions.POSITIVE != checker.get_conclusion():
        print(checker.get_message())
        exit(1)

    if args.action == 'e':
        encode(args.filename)

    if args.action == 'd':
        try:
            data = decode(args.filename)
            print(data)
        except Exception:
            print("Не удалось раскодировать строку")
