import unittest
from caesar_logic import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_true(self):
        self.assertEqual(encrypt(-25, 'abcxyz ABCXYZ'), 'bcdyza BCDYZA')
        self.assertEqual(encrypt(-1, 'abcxyz ABCXYZ'), 'zabwxy ZABWXY')
        self.assertEqual(encrypt(0, 'abcxyz ABCXYZ'), 'abcxyz ABCXYZ')
        self.assertEqual(encrypt(1, 'abcxyz ABCXYZ'), 'bcdyza BCDYZA')
        self.assertEqual(encrypt(25, 'abcxyz ABCXYZ'), 'zabwxy ZABWXY')

        self.assertEqual(decrypt(-25, 'abcxyz ABCXYZ'), 'zabwxy ZABWXY')
        self.assertEqual(decrypt(-1, 'abcxyz ABCXYZ'), 'bcdyza BCDYZA')
        self.assertEqual(decrypt(0, 'abcxyz ABCXYZ'), 'abcxyz ABCXYZ')
        self.assertEqual(decrypt(1, 'abcxyz ABCXYZ'), 'zabwxy ZABWXY')
        self.assertEqual(decrypt(25, 'abcxyz ABCXYZ'), 'bcdyza BCDYZA')

        self.assertEqual(encrypt(-1, ' ,.!?лол'), ' ,.!?лол')
        self.assertEqual(encrypt(0, ' ,.!?лол'), ' ,.!?лол')
        self.assertEqual(encrypt(1, ' ,.!?лол'), ' ,.!?лол')

        self.assertEqual(decrypt(-1, ' ,.!?лол'), ' ,.!?лол')
        self.assertEqual(decrypt(0, ' ,.!?лол'), ' ,.!?лол')
        self.assertEqual(decrypt(1, ' ,.!?лол'), ' ,.!?лол')

    def test_type(self):
        self.assertRaises(TypeError, encrypt, 0.5, 'abc')
        self.assertRaises(TypeError, encrypt, 'abc', 1)
        self.assertRaises(TypeError, encrypt, 1, 1)

        self.assertRaises(TypeError, decrypt, 0.5, 'abc')
        self.assertRaises(TypeError, decrypt, 'abc', 1)
        self.assertRaises(TypeError, decrypt, 1, 1)



if __name__ == '__main__':
    unittest.main()
