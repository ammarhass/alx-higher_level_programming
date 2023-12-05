#!/usr/bin/python3
"""define a function"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    listOflist = [[1]]
    while len(listOflist) != n:
        list1 = listOflist[-1]
        list2 = [1]
        for i in range(len(list1) - 1):
            list2.append(list1[i] + list1[i + 1])
        list2.append(1)
        listOflist.append(list2)
    return listOflist
