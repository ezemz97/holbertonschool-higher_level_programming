#!/usr/bin/python3
"""Single function module.

This function prints a name, followed by (optionally) a last name

"""


def say_my_name(first_name, last_name=""):
    """The function say_my_name() takes two strings,
    one for the name, and (optionally) one for the last name.
    And prints them in the standard output.

    Args:
        first_name (str): A name
        last_name (str): A last name

    Raises:
        TypeError: When either of the arguments are not strings (str)

    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
