from encoder import Encoder
from reader import DecompressionReader
import unittest
from unittest.mock import Mock
from bitstring import BitArray

class TestDecompressionReader(unittest.TestCase):
    def test_filename_none(self):
        self.assertRaises(TypeError, DecompressionReader, None)

    def test_filename_empty(self):
        self.assertRaises(ValueError, DecompressionReader, '')

    def test_hello(self):
        reader = DecompressionReader('input')

        reader.read_encoded = Mock(return_value=BitArray(
            [1, 0] + # H
            [0, 1] + # e
            [0, 0] + # l
            [0, 0] + # l
            [1, 1]   # o
        ))

        reader.read_info = Mock(return_value={
            'map': {
                '00': ord('l'),
                '01': ord('e'),
                '10': ord('H'),
                '11': ord('o')
            },

            'length': 2 + 2 + (2 * 2) + 2
        })

        self.assertEqual(b'Hello', reader.read())


if __name__ == '__main__':
    unittest.main()