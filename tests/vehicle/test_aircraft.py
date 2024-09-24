"""
Description: Unit tests for the Aircrat class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_aircraft.py
"""

import unittest

from vehicle.aircraft import Aircraft

class test(unittest.TestCase):

    def setUp(self):
        self.aircraft = Aircraft("Boeing", "Air Bus", 40.0, 550.0)

    def test_init_valid(self):

        self.assertEqual("Boeing", self.aircraft._Vehicle__make)
        self.assertEqual("Air Bus", self.aircraft._Vehicle__model)
        self.assertEqual(40.0, self.aircraft._Aircraft__fuel_burn_rate)
        self.assertEqual(550.0, self.aircraft._Aircraft__speed)

    def test_init_make_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft(" ", "Air Bus", 40.0, 550.0)

    def test_init_model_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "  ", 40.0, 550.0)

    def test_init_fuel_burn_rate_invalid_raises_value_error(self):
        with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "Air Bus", "rate", 550.0)

    def test_init_speed_invalid_raises_value_error(self):
         with self.assertRaises(ValueError):
            aircraft = Aircraft("Boeing", "Air Bus",  40.0, "speed")

    def test_str(self):
        expected = "Make: Boeing \n Model: Air Bus\nThis aircraft has a fuel burn rate of 40.0 litres/hour, and a cruising speed of 550.0 km/hour."
        self.assertEqual(expected, str(self.aircraft))

    def test_calculate_fuel_requirement_returns_correct_value(self):
        self.assertEqual(1200.0, self.aircraft.calculate_fuel_requirement(16500.0))
