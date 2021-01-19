#!/usr/bin/python3
"""Defines a class to check if object is instance of class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class

    Args:
        obj: Object to check
        a_class: Class to compare to object
    Returns:
        True: if is instance
        False: if it's not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
