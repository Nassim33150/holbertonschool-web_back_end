#!/usr/bin/python3
import asyncio
from typing import List


""" execute multiple coroutines at the same time """


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    coroutines = [wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
