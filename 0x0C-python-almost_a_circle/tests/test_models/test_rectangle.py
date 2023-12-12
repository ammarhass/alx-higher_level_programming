#!/usr/bin/python3
"""define unittest for rectangle"""


import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """unittest for rectangle"""

    def test_one(self):
        self.assertInstance(Rectangle(2, 4), Base)

    def test_two(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
