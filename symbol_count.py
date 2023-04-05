#!/usr/bin/env python3

from collections import defaultdict

class SymbolCountMap:
    def __init__(self, data: str):
        if not data:
            self.symbol_count = {}
            return

        self.symbol_count = defaultdict(int)
        for symbol in data:
            self.symbol_count[symbol] += 1

    def at(self, symbol: str):
        if not symbol:
            return -1

        return self.symbol_count[symbol]

    def values(self):
        return self.symbol_count.values()

    def keys(self):
        return self.symbol_count.keys()

    def items(self):
        return self.symbol_count.items()

    def __len__(self):
        return len(self.symbol_count)
