#!/usr/bin/env python3

from math import ceil, log2

def find_split(symbol_prob):
    low_summa = sum(symbol_prob.values())
    up_summa = 0
    min_nonzero_diff = low_summa
    split_index = 0

    for index, value in enumerate(symbol_prob.values()):
        up_summa += value
        low_summa -= value
        diff = abs(up_summa - low_summa)
        print(up_summa, low_summa, )
        if diff != 0:
            if diff <= min_nonzero_diff:
                min_nonzero_diff = diff
                split_index = index

    return split_index

def parts(symbol_prob):
    symbol_prob = sort(symbol_prob)

    part_left = dict()
    part_right = dict()

    keys = list(symbol_prob.keys())
    split_index = find_split(symbol_prob)
    part_left_keys = keys[:split_index+1]
    part_right_keys = keys[split_index+1:]

    print(part_left_keys, part_right_keys)

def sort(symbol_prob):
    return {k: v for k, v in sorted(symbol_prob.items(),
                                    key=lambda item: item[1],
                                    reverse=True)}

data = input()
symbols_info = dict()

for symbol in data:
    symbols_info[symbol] = 0

for symbol in data:
    symbols_info[symbol] += 1

for symbol in symbols_info:
    symbols_info[symbol] /= len(data)
    symbols_info[symbol] *= 100

print(symbols_info)
parts(symbols_info)
