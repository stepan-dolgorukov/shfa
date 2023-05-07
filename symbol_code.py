#!/usr/bin/env python3

from typing_extensions import override
from symbol_probability import SymbolProbabilityMap
from symbol_map import SymbolMap
from accessify import private
import json


class SymbolCodeMap(SymbolMap):
    """Отображение «символ→код»."""

    def __init__(self, data: str):
        self.symbol_code = dict()

        if not data:
            return

        self.symbol_prob = SymbolProbabilityMap(data)
        self.codes(self.symbol_prob)

    @private
    def sort(self, symbol_prob):
        return {k: v for k, v in sorted(symbol_prob.items(),
                                        key=lambda item: item[1],
                                        reverse=True)}

    @private
    def find_split(self, symbol_prob):
        low_summa = sum(symbol_prob.values())
        up_summa = 0
        min_diff = low_summa
        split_index = 0

        for index, value in enumerate(symbol_prob.values()):
            up_summa += value
            low_summa -= value
            diff = abs(up_summa - low_summa)
            if diff <= min_diff:
                min_diff = diff
                split_index = index

        return split_index

    @private
    def parts(self, symbol_prob, split_index):
        """Разбиение отображения на две части по индексу"""

        part_left = dict()
        part_right = dict()
        keys = list(symbol_prob.keys())

        for key in keys[:split_index + 1]:
            part_left[key] = symbol_prob[key]

        for key in keys[split_index + 1:]:
            part_right[key] = symbol_prob[key]

        return (part_left, part_right)


    @private
    def codes(self, symbol_prob, code=''):

        if len(symbol_prob) <= 2:
            # Если в отображении два прообраза, то index in {0,1}
            # Если один, то index = 0
            for index, symbol in enumerate(symbol_prob):
                self.symbol_code[symbol] = code + str(index)
            return

        symbol_prob = self.sort(symbol_prob)
        split_index = self.find_split(symbol_prob)

        part_left, part_right = self.parts(symbol_prob, split_index)

        self.codes(part_left, code + '0')
        self.codes(part_right, code + '1')

    @override
    def at(self, symbol: str):
        """Узнать код конкретного символа.

        symbol -- символ, количество раз которого узнаётся
        """
        if not symbol or len(symbol) != 1 or symbol not in self.symbol_code:
            return -1

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
