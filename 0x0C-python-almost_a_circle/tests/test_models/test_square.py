#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
import io
import unittest.mock
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Class to test the class Square
    """

    def setUp(self):
        """Creates the instance that can be used in the following tests"""
        self.s1 = Square(10, 0, 0, 12)

    def test_isinstance(self):
        """Test if is an instance of class Square"""
        self.assertIsInstance(self.s1, Square)

    def test_id(self):
        """Test id of Square s1"""
        self.assertEqual(self.s1.id, 12)

    def test_size(self):
        """Test size of Square s1"""
        self.assertEqual(self.s1.size, 10)

    def test_x(self):
        """Test x of Square s1"""
        self.assertEqual(self.s1.x, 0)

    def test_y(self):
        """Test y of Square s1"""
        self.assertEqual(self.s1.y, 0)

    def test_TypeError_size(self):
        """Test error raised by providing an invalid type size"""
        with self.assertRaises(TypeError):
            Square("2")

    def test_TypeErrorMessage_size(self):
        """Test error and message raised by providing an invalid type width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)

    def test_TypeErrorMessage_x(self):
        """Test error and message raised by providing an invalid type x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [1])

    def test_TypeError_y(self):
        """Test error raised by providing an invalid type y"""
        with self.assertRaises(TypeError):
            Square(10, 1, 3.56)

    def test_ValueErrorMessage_size(self):
        """Test error and message raised by providing a negative size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)

    def test_ValueError_size(self):
        """Test error raised by providing a negative size"""
        with self.assertRaises(ValueError):
            Square(-12)

    def test_ValueError_x(self):
        """Test error raised by providing a negative type x"""
        with self.assertRaises(ValueError):
            Square(10, -1)

    def test_ValueErrorMessage_y(self):
        """Test error and message raised by providing a negative type y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 1, -3)

    def test_area(self):
        """Test the area"""
        s2 = Square(6, 5, 8)
        self.assertEqual(s2.area(), 36)

    def test_display_not_None(self):
        """Test if rectangle is not None"""
        s3 = Square(2, 5)
        self.assertIsNotNone(s3.display)

    def test_display(self):
        """Test print in stdout the Square instance with the character #"""
        output = "#\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            s4 = Square(1)
            s4.display()
            self.assertEqual(_out.getvalue(), output)

    def test_str_method(self):
        """Test __str__ method in stdout"""
        output = "[Square] (12) 2/1 - 4\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(Square(4, 2, 1, 12))
            self.assertEqual(_out.getvalue(), output)

    def test_displayXY(self):
        """Test print in stdout the Square instance
        with the character # by taking care of x and y"""
        output = "\n\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            s5 = Square(2, 2, 2)
            s5.display()
            self.assertEqual(_out.getvalue(), output)

    def test_update(self):
        """Test assigns a key/value argument to attributes"""
        output = "[Square] (10) 0/0 - 5\n"
        s6 = Square(5)
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            s6.update(10)
            print(s6)
            self.assertEqual(_out.getvalue(), output)

    def test_to_dictionary(self):
        """Test return of the dictionary representation of a Square"""
        s7 = Square(10, 2, 1, 1)
        self.assertEqual(s7.to_dictionary(), {
                         'id': 1, 'size': 10, 'x': 2, 'y': 1})

    def test_to_json_string(self):
        """Test return of a JSON string representation of list_dictionaries"""
        s8 = Square(10, 7, 8, 1)
        dictionary = s8.to_dictionary()
        self.assertEqual(Base.to_json_string(
            [dictionary]), '[{"id": 1, "size": 10, "x": 7, "y": 8}]')

    def test_save_to_file(self):
        """Test write the JSON string representation of list_objs to a file"""
        s9 = Square(10, 2, 8, 2)
        output_expected = '[{"id": 2, "size": 10, "x": 2, "y": 8}]'
        Square.save_to_file([s9])
        with open("Square.json", "r") as file:
            output = file.read()
        self.assertEqual(output, output_expected)


if __name__ == "__main__":
    unittest.main()
