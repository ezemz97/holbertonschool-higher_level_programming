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
        new_dict = {}
        if type(attrs) is not list:
            return(self.__new_dictt__)
        else:
            for attribute in attrs:
                if attribute in self.__new_dictt__:
                    new_dict[attribute] = self.__new_dictt__[attribute]
            return(new_dict)

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for i in json:
            self.__dict__[i] = json[i]
        return self
