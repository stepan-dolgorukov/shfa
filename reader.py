from accessify import private
from bitstring import BitArray
import json
from decoder import Decoder

class DecompressionReader:
    """Читает из файла и раскодирует информацию."""

    def __init__(self, fname: str):
        self.fname = fname
        self.decoded = None
        self.encoded = None
        self.info = None

    def read(self):
        """Получить раскодированную строку."""
        if self.decoded is None:
            try:
                self.info = self.read_info()
                self.encoded = self.read_encoded()
                self.decoded = self.decode()
            except Exception:
                raise ValueError
        return self.decoded

    @private
    def read_info(self):
        """Считать заголовок."""
        info = None

        with open(self.fname, 'r', errors="ignore") as file:
            info = file.readline()

        header_length = len(info)

        try:
            info = json.loads(info)
            info["map"] = json.loads(info["map"])
        except Exception:
            raise ValueError

        info["header-length"] = header_length
        return info

    @private
    def read_encoded(self):
        """Считать закодированную информацию.

        Информация записана байтово, не символьно.
        """

        encoded = None

        with open(self.fname, "rb") as file:
            file.seek(self.info["header-length"])
            encoded = BitArray(file.read())

        return encoded

    @private
    def decode(self):
        decoder = Decoder(self.encoded, self.info["length"], self.info["map"])
        return decoder.decoded()
