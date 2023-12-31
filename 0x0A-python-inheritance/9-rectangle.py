#!/usr/bin/python3
""" class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """intializa a Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


    def area(self):
        """get the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """represent a Rectangle"""
        
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
