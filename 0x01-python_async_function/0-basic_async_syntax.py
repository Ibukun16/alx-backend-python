#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an
integer argument (max_delay, with a default value of 10)
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a number of seconds randomly allocated before return"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
