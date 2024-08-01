#!/usr/bin/env python3
"""
The module that provides a function for creating a function that
    multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    The function takes a float as an argument and returns a function that
        multiplies a float by the multiplier.

    Parameters:
    multiplier (float): The multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that multiplies float by multiplier.
    """
    def multiply(n: float) -> float:
        """
        The function multiplies a float by the multiplier.

        Parameters:
        n (float): The float to multiply by the multiplier.

        Returns:
        float: The result of multiplying n by the multiplier.
        """
        return n * multiplier
    return multiply
