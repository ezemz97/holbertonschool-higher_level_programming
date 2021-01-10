#!/usr/bin/python3
"""Single function module:
This function prints a square, displayed with '#' characters

"""


def print_square(size):
    """Function to print a square with numeral characters

    Args:
        size (int): Size of the square (total quantity of '#' characters)

    Raises:
        TypeError: When 'size' is not an integer
        ValueError: When 'size' is negative

    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
