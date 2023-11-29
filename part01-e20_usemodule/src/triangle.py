# Enter you module contents here
"""This module provides functions for working with right-angled triangles."""
import math

__author__ = "Alita"
__version__ = "1.0"

def hypotenuse(side1, side2):
    """Calculate the length of the hypotenuse in a right-angled triangle."""
    return math.sqrt(side1**2 + side2**2)

def area(base, height):
    """Calculate the area of a right-angled triangle."""
    return 0.5 * base * height