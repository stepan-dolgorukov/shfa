#!/usr/bin/env python3

from collections import defaultdict
from symbol_count import SymbolCountMap
from math import inf

class SymbolProbabilityMap:
    """Отображение «символ→вероятность»"""
    def __init__(self, data: str):
        if not data:
            self.symbol_prob = {}
            return

        symbol_count = SymbolCountMap(data)
        self.symbol_prob = defaultdict(float)

        for symbol in data:
            probability: float = symbol_count.at(symbol) / len(symbol_count)
            self.symbol_prob[symbol] = probability

    def at(self, symbol: str):
        """Вероятность указанного символа

        symbol -- символ, вероятность которого узнаётся
        """
        if not symbol or len(symbol) != 1 or symbol not in self.symbol_prob:
            return -inf

        return self.symbol_prob[symbol]

    def values(self):
        """Все вероятности, хранящиеся в словаре."""
        return self.symbol_prob.values()

    def keys(self):
        """Все символы, для которых посчитана вероятность."""
        return self.symbol_prob.keys()

    def items(self):
        """Все пары (символ, вероятность)."""
        return self.symbol_prob.items()

    def __len__(self):
        return len(self.symbol_prob)
