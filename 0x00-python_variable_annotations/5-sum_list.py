#!/usr/bin/env python3
"""summing elements in a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """looping to find the sum"""
    sum: float = 0
    for i in input_list:
        sum += i
    """returning the sum"""
    return float(sum)
