#!/usr/bin/python3
"""
This is the rectangle module.

This module provides the Rectangle class which inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    This is the Rectangle class.

    This class inherits from the Base class and represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the constructor method for the Rectangle class.

        It calls the super class with id and assigns each argument width,
        height, x and y to the right attribute.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        This method returns the area value of the Rectangle instance.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        This method prints in stdout the Rectangle instance with
        the character #, taking into account the x and y attributes.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        This method returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.

        The argument order is super important:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        Each key in kwargs represents an attribute to the instance.
        kwargs must be skipped if args exists and is not empty.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
