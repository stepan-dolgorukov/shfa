import json
from accessify import private
from code_symbol import CodeSymbolMap
from encoder import Encoder

class CompressionWriter:
    """Сжимает строку и записывает в указанный файл."""

    def __init__(self, data: bytes, fname: str):
        self.fname = fname
        self.data = data
        self.symbol_map = None
        self.compressed = None
        self.info = None

    @private
    def pad(self, length: int) -> int:
        return (8 - (length % 8)) % 8

    def write(self):
        """Записать заголовок & сжатые данные в файл. """

        if None is self.compressed:
            self.create_compressed()
            self.fill_info()

        with open(self.fname, "w") as file:
            file.write(self.info)
            file.write("\n")

        with open(self.fname, "ab") as file:
            length = len(self.compressed)
            pad = self.pad(length)

            self.compressed.append(pad)

            file.write(self.compressed.bytes)

    @private
    def fill_info(self):
        """Заполнить заголовок. """

        info = dict()
        info["encoding"] = "ShannonFano"
        info["version"] = "Test"
        info["map"] = CodeSymbolMap(self.symbol_map).json()
        info["length"] = len(self.compressed)
        self.info = json.dumps(info)

    @private
    def create_compressed(self):
        """Закодировать (сжать) строку."""

        encoder = Encoder(self.data)
        self.compressed = encoder.coded()
        self.symbol_map = encoder.map()
