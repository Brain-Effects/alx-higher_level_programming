#!/usr/bin/python3
"""
This module contains the Rectangle class and its methods.

The Rectangle class represents a rectangle shape with width and
height attributes.
It can be used for various purposes such as drawing,
calculating area and perimeter, etc.
"""
# Define a class Rectangle


class Rectangle:
    """
    This class defines a rectangle.

    It has private instance attributes width and height,
    with properties and setters.
    The width and height must be integers and greater than or equal to 0.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle with optional width and height.

        Parameters:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        """
        This script demonstrates the usage of the Rectangle class.

        It attempts to create Rectangle objects with invalid dimensions
        (negative width and height),and handles the exceptions that are raised.

        The script prints the type and message of any exceptions that occur,
        which helps in understanding the kind of errors that the
        Rectangle class is designed to raise when invalid dimensions are used.
        """

    try:
    # Attempt to create a Rectangle with width 2 and height -3.
    # Since the height is negative, this should raise a ValueError.
        myrectangle = Rectangle(2, -3)
    except Exception as e:
    # Print the type and message of the exception.
        print("[{}] {}".format(type(e).__name__, e))

    try:
    # Attempt to create a Rectangle with width -2 and height 3.
    # Since the width is negative, this should raise a ValueError.
        myrectangle = Rectangle(-2, 3)
    except Exception as e:
    # Print the type and message of the exception.
        print("[{}] {}".format(type(e).__name__, e))

    myrectangle = Rectangle(2, 4)
    print(myrectangle.width)  # prints: 2
    print(myrectangle.height)  # prints: 4
