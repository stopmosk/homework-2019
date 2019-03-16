import unittest
from hangman_logic import check_letter, generate_string


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(generate_string('олололала', {'о', 'а'}), 'о_о_о_а_а')


if __name__ == '__main__':
    unittest.main()
