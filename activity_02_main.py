""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: {JinG Li}
Date: {9/23/2024}
"""
from shape import *
from vehicle import *

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")
    # 1. Create an empty list of Shape objects.
    shapes = []




    # 2. Code a statement which creates an instance of the Triangle class.
    # Append the Triangle to the list of shapes.
    try:
        red_triangle = Triangle("red", 3, 4, 5)
        shapes.append(red_triangle)
    except ValueError as e:
        print(e)
    



    # 3. Code a statement which creates an instance of the Rectangle class.
    # Append the Rectangle to the list of shapes.
    try:
        red_rectangle = Rectangle("red", 4, 5)
        shapes.append(red_rectangle)
    except ValueError as e:
        print(e)
    

    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        blue_triangle = Triangle("blue", 5, 6, 7)
        shapes.append(blue_triangle)
    except ValueError as e:
        print(e)
    

    try:
        blue_rectangle = Rectangle("blue", 6, 7)
        shapes.append(blue_rectangle)
    except ValueError as e:
        print(e)
    

    try:
        yellow_triangle = Triangle("yellow", 6, 8, 7)
        shapes.append(yellow_triangle)
    except ValueError as e:
        print(e)
    



    # 5. Iterate through the list of shapes.  On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        try:
            print(shape)
        except ValueError as e:
            print(e)
       
        try:
            print(f'the area of the shape: {shape.calculate_area():.2f}')
        except ValueError as e:
            print(e)
        
        try:
            print(f'the perimeter of the shape: {shape.calculate_perimeter():.2f}')
        except ValueError as e:
            print(e)

        print()

    
    

    


    # *** END PART 1 ***

    # *** PART 2 ***
    print("*************PART 2****************")
    # 1. Create an empty list of Vehicle objects.
    vehicles = []

    # 2. Code a statement which creates an instance of the Automobile class.
    # Append the Automobile to the list of vehicles.
    try:
        automobile_01 = Automobile("HONDA", "HRV", 20.0)
        vehicles.append(automobile_01)
    except ValueError as e:
        print(e)
    

    # 3. Code a statement which creates an instance of the Aircraft class.
    # Append the Aircraft to the list of vehicles.
    try:
        aircraft = Aircraft("Boeing", "Air Bus", 40.0, 550.0)
        vehicles.append(aircraft)
    except ValueError as e:
        print(e)
    


    # 4. Code 3 additional statements which creates an instance of 
    # Automobile, Aircraft or Train classes (your choice).
    # Append these instances to the list of vehicles.

    try:
        train = Train("Siemens", "Intercity Subway", 13, 0.03)
        vehicles.append(train)
    except ValueError as e:
        print(e)
    
    

    try:
        automobile_02 = Automobile("Ford", "Escape", 15.0)
        vehicles.append(automobile_02)
    except ValueError as e:
        print(e)
    

    
    try :
        automobile_03 = Automobile("Honda", "CRV", 13.5)
        vehicles.append(automobile_03)
    except ValueError as e:
        print(e)
    




    # 5. Iterate through the list of vehicles.  On each iteration:
    # - print the vehicle
    # - print the phrase:
    # "Fuel needed for 500 kilometers: {fuel requirements} litres."
    for vehicle in vehicles:
        try:
            print(vehicle)
        except ValueError as e:
            print(e)
        
        try:
            print(f'Fuel needed for 500 kilometers:{vehicle.calculate_fuel_requirement(500.0):.2f} litres.')
        except ValueError as e:
            print(e)
        print()

if __name__ == "__main__":
    main()