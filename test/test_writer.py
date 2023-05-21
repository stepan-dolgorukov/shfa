import unittest
from unittest.mock import Mock
from bitstring import BitArray
from writer import CompressionWriter, Writer


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


class TestWriter(unittest.TestCase):
    def test_data_wrong_type(self):
        for data in (str(), int(), dict(), set()):
            self.assertRaises(TypeError, Writer, data, 'input')

    def test_data_empty(self):
        self.assertRaises(ValueError, Writer, b'', 'input')

    def test_filename_wrong_type(self):
        for filename in (bytes(), int(), dict(), set()):
            self.assertRaises(TypeError, Writer, b'Hello', filename)

    def test_correct_arguments(self):
        Writer.file_exists = Mock(return_value=False)

        try:
            Writer(b"Hello", 'input')
        except Exception:
            self.fail()


if __name__ == '__main__':
    unittest.main()
