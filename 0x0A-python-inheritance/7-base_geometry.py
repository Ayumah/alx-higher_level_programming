#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """raise exception is area is not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
