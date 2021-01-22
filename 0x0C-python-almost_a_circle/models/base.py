"""Module of the base class"""


class Base:
    """The base class, to manage id attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
