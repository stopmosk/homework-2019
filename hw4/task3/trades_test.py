import unittest
from trades_logic import *


class MyTestCase(unittest.TestCase):
    def test_max_qty_gap_ex(self):
        db = {'10:00:00': {'A': [10, 100.0]}, '10:00:01': {'A': [11, 100.0]}}
        res = ('10:00:01', 11, 100.0)
        self.assertEqual(max_qty_gap_ex(db, 'A'), res)
        db = {'10:00:00': {'A': [10, 100.0]}, '10:00:01': {'B': [11, 100.0]}}
        res = ('10:00:00', 10, 100.0)
        self.assertEqual(max_qty_gap_ex(db, 'A'), res)

    def test_max_qty_gap(self):
        db = {'10:00:00': {'A': [2, 200.0], 'D': [3, 300.0]},
              '10:00:01': {'D': [2, 200.0], 'B': [2, 200.0]}}
        res = ('10:00:00', 5, 500.0)
        self.assertEqual(max_qty_gap(db), res)

    def test_database_read(self):
        res_db = {'10:00:00': {'A': [2, 200.0], 'D': [3, 300.0]},
                  '10:00:01': {'D': [2, 200.0], 'B': [2, 200.0]}}
        res_ex = {'A', 'B', 'D'}
        self.assertEqual(database_read('trades_test.csv'), (res_db, res_ex))


if __name__ == '__main__':
    unittest.main()
