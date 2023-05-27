import unittest
from hashcode import hashcode

class HashcodeTest(unittest.TestCase):
    def test_wrong_data_type(self):
        self.assertRaises(TypeError, hashcode, str())

    def test_right_data(self):
        self.assertEqual("185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969", hashcode(b"Hello"))

if __name__ == '__main__':
    unittest.main()