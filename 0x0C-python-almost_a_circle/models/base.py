#!/usr/bin/python3
"""Module of the "Base" class."""
import json


class Base:
    """The base of all other classes in this project.

    Used to manage id attributes and number of instances.

    Attributes:
        __nb_objects (int): The total ammount of instances created.
        print_symbol (str): Symbol used to (and by) display a rectangle/square.

    """
    __nb_objects = 0
    # ╬
    print_symbol = "#"

    def __init__(self, id=None):
        """Base constructor for instances.

        Initializes a new instance and sets the id based
        on the number of instances (if id is not supplied)

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Parses a list of python dictionaries to a json string.

        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Parses a json string to a python object.

        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of instances to a .json file.

        Writes the json string representation of every
        object in 'list_objs', to a 'Classname.json' file.

        """
        name = cls.__name__ + ".json"
        with open(name, "w") as file:
            tojson = []
            if list_objs is None:
                file.write(tojson)
                return
            for element in list_objs:
                element = cls.to_dictionary(element)
                tojson.append(element)
            file.write(Base.to_json_string(tojson))

    @classmethod  # this is important
    def create(cls, **dictionary):
        """Creates a new instance with all attributes already set.

        """
        dummy = cls(1, 1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of new instances from a .json file.

        """
        lyst = []
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as file:
                lyst = cls.from_json_string(file.read())
        except FileNotFoundError:
            return lyst
        for element in range(len(lyst)):
            lyst[element] = cls.create(**lyst[element])
        return lyst
