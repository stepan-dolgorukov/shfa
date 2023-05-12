import unittest
from unittest.mock import Mock
from argparse import Namespace
from argchecker import ArgChecker, Conclusion, CheckMessage

class TestArgChecker(unittest.TestCase):
    def test_none(self):
        self.assertRaises(ValueError, ArgChecker, None)

    def test_no_action(self):
        checker = ArgChecker(Namespace(action=None))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_ACTION, checker.get_message())

    def test_incorrect_action(self):
        checker = ArgChecker(Namespace(action='bla-bla-bla'))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.INCORRECT_ACTION, checker.get_message())

    def test_no_file_name(self):
        checker = ArgChecker(Namespace(filename=None))
        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_FILE_NAME, checker.get_message())

    def test_no_output_file_name(self):
        checker = ArgChecker(Namespace(output=None))

        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_OUTPUT_FILE_NAME, checker.get_message())

if __name__ == '__main__':
    unittest.main()