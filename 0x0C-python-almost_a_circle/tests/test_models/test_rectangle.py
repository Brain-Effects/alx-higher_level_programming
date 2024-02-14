#!/usr/bin/python3

import unittest
import sys
from io import StringIO
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
        This method tests the width, height, x, and y attributes of
        the Rectangle class.
        """

        r = Rectangle(10, 15, 5, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 15)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)

    def test_validation(self):
        """
        This method tests the validation of the width, height, x,
        and y attributes of the Rectangle class.
        """

        with self.assertRaises(TypeError):
            r = Rectangle("10", 15)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 15)
        with self.assertRaises(TypeError):
            r = Rectangle(10, "15")
        with self.assertRaises(ValueError):
            r = Rectangle(10, -15)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 15, "5")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 15, -5)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 15, 5, "10")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 15, 5, -10)

    def test_area(self):
        """
        This method tests the area method of the Rectangle class.
        """

        r = Rectangle(10, 15)
        self.assertEqual(r.area(), 150)

    def test_display(self):
        """
        This method tests the display method of the Rectangle class.
        """

        r = Rectangle(4, 6, 2, 2)
        expected_output = "\n\n" + "  ####\n" * 6
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            output = out.getvalue()
            self.assertEqual(output, expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        """
        This method tests the __str__ method of the Rectangle class.
        """

        r = Rectangle(10, 15, 5, 10, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 5/10 - 10/15")

    def test_update(self):
        """
        This method tests the update method of the Rectangle class.
        """

        r = Rectangle(10, 15, 5, 10, 99)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(id=98, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 98)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        """
        This method tests the to_dictionary method of the Rectangle class.
        """

        r = Rectangle(10, 15, 5, 10, 99)
        expected_dict = {
            'id': 99,
            'width': 10,
            'height': 15,
            'x': 5,
            'y': 10
        }
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
