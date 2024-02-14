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

    def test_update(self):
        """
        This method tests the update method of the Square class.
        """

        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        s.update(size=6, y=7, x=8, id=9)
        self.assertEqual(s.id, 9)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        """
        This method tests the to_dictionary method of the Square class.
        """

        s = Square(5, 2, 3, 99)
        expected_dict = {
            'id': 99,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
