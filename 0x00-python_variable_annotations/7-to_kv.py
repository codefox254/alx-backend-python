#!/usr/bin/env python3
"""
The module that provides a function for creating a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    The function takes a string and an int or float, and returns a tuple with
        the string and the square of the int or float as a float.

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: A tuple with the string k and the square of v as a
        float.
    """
    return (k, float(v ** 2))
