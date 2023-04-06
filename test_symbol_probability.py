#!/usr/bin/env python3

import unittest
from symbol_probability import SymbolProbabilityMap

class TestSymbolProbabilityMap(unittest.TestCase):
    def test_empty_string(self):
        s = ''
        m = SymbolProbabilityMap(s)

        self.assertEqual(0, len(m.items()))
        self.assertGreater(0, m.at(chr(0)))
        self.assertGreater(0, m.at('a'))

    def test_char_equal_probability_string(self):
        s = 'abcde'
        m = SymbolProbabilityMap(s)

        self.assertEqual(5, len(m.items()))
        self.assertEqual(1./5, m.at('a'))
        self.assertEqual(1./5, m.at('b'))
        self.assertEqual(1./5, m.at('c'))
        self.assertEqual(1./5, m.at('d'))
        self.assertEqual(1./5, m.at('e'))

    def test_char_diff_probability_string(self):
        s = 'abarak'
        m = SymbolProbabilityMap(s)

        self.assertEqual(len(set(s)), len(m.items()))
        self.assertEqual(3./len(s), m.at('a'))
        self.assertEqual(1./len(s), m.at('b'))
        self.assertEqual(1./len(s), m.at('r'))
        self.assertEqual(1./len(s), m.at('k'))

if __name__ == '__main__':
    unittest.main()
