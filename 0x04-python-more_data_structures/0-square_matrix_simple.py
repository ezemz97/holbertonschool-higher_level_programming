#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for x in matrix:
        newmatrix.append([y**2 for y in x])
    return (newmatrix)
