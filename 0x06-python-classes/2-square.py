#!/usr/bin/python3
"""
This module defines a Square class.

The purpose of this module is to provide a simple representation of a square.
"""


class Square:
    """
    This is the Square class.

    The purpose of this class is to define a square with a specific size.
    """

    def __init__(self, size=0):
        """
        This is the constructor method for the Square class.

        It initializes a Square instance with a given size.
        The size must be an integer and greater than or equal to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
