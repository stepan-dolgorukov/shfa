import json
from accessify import private
from encoder import Encoder

class CompressionWriter:
    def __init__(self, data: str, fname: str):
        self.fname = fname

        encoder = Encoder(data)
        self.compressed_data = encoder.coded()
        self.symbol_map = encoder.map()
        self.data_to_write = None

    def write(self):
        if None is self.data_to_write:
            self.data_to_write = self.create_data_to_write()

        with open(self.fname, 'w') as file:
            file.write(self.data_to_write)

    @private
    def create_data_to_write(self):
        write_data = dict()
        write_data["encoding"] = "ShannonFano"
        write_data["version"] = "Test"
        write_data["data"] = self.compressed_data.uint
        write_data["map"] = self.symbol_map.json()
        return json.dumps(write_data)
