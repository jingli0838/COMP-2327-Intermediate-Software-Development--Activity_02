""""
Description: A class to represent generic Vehicle objects.
Author: {Jing Li}
Date: {9/23/2024}
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    An abstract base class representing a vehicle with a a manufacturer(make) and a specific vehicle model.

    Attributes:
        __make(str): Represents the make (manufacturer) of the Vehicle.
        __model(str): Represents the model (specific vehicle model) of the Vehicle.
    """
    
    def __init__(self, make:str, model:str):
        """
        Initializes a vehicle with a manufacturer(make) and a specific vehicle model.

        Args:
            make (str): The make (manufacturer) of the Vehicle.
            model (str): The model (specific vehicle model) of the Vehicle.

        Raises:
            ValueError: If the make is blank.
            ValueError: If the model is blank.
        """

        if (len(make.strip()) == 0):
            raise ValueError("Make cannot be blank.")
        else:
            self.__make = make
        
        if(len(model.strip()) == 0):
            raise ValueError("Model cannot be blank.")
        else:
            self.__model = model

    @property
    def make(self) ->str:
        """
        Gets the make (manufacturer) of the vehicle.

        Returns:
            str: The make (manufacturer) of the vehicle.
        """
        return self.__make
    
    @property
    def model(self) ->str:
        """
        Gets the specific vehicle model of the vehicle.

        Returns:
            str: The specific vehicle model of the vehicle.
        """
        return self.__model
    
    def __str__(self) -> str:
        """
        A string indicating the make and model of the Vehicle.

        Returns:
            str: a string describing the vehicle's manufacture and the specific model.
        """
        return f'Make: {self.make} \n Model: {self.model}'
    
    @abstractmethod
    def calculate_fuel_requirement(self, distance:float) ->float:
        """
        An abstract method calculating the amuont of the fuel (in litres) used by the vehicles with a given distance.
        This method must be implemented by subclasses.

        Args:
            distance (float): The distance traveled by the vehicle in kilometers.

        Returns:
            float: the fuel needed (in litres) to move the vehicle the distance provided.
        """
        pass

 
    

    

      