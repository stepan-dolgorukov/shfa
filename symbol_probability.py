#!/usr/bin/env python3

from collections import defaultdict
from typing_extensions import override
from symbol_count import SymbolCountMap
from symbol_map import SymbolMap
from math import inf


class SymbolProbabilityMap(SymbolMap):
    """Отображение «символ→вероятность»"""

    def __init__(self, data: bytes):
        if not data:
            self.symbol_prob = {}
            return

        symbol_count = SymbolCountMap(data)
        self.symbol_prob = defaultdict(float)

        for symbol in data:
            probability: float = symbol_count.at(symbol) / len(data)
            self.symbol_prob[symbol] = probability

    @override
    def at(self, symbol: bytes):
        """Вероятность указанного символа

        symbol -- символ, вероятность которого узнаётся
        """
        if symbol not in self.symbol_prob:
            return -inf

        return self.symbol_prob[symbol]

    @override
    def values(self):
        """Все вероятности, хранящиеся в словаре."""
        return self.symbol_prob.values()

    @override
    def keys(self):
        """Все символы, для которых посчитана вероятность."""
        return self.symbol_prob.keys()

    @override
    def items(self):
        """Все пары (символ, вероятность)."""
        return self.symbol_prob.items()

    @override
    def __len__(self):
        """Получить количество прообразов в отображении.

        Прообразы — символы, которые отображаются в вероятность.
        """

        return len(self.symbol_prob)
