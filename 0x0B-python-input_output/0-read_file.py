#!/usr/bin/python3
"""Reads a text file and print content to stdout

Example:
    read_file("text_file.txt")
"""


def read_file(filename=""):
    """Opens a file as read only, utf-8 encoded,
    and prints the contents to stdout

    Args:
        filename (str): Text file name to open
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
