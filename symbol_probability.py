#!/usr/bin/env python3

from collections import defaultdict
from symbol_count import SymbolCountMap

class SymbolProbabilityMap:
    def __init__(self, data: str):
        symbol_count = SymbolCountMap(data)
        self.symbol_prob = defaultdict(float)

        for symbol in data:
            self.symbol_prob[symbol] = symbol_count.at(symbol) / len(data)

    def at(self, symbol: str):
        return self.symbol_prob[symbol]
