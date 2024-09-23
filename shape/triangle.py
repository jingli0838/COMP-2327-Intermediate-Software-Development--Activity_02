""""
Description: A class to represent Triangle objects.
Author: {Jing Li}
Date: {22/9/2024}
"""

import math
from shape.shape import Shape

class Triangle(Shape):
    """
    A class representing a triangle, inheriting from Shape.

    Args:
        _color (str): The color of the triangle.
        __side_1 (int): Represents the length of the first side of the Triangle in centimeters.
        __side_2 (int): Represents the length of the second side of the Triangle in centimeters.
        __side_3 (int): Represents the length of the third side of the Triangle in centimeters.
    """
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """
        Initializes a Triangle with the color and side lengths.

        Args:
            color (str): The color of the triangle.
            side_1 (int): The length of the first side.
            side_2 (int): The length of the second side.
            side_3 (int): The length of the third side.

        Raises:
            ValueError: If the provided sides do not form a valid triangle
            ValueError: If side_1 is not numeric.
            ValueError: If side_2 is not numeric.
            ValueError: If side_3 is not numeric.
        """
        super().__init__(color)
        # validate the length of every side of the triangle is valid
       

        if isinstance(side_1,int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        
        if isinstance(side_2,int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        
        if isinstance(side_3,int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")
        
        

    def __str__(self):
        """
        Returns a string representation of the triangle.

        Returns:
            str: A string describing the triangle's color and  lengths of the three sides.
        """
        return super().__str__()+ f'\nThis triangle has three sides with lengths of {self.__side_1}, {self.__side_2} and {self.__side_3} centimeters.'

    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the triangle
        
        Returns:
            float: the perimeter of the triangle.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter


    def calculate_area(self) -> float:
        """
        Calculates the area of the triangle

        Returns:
            float: the area of the triangle.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))
        return area
 