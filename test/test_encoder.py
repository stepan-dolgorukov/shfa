import unittest
from encoder import Encoder
from bitstring import BitArray


class TestEncoder(unittest.TestCase):
    def test_empty_data(self):
        data = bytes()
        self.assertRaises(ValueError, Encoder, data)

    def test_data_wrong_type(self):
        for data in (int(), dict(), set(), str(), tuple(), list()):
            self.assertRaises(ValueError, Encoder, data)

    def test_one_byte(self):
        data = b'a'
        encoder = Encoder(data)

        self.assertEqual('0', encoder.map()[ord('a')])
        self.assertEqual(BitArray([0]), encoder.coded())

    def test_two_bytes(self):
        data = b'ab'
        encoder = Encoder(data)

        self.assertIn(encoder.map()[ord('a')], {'0', '1'})
        self.assertIn(encoder.map()[ord('b')], {'0', '1'})
        self.assertIn(encoder.coded(), (BitArray([0, 1]), BitArray([1, 0])))


if __name__ == '__main__':
    unittest.main()
