""""
Description: A class to represent Aircraft objects.
Author: {Jing Li}
Date: {9/23/2024}
"""

from vehicle.vehicle import Vehicle


class Aircraft(Vehicle):
    """
    A class representing an automobile, inheriting from Vehicle.

    Attributes: 
        make(str): Represents the make (manufacturer) of the Vehicle.
        model(str): Represents the model (specific vehicle model) of the Vehicle.
        fuel_burn_rate (float): The rate at which Aircraft fuel is expended.
        speed (float): The cruising speed of the Aircraft.
    """

    def __init__(self, make: str, model: str, fuel_burn_rate:float, speed:float):
        """
        Initialiazes an Aircraft with make, model, fuel_burn_rate and speed.

        Args:
            make (str): The make (manufacturer) of the aircraft.
            model (str): The model (specific vehicle model) of the aircraft.
            fuel_burn_rate (float): The rate at which Aircraft fuel is expended.
            speed (float): The cruising speed of the Aircraft.

        Raises:
            ValueError: If the fuel_burn_rate argument is not a float.
            ValueError: If the speed argument is not a float.
        """
        super().__init__(make, model)

        if not isinstance(fuel_burn_rate, float):
            raise ValueError("Fuel burn rate must be numeric.",)
        else:
            self.__fuel_burn_rate = fuel_burn_rate

        if not isinstance(speed, float):
            raise ValueError("Speed must be numeric.")
        else:
            self.__speed = speed


    def __str__(self) -> str:
        """
        Returns a string representation of the aircraft.

        Returns:
            str: A string describing the aircraft with the given arguments.
        """
        return super().__str__()+f'\nThis aircraft has a fuel burn rate of {self.__fuel_burn_rate} litres/hour, and a cruising speed of {self.__speed} km/hour.'

    def calculate_fuel_requirement(self, distance:float) ->float:
        """
        Calculate the amount of fuel needed by the aircraft for the given distance.

        Args:
            distance (float): the distance to cruise in kilometers.

        Returns:
            float: the calculated fuel requirements for the given distance.
        """
        flight_time = distance / self.__speed
        fuel_requirements = flight_time * self.__fuel_burn_rate
        return fuel_requirements


