#!/usr/bin/python3
def matrix_divided(matrix, div):
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
