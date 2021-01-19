#!/usr/bin/python3
"""Defines a class inherited from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Creates a new Rectangle object

        Args:
            width (int) = width of the rectangle
            height (int) = height of the rectangle
        """
        self.integer_validator("width", width):
            self.__width = width
        self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of a Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
