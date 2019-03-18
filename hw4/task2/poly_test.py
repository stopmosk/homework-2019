import unittest
from poly_logic import *


class MyTestCase(unittest.TestCase):
    def test_str_to_int(self):
        self.assertEqual(str_to_int('100'), 100)
        self.assertEqual(str_to_int('+100'), 100)
        self.assertEqual(str_to_int('-100'), -100)
        self.assertEqual(str_to_int('1'), 1)
        self.assertEqual(str_to_int('+1'), 1)
        self.assertEqual(str_to_int('-1'), -1)
        self.assertEqual(str_to_int('0'), 0)
        self.assertEqual(str_to_int('+0'), 0)
        self.assertEqual(str_to_int('-0'), 0)
        self.assertEqual(str_to_int('001'), 1)
        self.assertEqual(str_to_int('-001'), -1)
        self.assertEqual(str_to_int('+001'), 1)
        self.assertRaises(ValueError, str_to_int, '')
        self.assertRaises(ValueError, str_to_int, '+')
        self.assertRaises(ValueError, str_to_int, '-')
        self.assertRaises(ValueError, str_to_int, '1.1')
        self.assertRaises(ValueError, str_to_int, '-1.1')
        self.assertRaises(ValueError, str_to_int, 'x')

    def test_str_to_part(self):
        self.assertEqual(str_to_part('12x^34'), [34, 12])
        self.assertEqual(str_to_part('+12x^34'), [34, 12])
        self.assertEqual(str_to_part('-12x^34'), [34, -12])
        self.assertEqual(str_to_part('1x^34'), [34, 1])
        self.assertEqual(str_to_part('+1x^34'), [34, 1])
        self.assertEqual(str_to_part('-1x^34'), [34, -1])
        self.assertEqual(str_to_part('12x^1'), [1, 12])
        self.assertEqual(str_to_part('+12x^1'), [1, 12])
        self.assertEqual(str_to_part('-12x^1'), [1, -12])
        self.assertEqual(str_to_part('x^34'), [34, 1])
        self.assertEqual(str_to_part('+x^34'), [34, 1])
        self.assertEqual(str_to_part('-x^34'), [34, -1])
        self.assertEqual(str_to_part('12x'), [1, 12])
        self.assertEqual(str_to_part('+12x'), [1, +12])
        self.assertEqual(str_to_part('-12x'), [1, -12])
        self.assertEqual(str_to_part('x'), [1, 1])
        self.assertEqual(str_to_part('+x'), [1, 1])
        self.assertEqual(str_to_part('-x'), [1, -1])
        self.assertEqual(str_to_part('2'), [0, 2])
        self.assertEqual(str_to_part('+2'), [0, 2])
        self.assertEqual(str_to_part('-2'), [0, -2])
        self.assertEqual(str_to_part('0'), [0, 0])
        self.assertEqual(str_to_part('+0'), [0, 0])
        self.assertEqual(str_to_part('-0'), [0, 0])
        self.assertRaises(ValueError, str_to_part, '')
        self.assertRaises(ValueError, str_to_part, '+')
        self.assertRaises(ValueError, str_to_part, '-')
        self.assertRaises(ValueError, str_to_part, '')
        self.assertRaises(ValueError, str_to_part, '')
        self.assertRaises(ValueError, str_to_part, '')

    def test_derivative_poly_s(self):
        poly = 'x^2 + x + 1'
        result = '2x+1'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = 'x^2'
        result = '2x'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = 'x + 1'
        result = '1'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '1x^0'
        result = '0'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '-x^2 + x - 1'
        result = '-2x+1'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '15x^4'
        result = '60x^3'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '15x^4 - 8x^2 + 5 - 10 + 7x'
        result = '60x^3-16x+7'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '-1x + 8x + 10x - 10x - 8x + 5 + 18 - 18 - 5'
        result = '-1'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '-2x^2-2x-3'
        result = '-4x-2'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = 'x^2'
        result = '2x'
        self.assertEqual(derivative_poly_s(poly), result)
        poly = '-2x^3'
        result = '-6x^2'
        self.assertEqual(derivative_poly_s(poly), result)


if __name__ == '__main__':
    unittest.main()
