#!/usr/bin/python3
import json
"""define a function"""


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
