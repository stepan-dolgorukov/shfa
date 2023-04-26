from accessify import private
from bitstring import BitArray
import json

class DecompressionReader:
    def __init__(self, fname: str):
        self.fname = fname
        self.decoded = None
        self.encoded = None
        self.info = None

    def read(self):
        if self.decoded == None:
            self.read_info()
            self.read_encoded()
            self.decode()
        return self.decoded

    @private
    def read_info(self):
        info = None

        with open(self.fname, 'r', errors="ignore") as file:
            info = file.readline()

        header_length = len(info)

        self.info = json.loads(info)
        self.info["map"] = json.loads(self.info["map"])
        self.info["header-length"] = header_length

    @private
    def read_encoded(self):
        with open(self.fname, "rb") as file:
            file.seek(self.info["header-length"])
            self.encoded = file.readline()

    @private
    def decode(self):
        self.decoded = ""
        self.encoded = BitArray(self.encoded)
        data_length = self.info["length"]
        char_code = ""

        for i in range(data_length):
            char_code += str(int(self.encoded[i]))

            if char_code not in self.info["map"]:
                continue

            self.decoded += self.info["map"][char_code]
            char_code = ""
