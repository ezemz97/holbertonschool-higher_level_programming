#!/usr/bin/python3
"""Defines a function to check if object is an instance of the class"""


def is_same_class(obj, a_class):
    """Checks if object is an instance of the class

    Args:
        obj: Object to check
        a_class: Class to check object to
    Return:
        True: if object is an instance of the class
        False: if it's not
    """
    return (type(object) == a_class)
