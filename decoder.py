from bitstring import BitArray
from symbol_code import SymbolCodeMap
from code_symbol import CodeSymbolMap
from accessify import private


class Decoder:
    """Декодировка информации. Коды берутся из переданного отображения."""

    def __init__(self, data: BitArray, length: int,
                 code_symbol: dict[str:int]):

        if not isinstance(data, BitArray):
            raise ValueError("Поддерживается работа только со строками байтов")

        if not isinstance(length, int):
            raise ValueError("Длина должна задаваться целым числом")

        if not isinstance(code_symbol, dict):
            raise ValueError("Отображение «код→символ» должно быть словарём")

        if length <= 0:
            raise ValueError("Длина должна быть строго положительной")

        if len(data) <= 0:
            raise ValueError("Невалидная длина закодированной строки")

        if len(data) < length:
            raise ValueError("Длина закодированной строки меньше указанной "
                             "длины")

        if len(code_symbol) <= 0:
            raise ValueError("Отображение не должно быть пустым")

        self.code_symbol = code_symbol
        self.data = data
        self.data_length = length
        self.decompressed_data = None

    def decoded(self) -> bytes:
        """Получить информацию, которую раскодировал."""

        if self.decompressed_data is None:
            self.decompressed_data = self.decode()
        return self.decompressed_data

    @private
    def decode(self) -> bytes:
        """Раскодировать информацию."""

        decompressed = b""
        code = ""

        for i in range(self.data_length):
            code += str(int(self.data[i]))
            if code in self.code_symbol:
                decompressed += bytes([self.code_symbol[code]])
                code = ""

        return decompressed
