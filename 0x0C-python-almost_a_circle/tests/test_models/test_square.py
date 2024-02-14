#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    This is the TestSquare class.

    This class tests the Square class.
    """

    def setUp(self):
        self.s1 = Square(5, 2, 3, 99)

    def test_id(self):
        self.assertEqual(self.s1.id, 99)

    def test_size(self):
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)

    def test_x_y(self):
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 3)

    def test_str(self):
        self.assertEqual(str(self.s1), "[Square] (99) 2/3 - 5")

    def test_size(self):
        """
        This method tests the size getter and setter of the Square class.
        """

        s = Square(5)
        self.assertEqual(s.size, 5)

        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

        with self.assertRaises(TypeError):
            s.size = "10"
        with self.assertRaises(ValueError):
            s.size = -10


if __name__ == '__main__':
    unittest.main()
