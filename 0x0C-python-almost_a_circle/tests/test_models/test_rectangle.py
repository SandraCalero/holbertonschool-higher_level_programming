#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import io
import unittest.mock
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Class to test the class Rectangle
    """

    def setUp(self):
        """Creates the instance that can be used in the following tests"""
        self.r1 = Rectangle(10, 2, 0, 0, 12)

    def test_isinstance(self):
        """Test if is an instance of class Rectangle"""
        self.assertIsInstance(self.r1, Rectangle)

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

    def test_TypeErrorMessage_height(self):
        """Test error and message raised by providing an invalid type height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_TypeErrorMessage_x(self):
        """Test error and message raised by providing an invalid type x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, [1])

    def test_TypeError_y(self):
        """Test error raised by providing an invalid type y"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 3.56)

    def test_ValueErrorMessage_width(self):
        """Test error and message raised by providing a negative width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 10)

    def test_ValueError_height(self):
        """Test error raised by providing a negative height"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_ValueError_x(self):
        """Test error raised by providing a negative type x"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_ValueErrorMessage_y(self):
        """Test error and message raised by providing a negative type y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -3)

    def test_area(self):
        """Test the area"""
        r2 = Rectangle(6, 5, 8, 25)
        self.assertEqual(r2.area(), 30)

    def test_display_not_None(self):
        """Test if rectangle is not None"""
        r3 = Rectangle(2, 5)
        self.assertIsNotNone(r3.display)

    def test_display(self):
        """Test print in stdout the Rectangle instance with the character #"""
        output = "##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r4 = Rectangle(2, 1)
            r4.display()
            self.assertEqual(_out.getvalue(), output)

    def test_str_method(self):
        """Test __str__ method in stdout"""
        output = "[Rectangle] (12) 2/1 - 4/6\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(Rectangle(4, 6, 2, 1, 12))
            self.assertEqual(_out.getvalue(), output)

    def test_displayXY(self):
        """Test print in stdout the Rectangle instance
        with the character # by taking care of x and y"""
        output = "\n\n  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r5 = Rectangle(2, 3, 2, 2)
            r5.display()
            self.assertEqual(_out.getvalue(), output)

    def test_update(self):
        """Test assigns a key/value argument to attributes"""
        output = "[Rectangle] (89) 10/10 - 10/10\n"
        r6 = Rectangle(10, 10, 10, 10)
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            r6.update(89)
            print(r6)
            self.assertEqual(_out.getvalue(), output)

    def test_to_dictionary(self):
        """Test return of the dictionary representation of a Rectangle"""
        r7 = Rectangle(10, 2, 1, 9, 15)
        self.assertEqual(r7.to_dictionary(), {
                         'id': 15, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_to_json_string(self):
        r8 = Rectangle(10, 7, 2, 8, 1)
        dictio = r8.to_dictionary()
        self.assertEqual(Base.to_json_string(
            [dictio]), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')


if __name__ == "__main__":
    unittest.main()
