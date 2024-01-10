#!/usr/bin/python3
"""
101-add_attribute.py
"""


def add_attribute(obj, att, value):
    """Add new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
