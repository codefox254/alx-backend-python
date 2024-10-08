#!/usr/bin/env python3
"""
    Aysncronous python: coroutine takes int as an arg with 10 as def
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the
    delay time.

    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10.

    Returns:
        float: The amount of time waited in seconds.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
