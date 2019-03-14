from unittest import TestCase, main


def is_perfect(num):
    if type(num) != int: raise TypeError('Введено не целое число')
    if num <= 0: raise ValueError('Введено не положительное число')
    if num < 6: return False
    sum_divs = 0
    for div in range(1, num // 2 + 1):
        if num % div == 0:
            sum_divs += div
    return num == sum_divs


# print(is_perfect(496))


class TestPerfect(TestCase):
    def test_true(self):
        self.assertTrue(is_perfect(6))
        self.assertTrue(is_perfect(28))
        self.assertTrue(is_perfect(496))
        self.assertTrue(is_perfect(8128))
    def test_false(self):
        self.assertFalse(is_perfect(8))
        self.assertFalse(is_perfect(1))
        self.assertFalse(is_perfect(34554))
        self.assertFalse(is_perfect(14))
    def test_error_st(self):
        self.assertRaises(TypeError, is_perfect, 'О')
        self.assertRaises(TypeError, is_perfect, '')
        self.assertRaises(TypeError, is_perfect, '+')
        self.assertRaises(TypeError, is_perfect, '100.500')
    def test_error_ne(self):
        self.assertRaises(ValueError, is_perfect, -10)
        self.assertRaises(ValueError, is_perfect, -6)
        self.assertRaises(ValueError, is_perfect, -496)
        self.assertRaises(ValueError, is_perfect, 0)

main()

