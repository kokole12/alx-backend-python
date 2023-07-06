#!/usr/bin/env python3
"""summing a mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return float(sum)
