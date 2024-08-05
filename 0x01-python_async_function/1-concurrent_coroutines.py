#!/usr/bin/env python3
"""
This module contains the wait_n coroutine which spawns multiple wait_random
coroutines and returns the list of delays in ascending order.
"""


import asyncio
from typing import List
import importlib

# Dynamically import wait_random from 0-basic_async_syntax
basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the
    list of all delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
