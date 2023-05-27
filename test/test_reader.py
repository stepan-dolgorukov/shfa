from reader import DecompressionReader, Reader
import unittest
from unittest.mock import Mock, patch, mock_open
from bitstring import BitArray


class TestDecompressionReader(unittest.TestCase):
    def test_filename_none(self):
        self.assertRaises(TypeError, DecompressionReader, None)

    def test_filename_empty(self):
        self.assertRaises(ValueError, DecompressionReader, '')

    @patch("pathlib.Path.exists", return_value=True)
    def test_hello(self, mock_path_exists):
        reader = DecompressionReader('input')

        reader.read_encoded = Mock(return_value=BitArray(
            [1, 0] +  # H
            [0, 1] +  # e
            [0, 0] +  # l
            [0, 0] +  # l
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

    def test_bad_header_read(self):
        with patch("builtins.open", mock_open(read_data="Bad-Header")) as m:
            reader = DecompressionReader('input.txt')
            self.assertRaises(ValueError, reader.read)

    def test_bad_encoded_read(self):

        # Для этого теста все ключи заголовка не нужны
        DecompressionReader.read_info = Mock(return_value={
            'header-length': 128
        })

        # Байтовая строка может быть любой не пустой
        with patch("__main__.open", mock_open(read_data=b"")) as m:
            reader = DecompressionReader('input.txt')
            self.assertRaises(ValueError, reader.read)


class TestReader(unittest.TestCase):
    def test_filename_none(self):
        self.assertRaises(TypeError, Reader, None)

    def test_filename_empty(self):
        self.assertRaises(ValueError, Reader, '')

    def test_correct_filename(self):
        Reader.file_exists = Mock(return_value=True)

        try:
            Reader('input')
        except Exception:
            self.fail()

    def test_read(self):
        with patch("builtins.open", mock_open(read_data=b"Hello")):
            reader = Reader("input")
            self.assertEqual(b"Hello", reader.read())


if __name__ == '__main__':
    unittest.main()
