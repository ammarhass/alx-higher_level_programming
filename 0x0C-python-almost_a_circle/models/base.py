#!/usr/bin/python3
"""Define a Base class"""
import json


class Base:
    """A Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that's writes the JSON string
            representaion of list_objs to a file"""
        file = cls.__name__ + ".json"
        with open(file, "w") as file_j:
            if list_objs is None:
                file_j.write("[]")
            else:
                List = [i.to_dictionary() for i in list_objs]
                file_j.write(Base.to_json_string(List))

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            c = cls(2, 3)
        else:
            c = cls(1)
        c.update(**dictionary)
        return c
