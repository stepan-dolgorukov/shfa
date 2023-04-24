from symbol_code import SymbolCodeMap
from accessify import private

class CodeSymbolMap():
    def __init__(self, symbol_code: SymbolCodeMap):
        self.code_symbol = self.inverse(symbol_code)

    @private
    def inverse(self, symbol_code: SymbolCodeMap):
        inversed = dict()
        for symbol, code in symbol_code.items():
            inversed[code]=symbol
        return inversed

    def at(self, code):
        return self.code_symbol[code]

    def items(self):
        return self.code_symbol.items()

    def keys(self):
        return self.code_symbol.keys()

    def has(self, code: str):
        return code in self.code_symbol
