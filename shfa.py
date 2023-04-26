#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader
import argparse
import os.path

def parse_args():
    parser = argparse.ArgumentParser(prog="Архиватор «Shannon-Fano»")

    parser.add_argument("--filename", "-f")
    parser.add_argument("--action", "-a")

    args = parser.parse_args()
    return args

def check_args(args):
    if (args.filename is None) or (not os.path.exists(args.filename)):
        return False

    if (args.action is None) or (args.action not in {'e', 'd'}):
        return False

    return True

def encode(filename):
    data = ""
    with open(filename) as file:
        data = file.readline()

    writer = CompressionWriter(data, filename + '.compressed')
    writer.write()

def decode(filename):
    reader = DecompressionReader(filename)
    data = reader.read()

    print(data)
    return data

if __name__ == '__main__':
    args = parse_args()

    if not check_args(args):
        exit()

    if args.action == 'e':
        encode(args.filename)

    if args.action == 'd':
        decode(args.filename)
