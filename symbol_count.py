#!/usr/bin/env python3

from collections import defaultdict
from typing_extensions import override
from symbol_map import SymbolMap

class SymbolCountMap(SymbolMap):
    """Отображение помогает вести подсчёт символов.
    Оно вида «символ->количество».
    """

    def __init__(self, data: str):
        if not data:
            self.symbol_count = {}
            return

        self.symbol_count = defaultdict(int)
        for symbol in data:
            self.symbol_count[symbol] += 1

    @override
    def at(self, symbol: str):
        """Сколько раз встречается конкретный символ.

        symbol -- символ, количество раз которого узнаётся
        """
        if not symbol or len(symbol) != 1 or symbol not in self.symbol_count:
            return -1

        return self.symbol_count[symbol]

    @override
    def values(self):
        """Все количества, хранящиеся в словаре."""
        return self.symbol_count.values()

    @override
    def keys(self):
        """Все символы с подсчитанным количеством."""
        return self.symbol_count.keys()

    @override
    def items(self):
        """Все пары (символ, количество)."""
        return self.symbol_count.items()

    def __len__(self):
        return len(self.symbol_count)
