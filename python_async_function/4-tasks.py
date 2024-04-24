#!/usr/bin/python3


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
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        await task
        delays.append(task.result())
    return delays
