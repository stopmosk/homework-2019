import unittest
from class_river import *


class MyTestCase(unittest.TestCase):
    def test_river_init(self):
        self.assertRaises(ValueError, River, -1)
        self.assertRaises(ValueError, River, 0)
        # self.assertEqual(max_qty_gap_ex(db, 'A'), res)
        # self.assertEqual(max_qty_gap_ex(db, 'A'), res)

    def test_get_next_object(self):
        my_river = River(5)

        my_river.storage = [None, 66, None, None, 77]
        self.assertRaises(ValueError, my_river.get_next_object, -1)
        self.assertEqual(my_river.get_next_object(0), (66, 1))
        self.assertEqual(my_river.get_next_object(1), (66, 1))
        self.assertEqual(my_river.get_next_object(2), (77, 4))
        self.assertEqual(my_river.get_next_object(3), (77, 4))
        self.assertEqual(my_river.get_next_object(4), (77, 4))
        self.assertEqual(my_river.get_next_object(5), (None, -1))
        self.assertEqual(my_river.get_next_object(6), (None, -1))

        my_river.storage = [None, 66, None, 77, None]
        self.assertEqual(my_river.get_next_object(3), (77, 3))
        self.assertEqual(my_river.get_next_object(4), (None, -1))
        self.assertEqual(my_river.get_next_object(5), (None, -1))
        self.assertEqual(my_river.get_next_object(6), (None, -1))

if __name__ == '__main__':
    unittest.main()
