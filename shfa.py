#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader

from argparser import ArgParser
from argchecker import ArgChecker

def encode(filename):
    data = ""
    with open(filename) as file:
        data = "".join(file.readlines())

    writer = CompressionWriter(data, filename + '.compressed')
    writer.write()

def decode(filename):
    reader = DecompressionReader(filename)
    data = reader.read()

    print(data)
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
        decode(args.filename)
