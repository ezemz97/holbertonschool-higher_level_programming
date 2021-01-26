#!/usr/bin/python3
"""Module of the "Square" class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class.

    This is a subclass of the "Rectangle" class.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square generator.

        Creates a new Square instance by calling the parent class.
        Since all squares are rectangles, we just need one value for
        both width and height (so, we call it 'size' instead)

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the print() and str() representation of a square.

        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Retrieves the size of a square (getter).

        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size for a square (setter).

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of a square, from a dictionary.

        """
        attrs = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])

    def to_dictionary(self):
        """Returns the dictionary representation of a square.

        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
