#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Class to test the class Rectangle
    """
    def test_id_subclass(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
    



if __name__ == "__main__":
    unittest.main()
