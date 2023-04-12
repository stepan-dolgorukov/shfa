#!/usr/bin/env python3

import unittest
from symbol_count import SymbolCountMap


class TestSymbolCountMap(unittest.TestCase):
    def test_empty_string(self):
        """Тест на пустую строчку."""
        s = ''
        m = SymbolCountMap(s)

        self.assertEqual(0, len(m.items()))
        self.assertEqual(-1, m.at(chr(0)))
        self.assertEqual(-1, m.at('a'))

    def test_upper_and_lower(self):
        """Тест на обработку заглавных и строчных символов."""
        s = 'aAbBYyZwzWaA'
        m = SymbolCountMap(s)

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


if __name__ == '__main__':
    unittest.main()
