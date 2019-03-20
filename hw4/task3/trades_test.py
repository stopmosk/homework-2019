import unittest
from trades_logic import *

'''
class MyTestCase(unittest.TestCase):
    def test_max_qty_gap_ex(self):
        self.assertEqual(max_qty_gap_ex(''), 100)
        self.assertRaises(ValueError, max_qty_gap_ex, '')


    def test_max_qty_gap(self):
        self.assertEqual(max_qty_gap(''), [34, 12])
        self.assertRaises(ValueError, max_qty_gap, '')


    def test_database_read(self):
        self.assertEqual(database_read(), result)
        self.assertRaises(ValueError, database_read, '')

'''

if __name__ == '__main__':
    unittest.main()
