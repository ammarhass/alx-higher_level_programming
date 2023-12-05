#!/usr/bin/python3
"""defines a function"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a Json file """
    with open(filename) as file:
        return json.load(file)
