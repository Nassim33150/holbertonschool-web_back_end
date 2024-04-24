#!/usr/bin/python3
""" import modules """
from typing import List
import time
import asyncio


""" import coroutines"""


wait_n = __import__('1-concurrent_coroutines').wait_n


""" Create a measure_time function
with integers n and max_delay as
arguments that measures the total
execution time for wait_n(n, max_delay),
and returns total_time / n. """


def measure_time(n: int, max_delay: int) -> float:

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    average_time = total_time / n

    return average_time
