#!/usr/bin/env python3
"""
    Function to take a max_delay as parameter and monitoring the
    coroutines
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waiting time """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
