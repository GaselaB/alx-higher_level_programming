#!/usr/bin/python3
"""

Defines a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides an  integer or float number of a matrix

    Args:
        matrix: lists of integers/floats
        div: number dividing the matrix

    Returns:
        A new matrix comprising the result of the division

    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elemetns of the lists are not integers/floats
                   If div is not an integer or float number
                   If the lists of the matrix do not have the same size

        ZeroDivisionError: If div is zero


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
