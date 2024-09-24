"""
Description: Unit tests for the Train class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_train.py
"""

import unittest

from vehicle.train import Train

class Test(unittest.TestCase):
    
    def setUp(self):
        self.train = Train("Siemens", "Intercity Subway", 13, 0.03)

    def test_init_valid(self):
        self.assertEqual("Siemens", self.train._Vehicle__make)
        self.assertEqual("Intercity Subway", self.train._Vehicle__model)
        self.assertEqual(13, self.train._Train__cars)
        self.assertEqual(0.03, self.train._Train__base_fuel_rate)

    def test_init_make_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            train = Train("  ", "Intercity Subway", 13, 0.03)
    
    def test_init_model_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", "  ", 13, 0.03)

    def test_init_cars_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", "Intercity Subway", "cars", 0.03)

    def test_init_base_fuel_rate_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            train = Train("Siemens", "Intercity Subway", 13, None)

    def test_str(self):
        expected = 'Make: Siemens \n Model: Intercity Subway\nThis train has a base fuel rate of 0.03 litres/kilometer, and contains 13 cars.'
    
    def test_calculate_fuel_requiremen_returns_correct_value(self):
        self.assertEqual(42.9, self.train.calculate_fuel_requirement(100.0))



