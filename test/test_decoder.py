import unittest
from decoder import Decoder
from bitstring import BitArray

class TestDecoder(unittest.TestCase):
    def test_wrong_encoded_data_type(self):
        for data in (int(), dict(), set(), str(), tuple(), list()):
            self.assertRaises(ValueError, Decoder, data, 0, {})

    def test_wrong_length_type(self):
        for length in (float(), dict(), set(), str(), tuple(), list()):
            self.assertRaises(ValueError, Decoder, BitArray([0]), length, {})

    def test_wrong_code_to_symbol_map_type(self):
        for code_symbol in (float(), int(), set(), str(), tuple(), list()):
            self.assertRaises(
                ValueError, Decoder, BitArray([0]), 1, code_symbol)

    def test_empty_code_to_symbol_map(self):
        self.assertRaises(ValueError, Decoder, BitArray([0]), 1, {})

    def test_negative_length(self):
        code_symbol = {
            '0': ord('a')
        }

        encoded = BitArray([0])
        length = -1

        self.assertRaises(ValueError, Decoder, encoded, length, code_symbol)

    def test_zero_length(self):
        code_symbol = {
            '0': ord('a')
        }

        encoded = BitArray([0])
        length = 0 

        self.assertRaises(ValueError, Decoder, encoded, length, code_symbol)

    def test_empty_encoded_data(self):
        code_symbol = {
            '0': ord('a')
        }

        encoded = BitArray()
        length = 1

        self.assertRaises(ValueError, Decoder, encoded, length, code_symbol)

    def test_length_greater_than_encoded_data_length(self):
        code_symbol = {
            '0': ord('a')
        }

        encoded = BitArray([0])
        length = 2

        self.assertRaises(ValueError, Decoder, encoded, length, code_symbol)

    def test_one_char(self):
        code_symbol = {
            '0': ord('a')
        }

        encoded = BitArray([0])
        length = 1

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'a', decoder.decoded())

    def test_one_char_with_padding(self):
        code_symbol = {
            '0': ord('a')
        }

        # Дополнили строку до кратной восьми длины
        encoded = BitArray(
            [0] + # a
            [0, 0, 0, 0, 0, 0, 0])

        # Длина нужной нам информации не меняется 
        length = 1

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'a', decoder.decoded())

    def test_two_chars(self):
        code_symbol = {
            '0': ord('a'),
            '1': ord('b')
        }

        encoded = BitArray([0, 1])
        length = 2

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'ab', decoder.decoded())

    def test_two_chars_with_padding(self):
        code_symbol = {
            '0': ord('a'),
            '1': ord('b')
        }

        encoded = BitArray(
            [0] + # a
            [1] + # b
            [0, 0, 0, 0, 0, 0, 0])

        length = 2

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'ab', decoder.decoded())

    def test_hello(self):
        code_symbol = {
            '00': ord('l'),
            '01': ord('e'),
            '10': ord('h'),
            '11': ord('o')
        }

        encoded = BitArray(
            [1, 0] + # h
            [0, 1] + # e
            [0, 0] + # l
            [0, 0] + # l
            [1, 1]   # o
        )

        length = 2 + 2 + 2 + 2 + 2

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'hello', decoder.decoded())

    def test_hello_with_padding(self):
        code_symbol = {
            '00': ord('l'),
            '01': ord('e'),
            '10': ord('h'),
            '11': ord('o')
        }

        encoded = BitArray(
            [1, 0] + # h
            [0, 1] + # e
            [0, 0] + # l
            [0, 0] + # l
            [1, 1] + # o
            [0, 0, 0, 0, 0, 0]
        )

        length = 2 + 2 + 2 + 2 + 2

        decoder = Decoder(encoded, length, code_symbol)
        self.assertEqual(b'hello', decoder.decoded())


if __name__ == '__main__':
  unittest.main()