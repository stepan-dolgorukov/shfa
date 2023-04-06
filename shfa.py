#!/usr/bin/env python3

from symbol_code import SymbolCodeMap

if __name__ == '__main__':
    symbol_code = SymbolCodeMap("Hello world!")
    for symbol in symbol_code:
        print(symbol, symbol_code.at(symbol))
