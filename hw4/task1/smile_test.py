import unittest
from smile_logic import is_correct


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_correct('мыш (кродется)'))
        self.assertTrue(is_correct('внешний долг США over 9000'))
        self.assertTrue(is_correct('()[]{}'))
        self.assertTrue(is_correct('((({{{}}})))'))
        self.assertTrue(is_correct('[[]]'))
        self.assertTrue(is_correct('[/]*[(u)s]'))
        self.assertTrue(is_correct('(5+6)*(7*[8+5])'))
        self.assertTrue(is_correct(''))

    def test_false(self):
        self.assertFalse(is_correct('(]'))
        self.assertFalse(is_correct('пРифФкИи [) >3'))
        self.assertFalse(is_correct('({[)]'))
        self.assertFalse(is_correct('{а{ _ __ @{'))
        self.assertFalse(is_correct(')'))
        self.assertFalse(is_correct(']['))


if __name__ == '__main__':
    unittest.main()
