import unittest
from unittest.mock import Mock, patch
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

    @patch("pathlib.Path.exists")
    def test_output_file_exists(self, mock_path_exists):
        mock_path_exists = Mock(return_value=True)
        self.assertRaises(ValueError, CompressionWriter, b"Hello", "output")


class TestWriter(unittest.TestCase):
    def test_data_wrong_type(self):
        for data in (str(), int(), dict(), set()):
            self.assertRaises(TypeError, Writer, data, 'input')

    def test_data_empty(self):
        self.assertRaises(ValueError, Writer, b'', 'input')

    def test_filename_wrong_type(self):
        for filename in (bytes(), int(), dict(), set()):
            self.assertRaises(TypeError, Writer, b'Hello', filename)

    def test_output_file_exists(self):
        Writer.file_exists = Mock(return_value=True)
        self.assertRaises(ValueError, Writer, b"Hello", "output")

    def test_correct_arguments(self):
        Writer.file_exists = Mock(return_value=False)

        try:
            Writer(b"Hello", 'input')
        except Exception:
            self.fail()

    @patch("builtins.open")
    def test_good_write(self, mock_open):
        Writer.file_exists = Mock(return_value=False)
        writer = Writer(b"Hello", "output")

        writer.write()
        mock_open.return_value.__enter__.return_value.write.assert_called_once()

    @patch("builtins.open")
    def test_bad_write(self, mock_open):
        mock_open.side_effect = Exception("Откуда-то какая-то ошибка")

        Writer.file_exists = Mock(return_value=False)
        writer = Writer(b"Hello", "output")

        self.assertRaises(IOError, writer.write)


if __name__ == '__main__':
    unittest.main()
