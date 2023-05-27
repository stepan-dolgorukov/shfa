import json
from accessify import private
from code_symbol import CodeSymbolMap
from encoder import Encoder
from pathlib import Path
from symbol_code import SymbolCodeMap
from bitstring import BitArray
from hashcode import hashcode


class CompressionWriter:
    """Сжимает строку и записывает в указанный файл."""

    def __init__(self, data: bytes, fname: str):
        self.init_arguments_checking(data, fname)

        self.fname = fname
        self.data = data
        self.encoder = None

    @private
    def pad(self, length: int) -> int:
        return (8 - (length % 8)) % 8

    def write(self) -> None:
        """Записать заголовок & сжатые данные в файл. """

        if self.encoder is None:
            self.encoder = Encoder(self.data)

        self.write_header()
        self.write_compressed()

    @private
    def write_header(self) -> None:
        """Записать заголовок в файл."""

        try:
            with open(self.fname, "w") as file:
                file.write(self.get_header())
                file.write("\n")
        except Exception:
            raise IOError("Не удалось записать заголовок в файл")

    @private
    def write_compressed(self) -> None:
        """Записать сжатую строку в файл."""

        try:
            with open(self.fname, "ab") as file:
                compressed = self.encoder.coded()
                pad = self.pad(len(compressed))

                compressed.append(pad)
                file.write(compressed.bytes)
        except Exception:
            raise IOError(
                "Не удалось записать закодированную информацию в файл")

    @private
    def bytes_with_padding(self, data: BitArray) -> bytes:
        pad = self.pad(len(data))
        data.append(pad)

        return data.bytes

    @private
    def get_header(self) -> str:
        """Сформировать заголовок."""

        header = None
        code_symbol = CodeSymbolMap(self.encoder.map())

        try:
            info = dict()
            info["encoding"] = "ShannonFano"
            info["version"] = "Test"
            info["map"] = code_symbol.json()
            info["length"] = len(self.encoder.coded())

            info["hashcode"] = hashcode(self.data)

            header = json.dumps(info)
        except Exception:
            raise Exception("Не удалось сформировать заголовок")

        return header

    @private
    def init_arguments_checking(self, data: bytes, fname: str) -> None:
        """Проверка типов & состояний аргументов, переданных в __init__."""

        if not isinstance(data, bytes):
            raise TypeError(
                "Данные должны быть байтовой строкой (тип «bytes»)")

        if len(data) <= 0:
            raise ValueError("Длина байтовой строки должна быть строго "
                             "положительной")

        if not isinstance(fname, str):
            raise TypeError("Имя файла должно задаваться строкой типа «str»")

        if not fname:
            raise ValueError("Не указано имя файла")

        if Path(fname).exists():
            raise ValueError(f"Файл {fname} существует")


class Writer():
    """Запись байтов в файл."""

    def __init__(self, data: bytes, fname: str):
        self.arguments_checking(data, fname)

        self.data = data
        self.fname = fname

    def write(self) -> None:
        """Записать информацию."""

        try:
            with open(self.fname, "wb") as out:
                out.write(self.data)
        except Exception:
            raise IOError(f"Ошибка записи в файл {self.fname}")

    @private
    def file_exists(self, fname: str) -> bool:
        """Существует ли файл.

        fname -- имя файла, существование которого требуется узнать.
        """

        return Path(fname).exists()

    @private
    def arguments_checking(self, data: bytes, fname: str) -> None:
        """Проверка аргументов (типы & состояния), передаваемых в __init__.

        data -- информация на запись
        fname -- имя файла, в который нужно записать data
        """

        if not isinstance(data, bytes):
            raise TypeError("Информация должна быть типа bytes")

        if not data:
            raise ValueError("Передана пустая байтовая строка")

        if not isinstance(fname, str):
            raise TypeError("Имя файла должно быть строкой str")

        if not fname:
            raise ValueError("Передано пустое имя файла")

        if self.file_exists(fname):
            raise ValueError(f"Файл {fname} уже существует")
