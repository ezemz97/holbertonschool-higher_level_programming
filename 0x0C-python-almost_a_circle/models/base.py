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

    @staticmethod
    def from_json_string(json_string):
        """Parse json string to python object"""
        if not json_string:
            return []
        return json.loads(json_string)


    @classmethod
    def save_to_file(cls, list_objs):

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
