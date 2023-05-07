#!/usr/bin/env python3

import unittest
from symbol_probability import SymbolProbabilityMap


class TestSymbolProbabilityMap(unittest.TestCase):
    def test_empty_string(self):
        """Тест пустой строки."""
        s = ''
        m = SymbolProbabilityMap(s)

        self.assertEqual(0, len(m))
        self.assertEqual(0, len(m.keys()))
        self.assertEqual(0, len(m.values()))
        self.assertEqual(0, len(m.items()))

        # chr(i) определена на 0 <= i <= 0x10ffff
        for char_code in range(0, 0x10ffff + 1):
            char = chr(char_code)
            self.assertGreater(0, m.at(char))

    def test_char_equal_probability_string(self):
        """Проверка строки с равными вероятностями символов."""
        s = 'abcde'
        m = SymbolProbabilityMap(s)

        self.assertEqual(5, len(m.items()))
        self.assertEqual(1. / 5, m.at('a'))
        self.assertEqual(1. / 5, m.at('b'))
        self.assertEqual(1. / 5, m.at('c'))
        self.assertEqual(1. / 5, m.at('d'))
        self.assertEqual(1. / 5, m.at('e'))

        # chr(i) определена на 0 <= i <= 0x10ffff
        for char_code in range(0, 0x10ffff + 1):
            char = chr(char_code)
            if char not in s:
                self.assertGreater(0, m.at(char))

    def test_char_diff_probability_string(self):
        """Проверка строки с разными вероятностями символов."""
        s = 'abarak'
        m = SymbolProbabilityMap(s)

        self.assertEqual(len(set(s)), len(m.items()))
        self.assertEqual(3. / len(s), m.at('a'))
        self.assertEqual(1. / len(s), m.at('b'))
        self.assertEqual(1. / len(s), m.at('r'))
        self.assertEqual(1. / len(s), m.at('k'))

        # chr(i) определена на 0 <= i <= 0x10ffff
        for char_code in range(0, 0x10ffff + 1):
            char = chr(char_code)
            if char not in s:
                self.assertGreater(0, m.at(char))

if __name__ == '__main__':
    unittest.main()
