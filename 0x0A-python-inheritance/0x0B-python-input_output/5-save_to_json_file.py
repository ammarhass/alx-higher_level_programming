#1/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, "w") as file:
        return json.dump(my_obj, file) 
