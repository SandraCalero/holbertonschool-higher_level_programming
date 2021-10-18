#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to test the class Base
    """
    def test_id_None(self):
        """Test if id is None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_positive(self):
        """Test a positive number as id"""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_id_negative(self):
        """Test a negative number as id"""
        b4 = Base(-6)
        self.assertEqual(b4.id, -6)


if __name__ == "__main__":
    unittest.main()
