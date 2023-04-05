#!/usr/bin/env python3

from collections import defaultdict
from symbol_count import SymbolCountMap
from math import inf

class SymbolProbabilityMap:
    def __init__(self, data: str):
        if not data:
            self.symbol_prob = {}
            return

        symbol_count = SymbolCountMap(data)
        self.symbol_prob = defaultdict(float)

        for symbol in data:
            self.symbol_prob[symbol] = symbol_count.at(symbol) / len(data)

    def at(self, symbol: str):
        if not symbol:
            return -inf

        return self.symbol_prob[symbol]

    def values(self):
        return self.symbol_prob.values()

    def keys(self):
        return self.symbol_prob.keys()

    def items(self):
        return self.symbol_prob.items()

    def __len__(self):
        return len(self.symbol_prob)
