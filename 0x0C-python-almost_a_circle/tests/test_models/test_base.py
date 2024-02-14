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


if __name__ == '__main__':
    unittest.main()
