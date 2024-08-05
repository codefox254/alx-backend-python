#!/usr/bin/env python3
"""
This module contains the measure_time function which measures the execution
time of wait_n and returns the average delay.
"""

import asyncio
import importlib
import time


# Dynamically import wait_n from 1-concurrent_coroutines
concurrent_coroutines = importlib.import_module("1-concurrent_coroutines")
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average delay time.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay time in seconds.

    Returns:
        float: The average delay time.
    """
    start_time = time.time()  # Record start time
    delays = asyncio.run(wait_n(n, max_delay))  # Run wait_n
    end_time = time.time()  # Record end time
    
    total_time = end_time - start_time
    average_delay = total_time / n
    
    return average_delay
