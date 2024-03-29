from symbol_code import SymbolCodeMap
from accessify import private
from bitstring import BitArray


class Encoder:
    def __init__(self, data: bytes):
        """data -- информация, которую нужно закодировать"""

        self.init_arguments_checking(data)

        self.data = data
        self.symbol_code = SymbolCodeMap(data)
        self.compressed_data = None

    def coded(self) -> BitArray:
        """Получить информацию в сжатом виде."""
        if self.compressed_data is None:
            self.compressed_data = self.bitarray()
        return self.compressed_data

    def map(self) -> SymbolCodeMap:
        """Получить отображение «символ→код»."""
        return self.symbol_code

    @private
    def bitamount(self):
        """Вычислить количество битов, необходимых для сжатой строки."""
        return sum([len(code) for code in self.symbol_code.values()])

    @private
    def code_to_bitstr(self, code: str):
        """Преобразовать код символа в битовую строку."""
        bitstr = BitArray(len(code))
        for i in range(len(code)):
            bitstr[i] = code[i] == '1'
        return bitstr

    @private
    def bitarray(self):
        """Сформировать массив битов. Сжатая строка помещается в массив."""
        self.compressed_data = BitArray()

        for char in self.data:
            code = self.symbol_code.at(char)
            code_bitstr = self.code_to_bitstr(code)
            self.compressed_data.append(code_bitstr)

        return self.compressed_data

    @private
    def init_arguments_checking(self, data: bytes) -> None:
        """Функция проверки аргументов, переданных в инициализатор __init__.

        data -- информация, переданная на кодировку (сжатие)
        """

        if not isinstance(data, bytes):
            raise ValueError("Поддерживается работа только с байтовыми"
                             "строками")

        if len(data) <= 0:
            raise ValueError("Длина должна быть строго положительной")
