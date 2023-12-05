#!/usr/bin/python3
""" a student class """


class Student:
    """ define a Student class"""

    def __init__(self, first_name, last_name, age):
        """intialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation of an object"""
        if attrs is None:
            return self.__dict__
        _dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                _dict[key] = value
        return _dict
