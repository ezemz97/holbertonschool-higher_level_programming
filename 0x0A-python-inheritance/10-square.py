#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle"""

    def __init__(self, size):
        """Creates a new square
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
