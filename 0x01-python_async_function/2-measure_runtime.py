#!/usr/bin/env python3
"""
A function that measure_time with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Your
function should return a float.
"""
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()

    total_time = end_time - start_time
    return total_time / n
