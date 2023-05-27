import unittest
from symbol_code import SymbolCodeMap

class TestSymbolCodeMap(unittest.TestCase):
    def test_none(self):
        self.assertRaises(ValueError, SymbolCodeMap, None)

    def test_empty(self):
        self.assertRaises(ValueError, SymbolCodeMap, b"")

    def test_one_byte(self):
        symbol_code = SymbolCodeMap(b"a")

        self.assertEqual(1, len(symbol_code))
        self.assertIn(symbol_code[ord('a')], {'0', '1'})

    def test_two_bytes(self):
        symbol_code = SymbolCodeMap(b"ab")

        self.assertEqual(2, len(symbol_code))
        self.assertEqual({'0', '1'}, set(symbol_code.values()))
        self.assertNotEqual(symbol_code[ord('a')], symbol_code[ord('b')])

    def test_three_bytes(self):
        symbol_code = SymbolCodeMap(b"abc")

        self.assertEqual(3, len(symbol_code))

        self.assertIn(
            set(symbol_code.values()),
            [{'0', '10', '11'}, {'1', '01', '00'}])

    def test_privet(self):
        symbol_code = SymbolCodeMap(b"privet")

        self.assertEqual(6, len(symbol_code))

        # 2 байта с кодами длины 2
        self.assertEqual(2,
            len({code for code in symbol_code.values() if len(code) == 2}))

        # 4 байта с кодами длины 3
        self.assertEqual(4,
            len({code for code in symbol_code.values() if len(code) == 3}))

    def test_hello_world(self):
        symbol_code = SymbolCodeMap(b"HelloWorld")

        self.assertEqual(7, len(symbol_code))

        self.assertEqual(2, len(symbol_code[ord('l')]))
        self.assertEqual(2, len(symbol_code[ord('o')]))

        # l, o 
        self.assertEqual(2,
            len({code for code in symbol_code.values() if len(code) == 2}))

        # w, r, d
        self.assertEqual(3,
            len({code for code in symbol_code.values() if len(code) == 3}))

        # H, e
        self.assertEqual(2,
            len({code for code in symbol_code.values() if len(code) == 4}))

if __name__ == '__main__':
    unittest.main()