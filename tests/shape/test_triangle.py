"""
Description: Unit tests for the Book class.
Author: {Jing Li}
Date: {9/22/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""


import unittest

from shape.triangle import Triangle

class Test(unittest.TestCase):
    
    def setUp(self):
        self.triangle = Triangle("red", 3, 4, 5)

    def test_init_valid(self):
           
        # Test the inherited color attiribute from the superclass.
        self.assertEqual("red", self.triangle._color)
        # Access the private attributes of the subclass using name mangling
        self.assertEqual(3, self.triangle._Triangle__side_1)
        self.assertEqual(4, self.triangle._Triangle__side_2)
        self.assertEqual(5, self.triangle._Triangle__side_3)

    def test_init_invalid_color_raises_value_error(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(" ", 3, 4, 5)

    def test_init_invalid_side_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", None, 4, 5)

    def test_init_invalid_side_2_raises_value_error(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", 3, None, 5)

    def test_init_invalid_side_3_raises_value_error(self):
        with self.assertRaises(ValueError):
            triangle = Triangle("red", 3, 4, None)

    def test_str(self):
        expect = "The shape color is red.\nThis triangle has three sides with lengths of 3, 4 and 5 centimeters." 
        self.assertEqual(expect, str(self.triangle))

    def test_calculate_area_return_correct_value(self):
        expect =  6
        self.assertEqual(expect, self.triangle.calculate_area())

    def test_calculate_perimeter_return_correct_value(self):
        expect = 12
        self.assertEqual(expect, self.triangle.calculate_perimeter())
