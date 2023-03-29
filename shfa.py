#!/usr/bin/env python3

def find_split(symbol_prob):
    low_summa = sum(symbol_prob.values())
    up_summa = 0
    min_diff = low_summa
    split_index = 0

    for index, value in enumerate(symbol_prob.values()):
        up_summa += value
        low_summa -= value
        diff = abs(up_summa - low_summa)
        #  print(up_summa, low_summa, )
        if diff <= min_diff:
            min_diff = diff
            split_index = index

    return split_index


def codes(symbol_prob, code=''):

    if len(symbol_prob) <= 2:
        #  print(symbol_prob)

        if len(symbol_prob) == 2:
            for i, k in enumerate(symbol_prob):
                yield (code + str(i), k)
        else:
            yield code, *symbol_prob.keys()
        return

    symbol_prob = sort(symbol_prob)

    part_left = dict()
    part_right = dict()

    keys = list(symbol_prob.keys())
    split_index = find_split(symbol_prob)

    part_left_keys = keys[:split_index + 1]
    part_right_keys = keys[split_index + 1:]

    for key in part_left_keys:
        part_left[key] = symbol_prob[key]

    for key in part_right_keys:
        part_right[key] = symbol_prob[key]

    #  print(part_left, part_right)

    yield from codes(part_left, code + '0')
    yield from codes(part_right, code + '1')


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

#  print(symbols_info)
for code in codes(symbols_info):
    print(code)
