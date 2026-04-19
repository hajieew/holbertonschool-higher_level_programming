#!/usr/bin/python3
"""Defines a class"""


class Rectangle:
    """Represent a rectangle class"""

    def __init__(self, width=0, height=0):
        """initalize the attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
