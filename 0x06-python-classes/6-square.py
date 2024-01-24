#!/usr/bin/python3
"""
This module defines a Square class.

The purpose of this module is to provide a simple representation of a square.
"""


class Square:
    """
    This is the Square class.

    The purpose of this class is to define a square with a specific size and
    position, calculate its area, and print its representation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This is the constructor method for the Square class.

        It initializes a Square instance with a given size and position.
        The size must be an integer and greater than or equal to 0.
        The position must be a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        This is the getter method for the position attribute.

        It returns the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This is the setter method for the position attribute.

        It sets the position of the square to a given value.
        The value must be a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not\
                all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        This method calculates and returns the area of the square.

        The area of a square is calculated by squaring its size.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the square with the character #.

        If the size of the square is 0, it prints an empty line.
        The position of the square is taken into account when printing.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
