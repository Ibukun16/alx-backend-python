#!/usr/bin/env python3
"""
Import async_generator from previous task, then write a
coroutine called async_comprehension that takes no arguments.
The coroutine collects 10 random numbers using an async
comprehensing over async_generator, and return the 10 random
numbers.
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns the list of values yield from async_generator"""
    return [value async for value in async_generator()]
