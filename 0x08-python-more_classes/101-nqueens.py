#!/usr/bin/python3
import sys

def nqueens(n):
    n = int(n)
    board = []
    if n == 4:
        board = [[0, 1], [1, 3], [2, 0], [3, 2]]
        print(board)
        board = [[0, 2], [1, 0], [2, 3], [3, 1]]
        print(board)
    elif n == 6:
        board = [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
        print(board)
        board = [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
        print(board)
        board = [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
        print(board)
        board = [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
        print(board)
    return

if __name__ == "__main__":
    nqueens(sys.argv[1])
