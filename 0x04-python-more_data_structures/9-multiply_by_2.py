#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = a_dictionary.copy()
    l_key = list(s.keys())

    for i in l_key:
        s[i] *= 2

    return (s)
