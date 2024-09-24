""""
Description: A class to represent generic Shape objects.
Author: {Jing Li}
Date: {22/9/2024}
"""

from abc import ABC, abstractmethod



class Shape(ABC):
    """
    An abstract base class representing a shape with a color.

    Attributes:
        _color (str): the color of the Shape.
    """
    def __init__(self,color:str):
        """
        Initializes a Shape with the designed color.

        Args:
            color (str): The color of the shape.

        Raises:
            ValueError: If the color is blank.

        """
        if len(color.strip()) == 0:
            raise ValueError ("Color cannot be blank")
        
        self._color = color
            

    def __str__(self):
        """
        Returns a string representation of the shape.

        Returns:
            str: A string describing the color of the shape.
        """
        return f'The shape color is {self._color}.'
    
    @abstractmethod
    def calculate_area(self) ->float:
        """
        An abstract method calculating the area of the shape.
        This method must be implemented by subclasses.

        Returns:
            float: The area of the shape.
        """
        pass
    
    @abstractmethod
    def calculate_perimeter(self) ->float:
        """
        An abstract method calculating the perimeter of the shape.
        This method must be implemented by subclasses.

        Returns:
            float: The perimeter of the shape.
        """
        pass


    

    
    
