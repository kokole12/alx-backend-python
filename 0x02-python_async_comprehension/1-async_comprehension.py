#!/usr/bin/env python3
"""coroutine to return list of floats from function 0-asybc_generator"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returning the random numbers"""
    l = [i async for i in async_generator()]
    return l
