#!/usr/bin/env python3
"""
This module contains the task_wait_n function which creates multiple asyncio
Tasks for the task_wait_random function and returns the list of delays.
"""


import asyncio
import importlib
from typing import List


# Dynamically import task_wait_random from 3-tasks
tasks_module = importlib.import_module("3-tasks")
task_wait_random = tasks_module.task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates multiple asyncio Tasks for task_wait_random and returns the list of
    delays in ascending order.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay time in seconds for task_wait_random.

    Returns:
        List[float]: A list of delay times in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
