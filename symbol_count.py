#!/usr/bin/env python3

from collections import defaultdict

class SymbolCountMap:
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

    def at(self, symbol: str):
        """Сколько раз встречается конкретный символ.

        symbol -- символ, количество раз которого узнаётся
        """
        if not symbol or len(symbol) != 1:
            return -1

        return self.symbol_count[symbol]

    def values(self):
        """Все количества, хранящиеся в словаре."""
        return self.symbol_count.values()

    def keys(self):
        """Все символы с подсчитанным количеством."""
        return self.symbol_count.keys()

    def items(self):
        """Все пары (символ, количество)."""
        return self.symbol_count.items()

    def __len__(self):
        return len(self.symbol_count)
