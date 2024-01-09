#!/usr/bin/python3
def number_of_lines(filename=""):
    """Define a function that returns the number of lines of a text file """

    with open(filename) as f:
        count = len(f.readlines())
    return count
