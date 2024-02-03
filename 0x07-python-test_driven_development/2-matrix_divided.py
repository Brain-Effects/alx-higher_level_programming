#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by the divisor,
        rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       not \
       all(isinstance(item, (int, float)) for row in matrix for item in row):

        print("matrix must be a matrix (list of lists) of integers/floats")
        return

    if not all(len(row) == len(matrix[0]) for row in matrix):
        print("Each row of the matrix must have the same size")
        return

    if not isinstance(div, (int, float)):
        print("div must be a number")
        return

    if div == 0:
        print("division by zero")
        return

    return [[round(item / div, 2) for item in row] for row in matrix]


# Test cases
print(matrix_divided([[1, 2, 3], [4, 5, 6]], 2))
# Expected: [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
print(matrix_divided("invalid", 2))
# Expected: "matrix must be a matrix (list of lists) of integers/floats"
print(matrix_divided([[1, 2, 3], [4, 5]], 2))
# Expected: "Each row of the matrix must have the same size"
print(matrix_divided([[1, 2, 3], [4, 5, 6]], "invalid"))
# Expected: "div must be a number"
print(matrix_divided([[1, 2, 3], [4, 5, 6]], 0))
# Expected: "division by zero"
