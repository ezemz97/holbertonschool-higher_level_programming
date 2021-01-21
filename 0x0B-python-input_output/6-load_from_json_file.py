#!/usr/bin/python3
"""Defines a function to create an object from a json"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
