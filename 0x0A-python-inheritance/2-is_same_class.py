#!/usr/bin/python3
"""
2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """return true if object is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
