#!/usr/bin/env python3
""" execute multiple coroutines at the same time """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns the list of all the delays (float values). """
    delays = []

    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
