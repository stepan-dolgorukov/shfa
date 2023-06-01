import unittest
from probability import byte_probability


class TestProbability(unittest.TestCase):
    def test_none(self):
        self.assertRaises(ValueError, byte_probability, None)

    def test_empty(self):
        self.assertRaises(ValueError, byte_probability, b'')

    def test_one_byte(self):
        byte_prob = byte_probability(b'a')
        self.assertEqual(1, byte_prob[ord('a')])

    def test_two_bytes(self):
        match = {
            b'aa': {ord('a'): 1},
            b'ab': {ord('a'): 1 / 2, ord('b'): 1 / 2}
        }

        for data in match:
            byte_prob = byte_probability(data)
            self.assertAlmostEqual(match[data], byte_prob)

    def test_three_bytes(self):
        match = {
            b'abc': {ord('a'): 1 / 3, ord('b'): 1 / 3, ord('c'): 1 / 3},
            b'aac': {ord('a'): 2 / 3, ord('c'): 1 / 3}
        }

        for data in match:
            self.assertAlmostEqual(match[data], byte_probability(data))

    def test_natural_speech(self):
        match = {
            b'Hey, Bob. How are you today?': {
                ord('H'): 2 / 28,
                ord('e'): 2 / 28,
                ord('y'): 3 / 28,
                ord(','): 1 / 28,
                ord(' '): 5 / 28,
                ord('B'): 1 / 28,
                ord('o'): 4 / 28,
                ord('b'): 1 / 28,
                ord('.'): 1 / 28,
                ord('w'): 1 / 28,
                ord('a'): 2 / 28,
                ord('r'): 1 / 28,
                ord('u'): 1 / 28,
                ord('t'): 1 / 28,
                ord('d'): 1 / 28,
                ord('?'): 1 / 28
            },

            b'Let me speak from my heart, my friends': {
                ord('L'): 1 / 38,
                ord('e'): 5 / 38,
                ord('t'): 2 / 38,
                ord(' '): 7 / 38,
                ord('m'): 4 / 38,
                ord('s'): 2 / 38,
                ord('p'): 1 / 38,
                ord('a'): 2 / 38,
                ord('k'): 1 / 38,
                ord('f'): 2 / 38,
                ord('r'): 3 / 38,
                ord('o'): 1 / 38,
                ord('y'): 2 / 38,
                ord('h'): 1 / 38,
                ord(','): 1 / 38,
                ord('i'): 1 / 38,
                ord('n'): 1 / 38,
                ord('d'): 1 / 38
            }
        }

        for data in match:
            self.assertEqual(match[data], byte_probability(data))


if __name__ == '__main__':
    unittest.main()
