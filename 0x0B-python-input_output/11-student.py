#!/usr/bin/python3
""" Student """


class Student():
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ Initializes a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation
        of a student"""
        if type(attrs) is not list:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for i in json:
            self.__dict__[i] = json[i]
        return self
