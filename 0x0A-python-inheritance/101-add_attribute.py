#!/usr/bin/python3
"""
method module
"""


def add_attribute(obj, objname, value):
    """add attribute to object
    """

    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
