#!/usr/bin/python3
"""
This module contains the Rectangle class and its methods.

The Rectangle class represents a rectangle shape and can be used for
various purposes such as drawing, calculating area and perimeter, etc.
"""


# Define a class Rectangle
class Rectangle:
    """
    This class represents a rectangle shape with width and height attributes.

    It has methods to calculate the area and perimeter of the rectangle.
    It also has a custom representation using the character(s)
    stored in print_symbol.
    It also has a string representation that can be used to
    create a new instance using eval().
    It also prints a farewell message when an instance is deleted.
    It also keeps track of the number of instances created and deleted.
    It also has a static method to compare two rectangles based on their area.
    It also has a class method to create a square rectangle.
    """

    # Define a public class attribute for the number of instances
    number_of_instances = 0

    # Define a public class attribute for the print symbol
    print_symbol = "#"

    # Define the constructor with optional width and height parameters
    def __init__(self, width=0, height=0):
        # Set the width and height using the property setters
        self.width = width
        self.height = height
        # Increment the number of instances by 1
        Rectangle.number_of_instances += 1

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
        # Check if width or height is equal to 0, otherwise return
        # the sum of twice width and height
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    # Define the custom representation for print() and str()
    def __str__(self):
        # Check if width or height is equal to 0, otherwise return
        # a string of print_symbol characters
        if self.width == 0 or self.height == 0:
            return ""
        else:
            # Initialize an empty string
            string = ""
            # Loop through the rows of the rectangle
            for i in range(self.height):
                # Append a row of print_symbol characters
                string += str(self.print_symbol) * self.width
                # Append a newline character, except for the last row
                if i < self.height - 1:
                    string += "\n"
            # Return the string
            return string

    # Define the string representation for repr()
    def __repr__(self):
        # Return a string that can be used to create
        # a new instance using eval()
        return "Rectangle({}, {})".format(self.width, self.height)

    # Define the method for deleting an instance
    def __del__(self):
        # Print a farewell message
        print("Bye rectangle...")
        # Decrement the number of instances by 1
        Rectangle.number_of_instances -= 1

    # Define the static method for comparing two rectangles
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # Check if rect_1 is an instance of Rectangle,
        # otherwise raise a TypeError
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        # Check if rect_2 is an instance of Rectangle,
        # otherwise raise a TypeError
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        # Compare the area of rect_1 and rect_2, and return
        # the bigger or equal one
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    # Define the class method for creating a square rectangle
    @classmethod
    def square(cls, size=0):
        # Return a new Rectangle instance with width and height equal to size
        return cls(size, size)
