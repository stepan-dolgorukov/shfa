import json
from accessify import private
from code_symbol import CodeSymbolMap
from encoder import Encoder

class CompressionWriter:
    def __init__(self, data: str, fname: str):
        self.fname = fname
        self.data = data
        self.symbol_map = None
        self.compressed = None
        self.info = None

    def write(self):
        if None is self.data_to_write:
            self.data_to_write = self.create_data_to_write()

        with open(self.fname, 'w') as file:
            file.write(self.data_to_write)

    @private
    def fill_info(self):
        info = dict()
        info["encoding"] = "ShannonFano"
        info["version"] = "Test"
        info["map"] = CodeSymbolMap(self.symbol_map).json()
        info["length"] = len(self.compressed)
        self.info = json.dumps(info)

    @private
    def create_compressed(self):
        encoder = Encoder(self.data)
        self.compressed = encoder.coded()
        self.symbol_map = encoder.map()
