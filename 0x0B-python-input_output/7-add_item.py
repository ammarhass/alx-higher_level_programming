#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

_list = []
if os.path.exists("add_item.json"):
    _list = load_from_json_file("add_item.json")

_list.extend(sys.argv[1:])
save_to_json_file(_list, "add_item.json")
