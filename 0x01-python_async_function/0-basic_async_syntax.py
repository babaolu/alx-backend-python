#!/usr/bin/env python3
""" Implements a function that waits for a random number of seconds """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int | float:
    """ Waits for at most the max_delay seconds """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
