#!/usr/bin/env python3
"""
A function that import wait_random from previous python file that was
written and write an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay.

wait_n to return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Execute wait_random n number of time until max_delay, return list of delays"""
    tasks = tuple(map(lambda x: wait_random(max_delay), range(n)))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
