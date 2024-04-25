#!/usr/bin/env python3
""" Import modules """
import asyncio
import random
from typing import List

async def async_generator() -> List[float]:
    """ Asynchrone function that loop 10 times and
    yield number between 0 and 10 """
    random_numbers = []
    async for _ in range(1, 11):
        await asyncio.sleep(1)
        random_number = random.randint(0, 10)
        random_numbers.append(random_number)
    return random_numbers
