#!/usr/bin/env python3
""" Implements a function that waits for a random number of seconds """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for multiple tasks """
    delays = [asyncio.create_task(wait_random(max_delay)) for x in range(n)]
    results = []
    for result in asyncio.as_completed(delays):
        results.append(await result)
    return results
