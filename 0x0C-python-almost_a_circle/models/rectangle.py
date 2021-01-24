#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
#

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width for the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
#

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a height for the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value
#

    @property
    def x(self):
        """Get the X value of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value X for a rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
#

    @property
    def y(self):
        """Get the Y value of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value Y for a rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
#

    def area(self):
        """Gets the area of a rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """Prints a rectangle with numeral characters."""
        if ((self.__width == 0) or (self.__height == 0)):
            return ""

        sqrstr = ""
        if self.__y > 0:
            for y in range(self.__y):
                sqrstr += "\n"

        for h in range(self.__height):
            for x in range(self.__x):
                    sqrstr += " "
            for w in range(self.__width):
                sqrstr += str(super().print_symbol)
            if h != self.__height - 1:
                sqrstr += "\n"
        print(sqrstr)

    def __str__(self):
        """Returns the print() and str() representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates a rectangle attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
