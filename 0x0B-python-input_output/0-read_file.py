#!/usr/bin/python3
"""define a function"""


def read_file(filename=""):
    "function that reads a text file"
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
