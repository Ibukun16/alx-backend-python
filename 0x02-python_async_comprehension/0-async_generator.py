#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments,
it loops 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generate a sequence of 10 numbers by looping 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
