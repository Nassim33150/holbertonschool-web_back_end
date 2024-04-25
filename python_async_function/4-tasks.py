#!/usr/bin/env python3

""" import modules """


import asyncio
from typing import List


""" import wait_random """


task_wait_random = __import__('3-tasks').task_wait_random


""" Take the code from wait_n and
alter it into a new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called. """


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns the list of all the delays (float values)
        from async task. """
    delays = []

    coroutines = [task_wait_random(max_delay) for _ in range(n)]

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
