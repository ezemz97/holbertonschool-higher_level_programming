#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    largo = len(argv) -1
    if largo == 0:
        print("{} arguments.".format(largo))
    elif largo == 1:
        print("{} argument:\n{}: {}".format(largo, 1, argv[1]))
    elif largo > 1:
        print("{} arguments:".format(largo))
        for x in range(1, largo + 1):
            print("{}: {}".format(x, argv[x]))