0x0A. Python - Inheritance

0-lookup.py - Write a function that returns the list of available attributes and methods of an object:

1-my_list.py - Write a class MyList that inherits from list

2-is_same_class.py - Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

3-is_kind_of_class.py - Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

4-inherits_from.py - function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise Fals

5-base_geometry.py - Write an empty class BaseGeometry.

6-base_geometry.py - Public instance method: def area(self): that raises an Exception with the message area() is not implemented into the class BaseGeometry

7-base_geometry.py - Public instance method: def integer_validator(self, name, value): that validates value: you can assume name is always a string if value is not an integer: raise a TypeError exception, with the message must be an integer if value is less or equal to 0: raise a ValueError exception with the message must be greater than 0. Into the class BaseGeometry

8-rectangle.py - write a class Rectangle that inherits from BaseGeometry Instantiation with width and height: def init(self, width, height): width and height must be private. No getter or setter width and height must be positive integers, validated by integer_validator

9-rectangle.py - Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py). The area() method must be implemented print() should print, and str() should return, the following rectangle description: [Rectangle] / to the class Rectangle

10-square.py - Write a class Square that inherits from Rectangle Instantiation with size: def init(self, size) size must be private. No getter or setter size must be a positive integer, validated by integer_validator the area() method must be implemented

11-saquare.py - Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py). Print() should print, and str() should return, the square description: [Square] / to the class square
 
100-my_int.py - Write a class MyInt that inherits from int: MyInt is a rebel. MyInt has == and != operators inverted
