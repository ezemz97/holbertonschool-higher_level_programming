#!/usr/bin/python3
"""Student class"""


class Students:
    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Returns the dictionary representation
        of a student"""
        return self.__dict__
