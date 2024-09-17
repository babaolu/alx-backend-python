#!/usr/bin/env python3
""" Implements a function that creates an asynchronous task """
import asyncio
import importlib


wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """ Returns and asyncio Task """
    return asyncio.create_task(wait_random(max_delay))
