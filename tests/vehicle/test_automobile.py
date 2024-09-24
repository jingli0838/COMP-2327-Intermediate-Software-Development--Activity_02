"""
Description: Unit tests for the Automobile class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_automobile.py
"""

import unittest

from vehicle.automobile import Automobile

class Test(unittest.TestCase):

    def setUp(self):
        self.automobile = Automobile("HONDA", "CRV", 20.0)

    def test_init_valid(self):
        self.assertEqual("HONDA", self.automobile.make)   
        self.assertEqual("CRV", self.automobile.model)
        self.assertEqual(20.0, self.automobile._Automobile__kilometers_per_litre)

    def test_init_make_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            automobile = Automobile(" ", "CRV", 20.0)

    def test_init_model_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            automobile = Automobile("HONDA", " ", 20.0)

    def test_str(self):
        expected = "Make: HONDA \n Model: CRV\nThis automobile can drive 20.0 kilometers per litre."
        self.assertEqual(expected, str(self.automobile))

    def test_calculate_fuel_requirement_returns_correct_value(self):
        self.assertEqual(5, self.automobile.calculate_fuel_requirement(100.0))