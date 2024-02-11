#!/usr/bin/python3
"""
This module contains the Rectangle class and its methods.

The Rectangle class represents a rectangle shape with width and
height attributes.
It has methods to calculate the area and perimeter of the rectangle.
"""


# Define a class Rectangle
class Rectangle:
    """
    This class represents a rectangle shape with width and height attributes.

    It has methods to calculate the area and perimeter of the rectangle.
    It also has a custom representation using the character #.
    It also has a string representation that can be used to create
    a new instance using eval().
    It also prints a farewell message when an instance is deleted.
    """

    # Define the constructor with optional width and height parameters
    def __init__(self, width=0, height=0):
        # Set the width and height using the property setters
        self.width = width
        self.height = height

    # Define the property getter for width
    @property
    def width(self):
        # Return the private instance attribute __width
        return self.__width

    # Define the property setter for width
    @width.setter
    def width(self, value):
        # Check if the value is an integer, otherwise raise a TypeError
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Check if the value is positive, otherwise raise a ValueError
        if value < 0:
            raise ValueError("width must be >= 0")
        # Set the private instance attribute __width to the value
        self.__width = value

    # Define the property getter for height
    @property
    def height(self):
        # Return the private instance attribute __height
        return self.__height

    # Define the property setter for height
    @height.setter
    def height(self, value):
        # Check if the value is an integer, otherwise raise a TypeError
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if the value is positive, otherwise raise a ValueError
        if value < 0:
            raise ValueError("height must be >= 0")
        # Set the private instance attribute __height to the value
        self.__height = value

    # Define the public instance method for area
    def area(self):
        # Return the product of width and height
        return self.width * self.height

    # Define the public instance method for perimeter
    def perimeter(self):
        # Check if width or height is equal to 0, otherwise return the sum of
        # twice width and height
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    # Define the custom representation for print() and str()
    def __str__(self):
        # Check if width or height is equal to 0, otherwise return a string of
        # characters
        if self.width == 0 or self.height == 0:
            return ""
        else:
            # Initialize an empty string
            string = ""
            # Loop through the rows of the rectangle
            for i in range(self.height):
                # Append a row of # characters
                string += "#" * self.width
                # Append a newline character, except for the last row
                if i < self.height - 1:
                    string += "\n"
            # Return the string
            return string

    # Define the string representation for repr()
    def __repr__(self):
        # Return a string that can be used to create a
        # new instance using eval()
        return "Rectangle({}, {})".format(self.width, self.height)

    # Define the method for deleting an instance
    def __del__(self):
        # Print a farewell message
        print("Bye rectangle...")
