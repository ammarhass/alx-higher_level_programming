#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """ print the list in an ascending order"""

    def print_sorted(self):
        print(sorted(self))
