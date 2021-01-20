#!/usr/bin/python3
"""Encodes a python object into a json"""


import json
def to_json_string(my_obj):
    """Returns the serialization of an object"""
    return json.dumps(my_obj)
