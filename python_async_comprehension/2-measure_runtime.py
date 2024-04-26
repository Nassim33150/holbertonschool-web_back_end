#!/usr/bin/env python3
""" Import asyncio """
import asyncio


""" Import async_comprehension """
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ This coroutine that will
    execute async_comprehension four times
    and measure the total runtime and return
    it. """

    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
            *[async_comprehension() for _ in range(4)]
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
