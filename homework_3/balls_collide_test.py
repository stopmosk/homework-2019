import unittest
from balls_collide import balls_collide


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(balls_collide((0, 0, 2), (2, 2, 2)))
        self.assertTrue(balls_collide((1.0, 1.0, 10), (1.0, 1.0, 1)))
        self.assertTrue(balls_collide((0, 0, 10), (10, 0, 0)))
        self.assertTrue(balls_collide((-5, -5, 10), (-10, -10, 10)))
        self.assertTrue(balls_collide((1.5, -1.5, 1.5), (-2.5, -2.5, 5.5)))

    def test_false(self):
        self.assertFalse(balls_collide((0, 0, 1), (2, 2, 1)))
        self.assertFalse(balls_collide((0, 0, 0), (10, 0, 0)))
        self.assertFalse(balls_collide((-5, -5, 2), (-10, -10, 2)))
        self.assertFalse(balls_collide((10.5, -10.5, 1.5), (-2.5, -2.5, 5.5)))

    def test_type(self):
        self.assertRaises(TypeError, balls_collide, {0, 0, 1}, {2, 2, 1})
        self.assertRaises(TypeError, balls_collide, (0, 0, 1), {2, 2, 1})
        self.assertRaises(TypeError, balls_collide, [0, 0, 1], {2, 2, 1})
        self.assertRaises(TypeError, balls_collide, (0, 0, 1), 0)
        self.assertRaises(TypeError, balls_collide, 'O', (2, 2, 1))

    def test_len(self):
        self.assertRaises(TypeError, balls_collide, (0, 0), (2, 2, 1))
        self.assertRaises(TypeError, balls_collide, (0, 0, 1), (2, 2))
        self.assertRaises(TypeError, balls_collide, (0, 0, 1, 3), (2, 2, 1))
        self.assertRaises(TypeError, balls_collide, (0, 0, 1), (2, 2, 1, 4))

    def test_type_ball_arg(self):
        self.assertRaises(TypeError, balls_collide, (0, 0, 's'), (2, 2, 1))
        self.assertRaises(TypeError, balls_collide, (0, 0, 5), (2, 'for', 1))
        self.assertRaises(TypeError, balls_collide, (0, [0], 5), (2, 2, 1))
        self.assertRaises(TypeError, balls_collide, (0, 0, 5), (2, 2, '1'))

    def test_radius(self):
        self.assertRaises(ValueError, balls_collide, (0, 0, -1), (2, 2, 4))
        self.assertRaises(ValueError, balls_collide, (0, 0, 1), (2, 2, -2))
        self.assertRaises(ValueError, balls_collide, (0, 0, -4), (2, 2, -1))
        self.assertRaises(ValueError, balls_collide, (0, 0, -4.0), (2, 2, -1.0))


if __name__ == '__main__':
    unittest.main()
