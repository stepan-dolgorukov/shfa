from symbol_code import SymbolCodeMap
from accessify import private
import json
from bitstring import BitArray

class CodeSymbolMap:
    """Отображение «код символа→символ»

    Используется при декодировании.

    """
    def __init__(self, symbol_code: SymbolCodeMap):
        self.code_symbol = self.inverse(symbol_code)

    @private
    def inverse(self, symbol_code: SymbolCodeMap) -> dict[BitArray, str]:
        """Построить обратное отображение к отображению «символ→код»."""

        inversed = dict()
        for symbol, code in symbol_code.items():
            inversed[code]=symbol
        return inversed

    def at(self, code):
        """Получить символ по коду."""

        return self.code_symbol[code]

    def items(self):
        """Все элементы отображения.

        Элемент — пара (код, символ).
        """

        return self.code_symbol.items()

    def keys(self):
        """Все коды символов (множество прообразов). """

        return self.code_symbol.keys()

    def has(self, code: str):
        """Есть ли символ с указанным кодом."""

        return code in self.code_symbol

    def json(self):
        """Сформировать строку JSON."""

        return json.dumps(self.code_symbol)
