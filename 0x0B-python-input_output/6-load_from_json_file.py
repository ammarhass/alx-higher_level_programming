#!/usr/bin/python3
import json
"""defines a function"""


def load_from_json_file(filename):
    """function that creates an Object from a Json file """
    with open(filename) as file:
        return json.load(file)
