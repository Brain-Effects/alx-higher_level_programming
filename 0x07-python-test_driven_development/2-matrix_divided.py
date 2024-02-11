#!/usr/bin/python3
"""
This module contains a function that divides all elements of
a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists of int or float): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists of int or float: The new matrix with the
        divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError("matrix must be a matrix (list of lists) of\
                    integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
                        integers/floats")

    # Check if each row of the matrix has the same size
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix
