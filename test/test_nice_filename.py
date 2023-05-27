import unittest
from nice_filename import file_name_is_nice

class NiceFileNameTest(unittest.TestCase):
    def test_none(self):
        self.assertFalse(file_name_is_nice(None))

    def test_empty_file_name(self):
        self.assertFalse(file_name_is_nice(''))

    def test_correct_file_name(self):
        self.assertTrue(file_name_is_nice('a'))

if __name__ == '__main__':
    unittest.main()