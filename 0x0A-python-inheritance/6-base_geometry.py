#!/usr/bin/python3
"""
class module
"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """raise exception if area is not implemented"""
        raise Exception('area() is not implemented')
