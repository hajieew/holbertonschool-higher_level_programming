#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """Represent a rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initalize the attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """represents the figure"""
        if self.__width == 0 or self.__height == 0:
            return ""
        siyah= []
        for i in range(self.height):
            siyah.append("#" * self.__width)
        return "\n".join(siyah)

    def __repr__(self):
        """convert object to string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes the object"""
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1
