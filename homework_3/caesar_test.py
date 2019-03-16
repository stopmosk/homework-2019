import unittest
from caesar_logic import encrypt, decrypt


class MyTestCase(unittest.TestCase):
    def test_equal(self):
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


if __name__ == '__main__':
    unittest.main()
