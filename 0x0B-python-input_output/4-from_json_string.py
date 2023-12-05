#!/usr/bin/python3
"""define a function"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a json string"""
    return json.loads(my_str)
