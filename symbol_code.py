#!/usr/bin/env python3

from typing_extensions import override
from symbol_map import SymbolMap
from accessify import private
import json

import probability


class SymbolCodeMap(SymbolMap):
    """Отображение «символ→код»."""

    def __init__(self, data: bytes):
        self.symbol_code = dict()

        if not data:
            return

        self.symbol_prob = probability.byte_probability(data)
        self.codes(self.symbol_prob)

    @private
    def sort(self, symbol_prob: dict[int, float]) -> dict[int, float]:
        return {k: v for k, v in sorted(symbol_prob.items(),
                                        key=lambda item: item[1],
                                        reverse=True)}

    @private
    def find_split(self, symbol_prob: dict[int, float]):
        low_summa = sum(symbol_prob.values())
        up_summa = 0

        for index, value in enumerate(symbol_prob.values()):
            up_summa += value
            low_summa -= value

            if (up_summa - low_summa) >= 0:
                return index

        return -1

    @private
    def parts(self, symbol_prob: dict[int, float], split_index: int):
        """Разбиение отображения на две части по индексу"""

        if split_index < 0:
            raise ValueError("Отрицательное значение индекса")

        part_left = dict()
        part_right = dict()
        keys = list(symbol_prob.keys())

        for key in keys[:split_index + 1]:
            part_left[key] = symbol_prob[key]

        for key in keys[split_index + 1:]:
            part_right[key] = symbol_prob[key]

        return (part_left, part_right)


    @private
    def codes(self, symbol_prob: dict[int: float], code: str=''):

        # Группа из двух символов
        # первому символу назначается код слева — приписывается ноль
        # второму назначается код справа — приписывается единица
        if len(symbol_prob) == 2:
            for index, symbol in enumerate(symbol_prob):
                self.symbol_code[symbol] = code + str(index)
            return

        # Группа из одного символа
        # К коду ничего не дописывается
        if len(symbol_prob) == 1:
            symbol = [symbol for symbol in symbol_prob][0]
            self.symbol_code[symbol] = code
            return

        symbol_prob = self.sort(symbol_prob)
        split_index = self.find_split(symbol_prob)

        part_left, part_right = self.parts(symbol_prob, split_index)

        self.codes(part_left, code + '0')
        self.codes(part_right, code + '1')

    @override
    def at(self, symbol: bytes):
        """Узнать код конкретного символа.

        symbol -- символ, количество раз которого узнаётся
        """
        if symbol not in self.symbol_code:
            return -1

        return self.symbol_code[symbol]

    def __getitem__(self, symbol):
        if symbol not in self.symbol_code:
            return ""

        return self.symbol_code[symbol]

    @override
    def keys(self):
        """Подаёт контейнер, содержащий все символы, у которых есть код."""
        return self.symbol_code.keys()

    @override
    def values(self):
        """Подаёт контейнер, содержащий все коды символов (образы)."""
        return self.symbol_code.values()

    @override
    def items(self):
        """Все пары (символ, код)."""
        return self.symbol_code.items()

    @override
    def __len__(self):
        """Количество символов, имеющих свой код."""
        return len(self.symbol_code)

    def __iter__(self):
        return self.symbol_code.__iter__()

    def json(self):
        """Получить строку JSON."""

        return json.dumps(self.symbol_code)
