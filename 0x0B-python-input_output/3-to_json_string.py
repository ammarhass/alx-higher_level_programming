#!/usr/bin/python3
"""define a function"""
import json


def to_json_string(my_obj):
    """function that return the JSON representation of an object"""
    return json.dumps(my_obj)
