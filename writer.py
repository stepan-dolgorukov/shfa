import json
from accessify import private
from code_symbol import CodeSymbolMap
from encoder import Encoder

class CompressionWriter:
    """Сжимает строку и записывает в указанный файл."""

    def __init__(self, data: bytes, fname: str):
        if not isinstance(data, bytes):
            raise TypeError("Данные должны быть байтовой строкой (тип «bytes»)")

        if len(data) <= 0:
            raise ValueError("Длина байтовой строки должна быть строго "
                "положительной")

        if not isinstance(fname, str):
            raise TypeError("Имя файла должно задаваться строкой типа «str»")

        if not fname:
            raise ValueError("Не указано имя файла")

        self.fname = fname
        self.data = data
        self.encoder = None

    @private
    def pad(self, length: int) -> int:
        return (8 - (length % 8)) % 8

    def write(self):
        """Записать заголовок & сжатые данные в файл. """

        if self.encoder is None:
            self.encoder = Encoder(self.data)

        self.write_header()
        self.write_compressed()

    @private
    def write_header(self):
        """Записать заголовок в файл."""

        try:
            with open(self.fname, "w") as file:
                file.write(self.get_header())
                file.write("\n")
        except Exception:
            raise IOError("Не удалось записать заголовок в файл")

    @private
    def write_compressed(self):
        """Записать сжатую строку в файл."""

        try:
            with open(self.fname, "ab") as file:
                compressed = self.get_compressed()
                pad = self.pad(len(compressed))

                compressed.append(pad)
                file.write(compressed.bytes)
        except Exception:
            raise IOError("Не удалось записать закодированную информацию в файл")

    @private
    def get_header(self):
        """Сформировать заголовок."""

        header = None

        try:
            info = dict()
            info["encoding"] = "ShannonFano"
            info["version"] = "Test"
            info["map"] = CodeSymbolMap(self.get_symbol_code_map()).json()
            info["length"] = len(self.get_compressed())
            header = json.dumps(info)
        except Exception:
            raise Exception("Не удалось сформировать заголовок")

        return header 

    @private
    def get_compressed(self):
        """Получить сжатую строку."""

        return self.encoder.coded()

    @private
    def get_symbol_code_map(self):
        """Получить отображение для раскодирования."""

        return self.encoder.map()