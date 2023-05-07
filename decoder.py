from bitstring import BitArray
from symbol_code import SymbolCodeMap
from code_symbol import CodeSymbolMap
from accessify import private

class Decoder:
    """Декодировка информации. Коды берутся из переданного отображения."""

    def __init__(self, data: BitArray, symbol_code: SymbolCodeMap):
        self.code_symbol = CodeSymbolMap(symbol_code)
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

        decompressed = ""
        code = ""
        for i in range(len(self.data)):
            code += str(int(self.data[i]))
            if self.code_symbol.has(code):
                decompressed += self.code_symbol.at(code)
                code = ""
        if code:
            decompressed += self.code_symbol.at(code)
        return decompressed
