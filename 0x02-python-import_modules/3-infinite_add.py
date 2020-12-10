#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argcount = len(argv)
    add = 0
    for x in range(1, argcount):
        add += int(argv[x])
    print("{:d}".format(add))