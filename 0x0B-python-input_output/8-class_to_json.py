#!/usr/bin/python3
"""Function to return the attributes of an object"""


def class_to_json(obj):
    """Returns the attributes of the object"""
    return obj.__dict__
