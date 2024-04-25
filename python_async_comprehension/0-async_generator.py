#!/usr/bin/env python3
""" Import modules """
import asyncio
import random


async def async_generator() -> 'AsyncIterator[float]':
    """ Asynchrone function that loop 10 times and
    yield number between 0 and 10 """
    random_numbers = []
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
