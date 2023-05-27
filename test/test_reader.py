from reader import DecompressionReader, Reader
import unittest
from unittest.mock import Mock, patch, mock_open
from bitstring import BitArray
import pathlib
from nice_filename import NotNiceFileName


class TestDecompressionReader(unittest.TestCase):
    def test_filename_none(self):
        self.assertRaises(NotNiceFileName, DecompressionReader, None)

    def test_filename_empty(self):
        self.assertRaises(NotNiceFileName, DecompressionReader, '')

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

            'length': 2 + 2 + (2 * 2) + 2,


            # hashlib.new("sha256", b"Hello").hexdigest()
            'hashcode': "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
        })

        self.assertEqual(b'Hello', reader.read())

    def test_bad_header_read(self):

        def dummy_exists(fname: pathlib.Path):
            return fname == pathlib.Path('input.txt')

        with patch("builtins.open", mock_open(read_data="Bad-Header")):
            with patch.object(pathlib.Path, "exists", dummy_exists):
                reader = DecompressionReader('input.txt')
                self.assertRaises(ValueError, reader.read)

    def test_bad_encoded_read(self):

        def dummy_exists(fname: pathlib.Path):
            return fname == pathlib.Path('input.txt')

        # Для этого теста все ключи заголовка не нужны
        DecompressionReader.read_info = Mock(return_value={
            'header-length': 128
        })

        # Байтовая строка может быть любой не пустой
        with patch("__main__.open", mock_open(read_data=b"")):
            with patch.object(pathlib.Path, "exists", dummy_exists):
                reader = DecompressionReader('input.txt')
                self.assertRaises(ValueError, reader.read)


class TestReader(unittest.TestCase):
    def test_filename_none(self):
        self.assertRaises(NotNiceFileName, Reader, None)

    def test_filename_empty(self):
        self.assertRaises(NotNiceFileName, Reader, '')

    def test_correct_filename(self):

        def dummy_exists(fname: pathlib.Path):
            return fname == pathlib.Path('input')

        try:
            with patch.object(pathlib.Path, "exists", dummy_exists):
                Reader('input')
        except Exception:
            self.fail()

    @patch('pathlib.Path.exists', return_value=True)
    def test_read(self, mock_path_exists):
        with patch("builtins.open", mock_open(read_data=b"Hello")):
            reader = Reader("input")
            self.assertEqual(b"Hello", reader.read())


if __name__ == '__main__':
    unittest.main()
