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

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.

        The argument order is super important for args:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute

        Each key in kwargs represents an attribute to the instance.
        kwargs must be skipped if args exists and is not empty.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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
