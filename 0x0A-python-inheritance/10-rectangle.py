#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
module with class BaseGeometry
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """initializing the attributes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area of a rectangle"""

        return self.__size ** 2
