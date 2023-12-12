#!/usr/bin/python3
"""define a unit test for base class"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class MyTestBase_id(unittest.TestCase):
    """unittest for Base class"""

    def test_one_id(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_two_id(self):
        a = Base(2)
        self.assertEqual(a.id, 2)

    def test_three_id(self):
        a = Base(1)
        b = Base(2)
        self.assertEqual(a.id, b.id - 1)

    def test_nb_objects(self):
        a = Base()
        a2 = Base(10)
        a3 = Base()
        self.assertEqual(a.id, a3.id - 1)

    def test_four_id(self):
        self.assertEqual(True, Base(True).id)

    def test_five_id(self):
        self.assertEqual("id", Base("id").id)


class MyTestBase_to_json_string(unittest.TestCase):
    """unittest for to_json_string method"""

    def test_one_to_json_string(self):
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([a.to_dictionary()])))

    def test_two_to_json_string(self):
        a = Square(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([a.to_dictionary()])))
    
    def test_three_to_json_string(self):
        self.assertEqual("[]", Base.to_json_string([]))


class MyTestBase_save_to_file(unittest.TestCase):
    """unittest for save_to_file method"""
    pass 
