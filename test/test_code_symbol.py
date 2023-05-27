import unittest
from code_symbol import CodeSymbolMap
from symbol_code import SymbolCodeMap

class CodeSymbolMapTest(unittest.TestCase):
    def test_five_letters_string(self):
        symbol_code = SymbolCodeMap(b"Hello")
        code_symbol = CodeSymbolMap(symbol_code)

        self.assertEqual(ord('H'), code_symbol.at(symbol_code[ord('H')]))
        self.assertEqual(ord('e'), code_symbol.at(symbol_code[ord('e')]))
        self.assertEqual(ord('l'), code_symbol.at(symbol_code[ord('l')]))
        self.assertEqual(ord('o'), code_symbol.at(symbol_code[ord('o')]))

        self.assertEqual({'00', '01', '10', '11'}, set(code_symbol.keys()))

        self.assertTrue(code_symbol.has('00'))
        self.assertTrue(code_symbol.has('01'))
        self.assertTrue(code_symbol.has('10'))
        self.assertTrue(code_symbol.has('11'))