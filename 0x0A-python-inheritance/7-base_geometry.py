#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Basegeometry"""

    def area(self):
        """method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))