#!/usr/bin/env python3
"""summing a mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """using for loop to get the sum"""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    """returning the sum with type float"""
    return float(sum)
