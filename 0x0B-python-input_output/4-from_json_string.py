#!/usr/bin/python3
"""Decodes a json string into a python object"""
import json


def from_json_string(my_str):
    """Returns a python object from a json string"""
    return json.loads(my_str)
