#!/usr/bin/python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
newmatrix = []
for x in matrix:
	newmatrix.append([y**2 for y in x])
print (newmatrix)
