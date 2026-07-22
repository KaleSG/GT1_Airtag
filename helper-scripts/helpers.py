""" helpers.py

Purpose:
    This file helps abstract certain mathematical computations when
    deciding component values for IC designs
"""

# Returns a value with an associated margin.
# ex. computeMargined(100, .15) = 115
def computeMarginedValue(value: float, margin: float):
    return value * (1 + margin)