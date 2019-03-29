import unittest
from class_river import *


class MyTestCase(unittest.TestCase):
    def test_river_init(self):
        self.assertRaises(ValueError, River, -1)
        self.assertRaises(ValueError, River, 0)

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

    def test_place_new_object(self):
        my_river = River(5)

        my_river.storage = [None, 66, None, None, 77]
        self.assertRaises(ValueError, my_river.place_new_object, 'SS', -1)
        self.assertRaises(ValueError, my_river.place_new_object, 'SS', 5)
        self.assertRaises(RuntimeError, my_river.place_new_object, None, 0)
        self.assertRaises(RuntimeError, my_river.place_new_object, 'SS', 1)
        self.assertRaises(RuntimeError, my_river.place_new_object, 'SS', 4)

        my_river.place_new_object('SS', 2)
        self.assertTrue(my_river.storage[2] == 'SS')
        my_river.place_new_object('TT', 0)
        self.assertTrue(my_river.storage[0] == 'TT')

    def test_move_object(self):
        my_river = River(5)

        my_river.storage = [None, 66, None, None, 77]
        self.assertRaises(ValueError, my_river.move_object, 1, -1)
        self.assertRaises(ValueError, my_river.move_object, 1, 5)
        self.assertRaises(RuntimeError, my_river.move_object, 0, 2)
        self.assertRaises(RuntimeError, my_river.move_object, 2, 2)
        self.assertRaises(RuntimeError, my_river.move_object, 1, 4)
        self.assertRaises(RuntimeError, my_river.move_object, 4, 1)
        self.assertRaises(RuntimeError, my_river.move_object, 3, 1)

        my_river.move_object(1, 2)
        self.assertTrue(my_river.storage[1] is None)
        self.assertTrue(my_river.storage[2] == 66)
        my_river.move_object(2, 3)
        self.assertTrue(my_river.storage[2] is None)
        self.assertTrue(my_river.storage[3] == 66)
        my_river.move_object(4, 2)
        self.assertTrue(my_river.storage[4] is None)
        self.assertTrue(my_river.storage[2] == 77)

    def test_release_cell(self):
        my_river = River(5)

        my_river.storage = [None, 66, None, None, 77]
        self.assertRaises(ValueError, my_river.release_cell, -1)
        self.assertRaises(ValueError, my_river.release_cell, 5)
        self.assertRaises(RuntimeError, my_river.release_cell, 2)

        my_river.release_cell(1)
        self.assertTrue(my_river.storage[1] is None)
        my_river.release_cell(4)
        self.assertTrue(my_river.storage[4] is None)


if __name__ == '__main__':
    unittest.main()
