#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
Square module
"""


class Square(Rectangle):
    """square class inherits from Rectangle"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
