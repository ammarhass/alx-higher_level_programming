#!/usr/bin/python3
"""

class BaseGeometry

"""


class BaseGeometry:
    """BaseGeometry class"""

    @classmethod
    def area(self):
        """function to get the area"""

        raise Exception("area() is not implemented")

    @classmethod
    def integer_validator(self, name, value):
        """function to check the validation of an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
