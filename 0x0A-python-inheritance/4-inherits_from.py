#!/usr/bin/python3
"""function to check if object is instance
    from the inhertied specified class"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited,
     from the specified class ; otherwise False"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
