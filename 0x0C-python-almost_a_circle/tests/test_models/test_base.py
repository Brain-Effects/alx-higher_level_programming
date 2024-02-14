#!/user/bin/python3


import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This is the TestBase class.

    This class tests the Base class.
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        This method tests the id attribute of the Base class.
        """

        # Test when id is not provided
        b1 = Base()
        self.assertEqual(b1.id, 1)

        # Test when id is provided
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

        # Test when id is not provided again
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """
        This method tests the to_json_string method of the Base class.
        """

        list_dictionaries = [{'id': 12}, {'id': 34}]
        self.assertEqual(Base.to_json_string(
            list_dictionaries), '[{"id": 12}, {"id": 34}]')

        list_dictionaries = []
        self.assertEqual(Base.to_json_string(list_dictionaries), '[]')

        list_dictionaries = None
        self.assertEqual(Base.to_json_string(list_dictionaries), '[]')

    def test_save_to_file(self):
        """
        This method tests the save_to_file method of the Base class.
        """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_objs = [r1, r2]
        Rectangle.save_to_file(list_objs)

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = ('[{"id": 1, "width": 10, "height": 7, "x": 2, \
                    "y": 8},' ' {"id": 2, "width": 2, "height": 4, "x": 0,\
                    "y": 0}]')

        list_objs = None
        Rectangle.save_to_file(list_objs)

        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_from_json_string(self):
        """
        This method tests the from_json_string method of the Base class.
        """

        json_string = '[{"id": 12}, {"id": 34}]'
        self.assertEqual(Base.from_json_string(
            json_string), [{'id': 12}, {'id': 34}])

        json_string = None
        self.assertEqual(Base.from_json_string(json_string), [])

        json_string = ""
        self.assertEqual(Base.from_json_string(json_string), [])


if __name__ == '__main__':
    unittest.main()
