#!/usr/bin/env python3

from writer import CompressionWriter, Writer
from reader import DecompressionReader, Reader

from argparser import ArgParser
from argchecker import ArgChecker, Conclusion, Action


def write_encode(source_filename: str, destination_filename: str) -> None:
    """Считать информацию с файла, записать заголовок и сжатую
    информацию в файл

    Аргументы:
    source_filename -- файл ввода, в нём лежит информация, которую нужно сжать
    destination_filename -- файл вывода, в него будет помещён контейнер (заголовок & сжатая информация)
    """

    reader = Reader(source_filename)
    data: bytes = reader.read()

    writer = CompressionWriter(data, destination_filename)
    writer.write()


def write_decode(source_filename: str, destination_filename: str) -> None:
    """Считать заголок & сжатые данные из файла,
    вернуть раскодированную информацию

    Аргументы:
    source_filename -- файл, в котором содержится заголовок & сжатые данные
    destination_filename -- файл, в который нужно записать расжатую информацию
    """

    reader = DecompressionReader(source_filename)
    data: bytes = reader.read()

    writer = Writer(data, destination_filename)
    writer.write()


if __name__ == '__main__':
    parser = ArgParser()
    args = parser.parse()
    checker = ArgChecker(args)

    if Conclusion.POSITIVE != checker.get_conclusion():
        print(checker.get_message())
        print(parser.brief())
        exit(1)

    if parser.args.action == Action.ENCODE:
        write_encode(args.filename, args.output)

    if parser.args.action == Action.DECODE:
        write_decode(args.filename, args.output)