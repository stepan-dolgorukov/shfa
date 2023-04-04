#!/usr/bin/env python3

from collections import defaultdict

class SymbolCountMap:
    def __init__(self, data: str):
        self.symbol_count = defaultdict(int)
        for symbol in data:
            self.symbol_count[symbol] += 1

    def at(self, symbol: str):
        return self.symbol_count[symbol]
