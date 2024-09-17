#!/usr/bin/env python3
""" Implements a function that waits for a random number of seconds """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for multiple tasks """
    delays = [task_wait_random(max_delay) for x in range(n)]
    results = []
    for result in asyncio.as_completed(delays):
        results.append(await result)
    return results
