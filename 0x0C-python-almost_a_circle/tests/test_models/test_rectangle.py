#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class to test the class Rectangle
    """
    def setUp(self):
        """Creates the instance that can be used in the following tests"""
        self.r1 = Rectangle(10, 2, 0, 0, 12)

    def test_id(self):
        """Test id of Rectangle r1"""
        self.assertEqual(self.r1.id, 12)

    def test_width(self):
        """Test width of Rectangle r1"""
        self.assertEqual(self.r1.width, 10)

    def test_height(self):
        """Test height of Rectangle r1"""
        self.assertEqual(self.r1.height, 2)

    def test_x(self):
        """Test x of Rectangle r1"""
        self.assertEqual(self.r1.x, 0)

    def test_y(self):
        """Test y of Rectangle r1"""
        self.assertEqual(self.r1.y, 0)

    def test_TypeError_width(self):
        """Test error raised by providing an invalid type width"""
        with self.assertRaises(TypeError):
            Rectangle("2", 10)

    def test_TypeError_height(self):
        """Test error raised by providing an invalid type height"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2.5)

    def test_TypeError_x(self):
        """Test error raised by providing an invalid type x"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, [1])

    def test_TypeError_y(self):
        """Test error raised by providing an invalid type y"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 3.56)

    def test_ValueError_width(self):
        """Test error raised by providing a negative width"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 10)

    def test_ValueError_height(self):
        """Test error raised by providing a negative height"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_ValueError_x(self):
        """Test error raised by providing a negative type x"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_ValueError_y(self):
        """Test error raised by providing a negative type y"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -3)


if __name__ == "__main__":
    unittest.main()
