#!/usr/bin/env python3

from writer import CompressionWriter
from reader import DecompressionReader

from argparser import ArgParser
from argchecker import ArgChecker, Conclusion, Action

def encode(filename, output_filename):
    """Считать информацию с файла, записать заголовок и сжатую
    информацию в файл

    Аргументы:
    filename -- файл ввода, в нём лежит информация, которую нужно сжать
    output -- файл вывода, в него будет помещён контейнер
    """

    data = ""
    with open(filename, 'rb') as file:
        data = file.read()

    writer = CompressionWriter(data, output_filename)
    writer.write()

def decode(filename):
    """Считать заголок & сжатые данные из файла,
    вернуть раскодированную информацию

    Аргументы:
    filename -- файл, в котором содержится заголовок & сжатые данные
    """

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
        encode(args.filename, args.output)

    if parser.args.action == Action.DECODE:
        try:
            data = decode(args.filename)

            try:
                with open(parser.args.output, "wb") as out:
                    out.write(data)
            except Exception:
                print("Не удалось записать раскодированную информацию")
        except Exception:
            print("Не удалось раскодировать строку")
