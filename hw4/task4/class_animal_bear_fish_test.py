import unittest
from class_animal_bear_fish import *


class MyTestCase(unittest.TestCase):

    def test_set_bounds(self):
        self.assertRaises(ValueError, Animal.set_bounds, -1, 5)
        self.assertRaises(ValueError, Animal.set_bounds, 5, -1)
        self.assertRaises(ValueError, Animal.set_bounds, -5, -1)
        self.assertRaises(ValueError, Animal.set_bounds, 5, 1)

        Animal.set_bounds(1, 10)
        self.assertTrue(Animal.min_pos == 1)
        self.assertTrue(Animal.max_pos == 10)
        # self.assertEqual(max_qty_gap_ex(db, 'A'), res)

    def test_animal_init(self):
        Animal.set_bounds(5, 20)
        self.assertRaises(ValueError, Animal, 4)
        self.assertRaises(ValueError, Animal, 20)

    def test_is_meet(self):
        Animal.set_bounds(5, 20)
        a1, a2 = Animal(18), Animal(16)
        self.assertRaises(ValueError, Animal.is_meet, a1, a2)

        a1, a2 = Animal(6), Animal(8)
        a1.direction, a2.direction = -1, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = -1, 0
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = -1, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 0, -1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 0, 0
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 0, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 1, -1
        self.assertEqual(Animal.is_meet(a1, a2), True)
        a1.direction, a2.direction = 1, 0
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 1, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)

        a1, a2 = Animal(8), Animal(9)
        a1.direction, a2.direction = -1, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = -1, 0
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = -1, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 0, -1
        self.assertEqual(Animal.is_meet(a1, a2), True)
        a1.direction, a2.direction = 0, 0
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 0, 1
        self.assertEqual(Animal.is_meet(a1, a2), False)
        a1.direction, a2.direction = 1, -1
        self.assertEqual(Animal.is_meet(a1, a2), True)
        a1.direction, a2.direction = 1, 0
        self.assertEqual(Animal.is_meet(a1, a2), True)
        a1.direction, a2.direction = 1, 1   # Не логично, но так задано
        self.assertEqual(Animal.is_meet(a1, a2), True)


if __name__ == '__main__':
    unittest.main()
