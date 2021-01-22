from models.base import Base
class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
#
    @property
    def x(self):
        """Get the X value of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value X for a rectangle"""
        self.__x = value
#
    @property
    def y(self):
        """Get the Y value of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value Y for a rectangle"""
        self.__y = value
#
