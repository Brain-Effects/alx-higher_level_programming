#!/usr/bin/python3
"""
This module defines a Square class.

The purpose of this module is to provide a simple representation of a square.
"""


class Square:
    """
    This is the Square class.

    The purpose of this class is to define a square with a specific size and
    to calculate its area.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for the Square class.

        It initializes a Square instance with a given size.
        The size must be an integer and greater than or equal to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This is the getter method for the size attribute.

        It returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter method for the size attribute.

        It sets the size of the square to a given value.
        The value must be an integer and greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.

        The area of a square is calculated by squaring its size.
        """
        return self.__size ** 2
