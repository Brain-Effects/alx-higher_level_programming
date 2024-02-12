#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    This is the TestRectangle class.

    This class tests the Rectangle class.
    """
    
    """
    By resetting Base.__nb_objects in the setUp method,
    you ensure that each test starts with a clean state.
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        This method tests the id attribute of the Rectangle class.
        """

        # Test when id is not provided
        r1 = Rectangle(10, 15)
        self.assertEqual(r1.id, 1)

        # Test when id is provided
        r2 = Rectangle(10, 15, id=12)
        self.assertEqual(r2.id, 12)

        # Test when id is not provided again
        r3 = Rectangle(10, 15)
        self.assertEqual(r3.id, 2)

    def test_dimensions(self):
        """
        This method tests the width, height, x, and y
        attributes of the Rectangle class.
        """

        r = Rectangle(10, 15, 5, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

if __name__ == '__main__':
    unittest.main()
