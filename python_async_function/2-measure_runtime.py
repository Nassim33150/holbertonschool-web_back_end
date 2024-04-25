#!/usr/bin/python3
""" import modules """
from typing import List
import time
import asyncio


""" import coroutines"""


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:


    asyncio.sleep(max_delay)

    total_time = time.time(wait_n)

    runtime = total_time/n

    return runtime
