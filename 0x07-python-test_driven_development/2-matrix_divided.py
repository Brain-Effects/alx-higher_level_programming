#!/usr/bin/python3
"""
This module contains a function that divides all elements of
a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given number.

    Parameters:
    matrix (list of lists): a matrix of integers or floats
    div (int or float): a non-zero number to divide the matrix elements by

    Returns:
    list of lists: a new matrix with the divided elements,
    rounded to 2 decimal places

    Raises:
    TypeError: if matrix is not a list of lists of integers or floats,
    or if div is not a number, or if the rows of the matrix
    are not of the same size
    ZeroDivisionError: if div is equal to 0
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not matrix
    or not all(isinstance(row, list) for row in matrix)
    or not
    all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (array of arrays) of\
                integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if the rows of the matrix are of the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Create a new matrix with the divided elements, rounded
    # to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
