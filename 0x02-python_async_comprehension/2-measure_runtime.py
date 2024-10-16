#!/usr/bin/env python3
"""
bring async_comprehension from the previous file and write
a measure_runtime coroutine that execute async_comprehension
four times in parallel using asyncio.gather, and
measure_runtime should measure the total runtime and return it
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel and masure_runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time