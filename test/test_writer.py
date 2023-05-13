import unittest
from unittest.mock import Mock
from bitstring import BitArray
from writer import CompressionWriter

class TestCompressionWriter(unittest.TestCase):
    def test_data_wrong_type(self):
        for data in (str(), int(), dict(), set()):
            self.assertRaises(TypeError, CompressionWriter, data, 'input')

    def test_data_empty(self):
        self.assertRaises(ValueError, CompressionWriter, b'', 'input')

    def test_filename_wrong_type(self):
        for filename in (bytes(), int(), dict(), set()):
            self.assertRaises(TypeError, CompressionWriter, b'Hello', filename)

    def test_filename_empty(self):
        self.assertRaises(ValueError, CompressionWriter, b'Hello', str())

if __name__ == '__main__':
    unittest.main()