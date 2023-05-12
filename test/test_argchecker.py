import unittest
from unittest.mock import Mock
from argparse import Namespace
from argchecker import ArgChecker, Conclusion, CheckMessage, Action

class TestArgChecker(unittest.TestCase):
    def test_none(self):
        self.assertRaises(ValueError, ArgChecker, None)

    def test_no_action(self):
        checker = ArgChecker(Namespace(action=None))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)
        checker.check_arg_output = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_ACTION, checker.get_message())

    def test_incorrect_action(self):
        checker = ArgChecker(Namespace(action='bla-bla-bla'))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)
        checker.check_arg_output = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.INCORRECT_ACTION, checker.get_message())

    def test_action_encode(self):
        checker = ArgChecker(Namespace(action=Action.ENCODE))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)
        checker.check_arg_output = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.POSITIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.CORRECT, checker.get_message())

    def test_action_decode(self):
        checker = ArgChecker(Namespace(action=Action.DECODE))
        checker.check_arg_filename = Mock(return_value=CheckMessage.CORRECT)
        checker.check_arg_output = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.POSITIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.CORRECT, checker.get_message())

    def test_no_file_name(self):
        checker = ArgChecker(Namespace(filename=None))
        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_FILE_NAME, checker.get_message())

    def test_input_file_does_not_exist(self):
        checker = ArgChecker(Namespace(filename='input'))

        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)

        def file_exists(filename: str) -> bool:
            if filename == 'input': return False
            if filename == 'output': return False
            raise ValueError("Имя файла в тесте не участвует")

        checker.file_exists = Mock(side_effect=file_exists)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.FILE_DOESNT_EXIST, checker.get_message())

    def test_no_output_file_name(self):
        checker = ArgChecker(Namespace(filename='in.txt', output=None))
        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)

        def file_exists(filename: str) -> bool:
            if filename == 'in.txt': return True 
            if filename == 'out.txt': return False
            raise ValueError("Имя файла в тесте не участвует")

        checker.file_exists = Mock(side_effect=file_exists)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.NO_OUTPUT_FILE_NAME, checker.get_message())

    def test_output_file_exists(self):
        checker = ArgChecker(Namespace(output='output', filename='input'))
        checker.check_arg_action = Mock(return_value=CheckMessage.CORRECT)

        def file_exists(filename: str) -> bool:
            if filename == 'input': return True
            if filename == 'output': return True
            raise ValueError("Имя файла в тесте не участвует")

        checker.file_exists = Mock(side_effect=file_exists)

        self.assertEqual(Conclusion.NEGATIVE, checker.get_conclusion())
        self.assertEqual(CheckMessage.OUTPUT_FILE_EXIST, checker.get_message())

        checker.file_exists.assert_called_with('output')


if __name__ == '__main__':
    unittest.main()