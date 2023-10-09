#!/usr/bin/python3
"""a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle"""
        s = "[Rectangle] "
        s += str(self.__width) + "/" + str(self.__height)
        return s
