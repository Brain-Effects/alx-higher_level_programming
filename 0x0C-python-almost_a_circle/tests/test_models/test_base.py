#!/user/bin/python3


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    This is the TestBase class.

    This class tests the Base class.
    """

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

if __name__ == '__main__':
    unittest.main()
