#!/usr/bin/python3
"""Student class"""


class Students:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation
        of a student"""
        return self.__dict__
