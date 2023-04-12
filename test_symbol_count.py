#!/usr/bin/env python3

import unittest
from symbol_count import SymbolCountMap


class TestSymbolCountMap(unittest.TestCase):
    def test_empty_string(self):
        """Тест на пустую строчку."""
        s = ''
        m = SymbolCountMap(s)

        self.assertEqual(0, len(m))
        self.assertEqual(0, len(m.keys()))
        self.assertEqual(0, len(m.values()))
        self.assertEqual(0, len(m.items()))

        # chr(i) определена на 0 <= i <= 0x10ffff
        for char_code in range(0, 0x10ffff + 1):
            char = chr(char_code)
            self.assertEqual(-1, m.at(char))

    def test_upper_and_lower(self):
        """Тест на обработку заглавных и строчных символов."""
        s = 'aAbBYyZwzWaA'
        m = SymbolCountMap(s)

        # a: 2
        # A: 2
        # b: 1
        # B: 1
        # Y: 1
        # y: 1
        # Z: 1
        # z: 1
        # w: 1
        # W: 1

        self.assertEqual(10, len(m))
        self.assertEqual(10, len(m.keys()))
        self.assertEqual(10, len(m.values()))
        self.assertEqual(10, len(m.items()))

        self.assertEqual(2, m.at('a'))
        self.assertEqual(2, m.at('A'))
        self.assertEqual(1, m.at('b'))
        self.assertEqual(1, m.at('B'))
        self.assertEqual(1, m.at('Y'))
        self.assertEqual(1, m.at('y'))
        self.assertEqual(1, m.at('z'))
        self.assertEqual(1, m.at('Z'))
        self.assertEqual(1, m.at('w'))
        self.assertEqual(1, m.at('W'))

        # chr(i) определена на 0 <= i <= 0x10ffff
        for char_code in range(0, 0x10ffff + 1):
            char = chr(char_code)
            if char not in s:
                self.assertEqual(-1, m.at(char))


if __name__ == '__main__':
    unittest.main()
