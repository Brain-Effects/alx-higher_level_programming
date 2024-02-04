#!/usr/bin/python3
class Rectangle:
    """
    This class defines a rectangle.

    It has private instance attributes width and height, with properties and setters.
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
