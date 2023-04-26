#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader
import argparse
import os.path

def parse_args():
    parser = argparse.ArgumentParser(prog="Архиватор «Shannon-Fano»")

    parser.add_argument("--filename", "-f", nargs='?')
    parser.add_argument("--action", "-a", nargs='?')

    args = parser.parse_args()
    return args

def check_args(args):
    if args.filename is None:
        return "Не указано имя файла"

    if not os.path.exists(args.filename):
        return "Файл не существует"

    if args.action is None:
        return "Не указано действие"

    if args.action not in {'e', 'd'}:
        return "Указано некорректное действие"

    return "Хорошо"

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
    args = parse_args()
    message = check_args(args)

    if "Хорошо" != message:
        print(message)
        exit()

    if args.action == 'e':
        encode(args.filename)

    if args.action == 'd':
        decode(args.filename)
