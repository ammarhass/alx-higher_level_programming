#!/usr/bin/python3
"""a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """Init method"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Rectangle"""
        s = "[Square] "
        s += str(self.__size) + "/" + str(self.__size)
        return s
