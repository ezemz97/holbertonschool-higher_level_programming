#!/usr/bin/python3
"""Defines a function to check an object class"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class
    (but not the class itself), or False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
