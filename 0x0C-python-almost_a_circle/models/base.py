"""Module of the base class"""
import json
#╬


class Base:
    """The base class, to manage id attributes"""

    __nb_objects = 0
    print_symbol = "#"

    def __init__(self, id=None):
        """Base constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs.write("[]")
        name = cls.__name__ + ".json"
        str = cls.to_json_string(list_objs)

        with open(name, "w+") as file:
            return file.write(str)
