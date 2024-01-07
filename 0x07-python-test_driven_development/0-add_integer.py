#!/usr/bin/python3
"""

This module is comprise of a function that adds two integers

"""


def add_integer(a, b=98):
    """Function adding two integers and float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of two provided  numbers

    Raises:
        TypeError: If a or b are not integers or floats

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
