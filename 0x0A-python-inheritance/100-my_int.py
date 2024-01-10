#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, other):
        if self.real == other.real:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.real == other.real:
            return True
        else:
            return False
