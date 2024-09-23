"""
Description: Unit tests for the Rectangle class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/rectangle.py
"""

import unittest

from shape.rectangle import Rectangle

class Test(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle("red", 4, 5)

    def test_init_valid(self):
        self.assertEqual("red", self.rectangle._color)
        self.assertEqual(4, self.rectangle._Rectangle__length)
        self.assertEqual(5, self.rectangle._Rectangle__width)

    def test_init_invalid_color_raises_value_error(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(" ", 4, 5)

    def test_init_invalid_length_raises_value_error(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("red", "length", 5)

    def test_init_invalid_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle("red", 4, "width")

    def test_str(self):
        expected = "The shape color is red.\nThis rectangle has four sides with the lengths of 4, 5, 4 and 5 centimeters."      
        self.assertEqual(expected, str(self.rectangle))

    def test_caculate_area_return_correct_value(self):
        self.assertEqual(20, self.rectangle.calculate_area())

    def test_caculate_perimeter_return_correct_value(self):
        self.assertEqual(18, self.rectangle.calculate_perimeter())

    

    

    


