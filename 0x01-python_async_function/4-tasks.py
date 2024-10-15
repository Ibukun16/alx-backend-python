#!/usr/bin/env python3
"""
A function that takes code from wait_n and alter it
into a new function called task_wait_n to call task_wait_random.
"""
import asyncio
import random
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a sorted list of delay similar to wait_n"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
