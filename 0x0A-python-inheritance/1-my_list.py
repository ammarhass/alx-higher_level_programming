#!/usr/bin/python3

class MyList(list):
    """class that inherited from list class"""

    def print_sorted(self):
        """function to sort a list"""
        print(sorted(self))
