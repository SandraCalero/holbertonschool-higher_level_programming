#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer function"""
    def test_max_integer_success(self):
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        self.assertEqual(max_integer([10, 265, 30, 40]), 265)
        self.assertEqual(max_integer([10, 265, -30, 40]), 265)
        self.assertEqual(max_integer([10, -265, -30, 40]), 40)
        self.assertEqual(max_integer([10, -265, -30, -40]), 10)
        self.assertEqual(max_integer([-10, -265, -30, -40]), -10)
        self.assertEqual(max_integer("Hello"), 'o')
        self.assertEqual(max_integer(["Hello"]), 'Hello')
        self.assertEqual(max_integer([56]), 56)
        self.assertEqual(max_integer([[-10, -265, -30, -40], [1024]]), [1024])

    def test_max_integer_none(self):
        self.assertIsNone(max_integer([None]))
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())


if __name__ == "__main__":
    unittest.main()
