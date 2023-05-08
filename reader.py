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
                self.read_info()
                self.read_encoded()
                self.decode()
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
            self.info = json.loads(info)
            self.info["map"] = json.loads(self.info["map"])
        except Exception:
            raise ValueError

        self.info["header-length"] = header_length

    @private
    def read_encoded(self):
        """Считать закодированную информацию.

        Информация записана байтово, не символьно.
        """

        with open(self.fname, "rb") as file:
            file.seek(self.info["header-length"])
            self.encoded = BitArray(file.read())

    @private
    def decode(self):
        code_symbol = self.info["map"]

        decoder = Decoder(self.encoded, code_symbol)
        self.decoded = decoder.decoded()