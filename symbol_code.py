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
            #  print(up_summa, low_summa, )
            if diff <= min_diff:
                min_diff = diff
                split_index = index

        return split_index

    @private
    def codes(self, symbol_prob, code=''):

        if len(symbol_prob) <= 2:
            #  print(self.symbol_prob)

            if len(symbol_prob) == 2:
                for i, k in enumerate(symbol_prob):
                    #  yield (code + str(i), k)
                    self.symbol_code[k] = code + str(i)
            else:  # == 1
                #  yield code, *self.symbol_prob.keys()
                k = list(symbol_prob.keys())[0]
                self.symbol_code[k] = 0 if code == '' else code
            return

        symbol_prob = self.sort(symbol_prob)

        part_left = dict()
        part_right = dict()

        keys = list(symbol_prob.keys())
        split_index = self.find_split(symbol_prob)

        part_left_keys = keys[:split_index + 1]
        part_right_keys = keys[split_index + 1:]

        for key in part_left_keys:
            part_left[key] = symbol_prob[key]

        for key in part_right_keys:
            part_right[key] = symbol_prob[key]

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
        return json.dumps(self.symbol_code)
