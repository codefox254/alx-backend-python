#!/usr/bin/env python3
"""
The module that provides a function for returning the first element
    of a list, or None if the list is empty.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    The function returns the first element of a sequence, or None if the
        sequence is empty.

    Parameters:
    lst (Sequence): The sequence to process.

    Returns:
    Union[object, None]: The first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
