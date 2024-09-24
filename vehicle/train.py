""""
Description: A class to represent Train objects.
Author: {Jing Li}
Date: {9/24/2024}
"""

from vehicle.vehicle import Vehicle


class Train(Vehicle):
    """
    A class representing an train, inheriting from Vehicle.

    Attributes:
        __make(str): Represents the make (manufacturer) of the Train.
        __model(str): Represents the model (specific vehicle model) of the Train.
        __cars(int): Represents the number of cars on the Train.
        __base_fuel_rate(float): Represents the rate at which fuel is burned by the Train.
    """
    def __init__(self, make: str, model: str, cars:int, base_fuel_rate:float):
        """
        Initialiazes an Train with make, model, base_fuel_rate and cars.

        Args:
            make (str): The make (manufacturer) of the Train.
            model (str): The model (specific vehicle model) of the Train.
            cars (int): The number of cars on the Train.
            base_fuel_rate (float): The rate at which fuel is burned by the Train.

        Raises:
            ValueError: If the cars argument is not an int.
            ValueError: If the base_fuel_rate argument is not a float.
        """
        super().__init__(make, model)

        if not isinstance(cars, int):
            raise ValueError("Cars must be numeric.")
        else:
            self.__cars = cars

        if not isinstance(base_fuel_rate,float):
            raise ValueError("Base fuel rate must be numeric")
        else:
            self.__base_fuel_rate = base_fuel_rate

    def __str__(self) -> str:
        """
        Returns a string representation of the train.

        Returns:
            str: A string describing the train with the given arguments.

        """
        return super().__str__()+f'\nThis train has a base fuel rate of {self.__base_fuel_rate} litres/kilometer, and contains {self.__cars} cars.'

    def calculate_fuel_requirement(self, distance: float) -> float:
        """
        Calculate the amount of fuel needed by the train for the given distance.

        Args:
            distance (float): the distance to travel in kilometers.

        Returns:
            float: the calculated fuel requirements for the given distance.
        """
        total_fuel = self.__base_fuel_rate * (1.1 * self.__cars)
        fuel_requirements = total_fuel * distance
        return fuel_requirements