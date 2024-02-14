#!/usr/bin/python3
"""
This is the square module.

This module provides the Square class which inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class.

    This class inherits from the Rectangle class and represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the constructor method for the Square class.

        It calls the super class with id, x, y, width and height.
        The width and height are assigned to the value of size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method returns a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        This is the getter for size which is equal to width or
        height of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This is the setter for size. It assigns the value to
        both width and height.
        The value validation is the same as the Rectangle for width and height.
        """
        self.width = value
        self.height = value
