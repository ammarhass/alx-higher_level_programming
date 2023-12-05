#!/usr/bin/python3
""" a student class """


class Student:
    """ define a Student class"""

    def __init__(self, first_name, last_name, age):
        """intialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
