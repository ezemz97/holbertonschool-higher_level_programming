#!/usr/bin/python3
"""Single function module

This function divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """The function matrix_divided() function takes a matrix
    and a divisor number, it then divides each element of the matrix
    by said number (div), storing the new elements in a new matrix

    Args:
        matrix (list of lists): The matrix to be divided
        div (int, float): The divisor number

    Returns:
        A new matrix with the elements of the original divided by (div)

    Raises:
        ZeroDivisionError: When (div) is zero
        TypeError:
            - When (div) is not a number
            - When matrix is not a list of lists
            - When the elements of the matrix are not numbers
            - When the size of the rows are not the same

    """
    if type(div) not in {int, float}:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmatrix = []
    try:
        size = len(matrix[0])
    except TypeError:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if size == len(row):
            size = len(row)
        else:
            raise TypeError("Each row of the matrix must have the same size")
        newrow = []
        for number in row:
            if type(number) not in {int, float}:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            newrow.append(round(number / div, 2))
        newmatrix.append(newrow)
    return newmatrix
