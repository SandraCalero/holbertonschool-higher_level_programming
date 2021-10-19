#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import io
import unittest.mock
import pycodestyle
import os
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
        self.assertIsInstance(r7.to_dictionary(), dict)

    def test_to_json_string(self):
        """Test return of a JSON string representation of list_dictionaries"""
        r8 = Rectangle(10, 7, 2, 8, 1)
        dictio = r8.to_dictionary()
        self.assertEqual(Base.to_json_string(
            [dictio]), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertIsInstance(dictio, dict)
        self.assertIsInstance(Base.to_json_string([dictio]), str)

    def test_save_to_file(self):
        """Test write the JSON string representation of list_objs to a file"""
        json_content = '[{"id": 2, "width": 10, "height": 7, "x": 2, "y": 8}]'
        filename_expected = "Rectangle.json"
        r9 = Rectangle(10, 7, 2, 8, 2)
        Rectangle.save_to_file([r9])
        path = os.getcwd()
        self.assertTrue(os.path.isfile(path + "/" + filename_expected))
        with open("Rectangle.json", "r") as file:
            output = file.read()
        self.assertEqual(output, json_content)
        self.assertEqual(file.name, filename_expected)
        self.assertIsInstance(r9, Rectangle)
        self.assertIsInstance(output, str)
        os.remove(path + "/" + filename_expected)

    def test_save_to_file_None(self):
        """Test save_to_file methot if list_objs is None"""
        json_content = '[]'
        filename_expected = "Rectangle.json"
        Rectangle.save_to_file(None)
        path = os.getcwd()
        self.assertTrue(os.path.isfile(path + "/" + filename_expected))
        with open("Rectangle.json", "r") as file:
            output = file.read()
        self.assertEqual(output, json_content)
        self.assertEqual(file.name, filename_expected)
        self.assertIsInstance(output, str)
        os.remove(path + "/" + filename_expected)

    def test_from_json_string(self):
        """Test return of a list of the JSON string
        representation json_string"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(Rectangle.from_json_string(
            json_list_input), list_input)
        self.assertIsInstance(
            Rectangle.from_json_string(json_list_input), list)

    def test_from_json_stringNone(self):
        """Test return of a list of the JSON string
        representation json_string None"""
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertIsNotNone(Rectangle.from_json_string(None))

    def test_from_json_string_emptyList(self):
        """Test return of a list of the JSON string
        representation json_string empty"""
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        self.assertEqual(Rectangle.from_json_string(
            json_list_input), list_input)
        self.assertIsInstance(
            Rectangle.from_json_string(json_list_input), list)

    def test_create(self):
        """Test return of an instance with all attributes already set"""
        r10 = Rectangle(3, 5, 1, 2, 10)
        r10_dictionary = r10.to_dictionary()
        r11 = Rectangle.create(**r10_dictionary)
        output = "[Rectangle] (10) 1/2 - 3/5\n[Rectangle] (10) 1/2 - 3/5\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            print(r10)
            print(r11)
            self.assertEqual(_out.getvalue(), output)
        self.assertIsNot(r10, r11)
        self.assertNotEqual(r10, r11)

    def test_load_from_file(self):
        """Test return of a list of instances"""
        r12 = Rectangle(10, 7, 2, 8, 1)
        r13 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r12, r13]
        output = "[Rectangle] (1) 2/8 - 10/7\n[Rectangle] (2) 0/0 - 2/4\n"
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as _out:
            for rect in list_rectangles_output:
                print("{}".format(rect))
            self.assertEqual(_out.getvalue(), output)
        path = os.getcwd()
        os.remove(path + "/" + "Rectangle.json")

    def test_load_from_file_FileNotFoundError(self):
        """Test return of an empty list and FileNotFoundError"""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_pycodestyle(self):
        """Test pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
