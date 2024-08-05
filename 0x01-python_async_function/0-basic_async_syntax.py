#!/usr/bin/env python3
"""
    Aysncronous python: coroutine takes int as an arg with 10 as def
"""

import random
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the
    delay time.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
        float: The amount of time waited in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
