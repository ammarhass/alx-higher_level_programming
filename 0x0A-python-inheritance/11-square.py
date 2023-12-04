#!/usr/bin/python3
"""import Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialize a square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """get the area"""
        return self.__size * self.__size

    def __str__(self):
        """print info about the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
