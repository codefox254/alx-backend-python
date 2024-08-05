#!/usr/bin/env python3
"""
This module contains the task_wait_random function which creates and returns
an asyncio Task for the wait_random coroutine.
"""

import asyncio
import importlib

# Dynamically import wait_random from 0-basic_async_syntax
basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay time in seconds for wait_random.

    Returns:
        asyncio.Task: The asyncio Task object that schedules the execution of
                       wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

