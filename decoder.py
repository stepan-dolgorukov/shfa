from bitstring import BitArray
from symbol_code import SymbolCodeMap
from code_symbol import CodeSymbolMap
from accessify import private

class Decoder:
    """Декодировка информации. Коды берутся из переданного отображения."""

    def __init__(self, data: BitArray, code_symbol: dict[str:int]):
        self.code_symbol = code_symbol
        self.data = data
        self.decompressed_data = None

    def decoded(self):
        """Получить информацию, которую раскодировал."""

        if self.decompressed_data is None:
            self.decompressed_data = self.decode()
        return self.decompressed_data

    @private
    def decode(self):
        """Раскодировать информацию."""

        decompressed = b""
        code = ""

        for i in range(len(self.data)):
            code += str(int(self.data[i]))
            if code in self.code_symbol:
                decompressed += bytes([self.code_symbol[code]])
                code = ""

        return decompressed
