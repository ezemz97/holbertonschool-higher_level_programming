"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the print() and str() representation of a rectangle"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the width of the rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of width and height for the rectangle."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates a square attributes"""
        attrs = ["id", "size", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

