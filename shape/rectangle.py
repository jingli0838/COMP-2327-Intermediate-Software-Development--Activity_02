""""
Description: A class to represent Rectangle objects.
Author: {Jing Li}
Date: {9/23/2024}
"""

from shape.shape import Shape


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        _color (str): The color of the rectangle.
        __length (int): Represents the length of two opposing sides of the Rectangle in centimeters.
        __width (int): Represents the width of two opposing sides of the Rectangle in centimeters.
    """
    def __init__(self, color: str, length: int, width: int):
        """
        Initializes a Rectangle with the color and length and width.

        Args:
            color (str): The color of the rectangle.
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.

        Raises:
            ValueError: if the width is not numeric.
            ValueError: if the length is not numeric.
        """
        super().__init__(color)
        
        if not isinstance(length, int):
            raise ValueError("Length must be numeric")
        else:
            self.__length = length

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        else:
            self.__width = width

    def __str__(self) ->str:
        """
        A string representation of the rectangle.

        Returns:
            str: A string describing the rectangle's color ,width and length of the rectangle.
        """
        return super().__str__()+f'\nThis rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters.'

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: the area of the rectangle.
        """
        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: the perimeter of the rectangle.
        """
        perimeter = self.__length * 2 + self.__width * 2
        return perimeter
    
