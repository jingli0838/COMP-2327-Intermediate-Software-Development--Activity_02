""""
Description: A class to represent Automobile objects.
Author: {Jing Li}
Date: {9/23/2024}
"""

from vehicle.vehicle import Vehicle


class Automobile(Vehicle):
    """
    A class representing an automobile, inheriting from Vehicle.

    Attributes: 
        __kilometers_per_litre (float): The number of kilometers the Automobile can drive per litre of gasoline.    
    """

    def __init__(self, make: str, model: str, kilometers_per_litre: float):
        """
        Initialiazes an Automobile with make, model, and kilometers_per_litre.

        Args:
            make (str): The make (manufacturer) of the automobile.
            model (str): The model (specific vehicle model) of the Vehicle.
            kilometers_per_litre (float): The number of kilometers the Automobile can drive per litre of gasoline.
        Raises:
            ValueError: if kilometers_per_litre argument is not a float.
        """
        super().__init__(make, model)
        if not isinstance(kilometers_per_litre,float):
            raise ValueError("Kilometers per litre must be numeric.")
        else: 
            self.__kilometers_per_litre = kilometers_per_litre


    def __str__(self) -> str:
        """
        Returns a string representation of the automobile.

        Returns:
            str: A string describing the autombile with the given arguments.
        """
        return super().__str__()+f'\nThis automobile can drive {self.__kilometers_per_litre} kilometers per litre.'

    def calculate_fuel_requirement(self, distance: float) -> float:
        """
        Calculate the amount of fuel needed by the automobile for the given distance.

        Args:
            distance (float): the distance to drive in kilometers.

        Returns:
            float: the calculated fuel requirements for the given distance.
        """
        fuel_requirements = distance / self.__kilometers_per_litre
        return fuel_requirements



