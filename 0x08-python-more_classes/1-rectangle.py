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
    This class represents a rectangle shape with width and height attributes.
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
