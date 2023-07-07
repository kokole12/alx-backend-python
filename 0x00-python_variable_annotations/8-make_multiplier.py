#!/usr/bin/env python3
"""make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """making the multiplication with float"""
    def multi_by(x: float) -> float:
        return multiplier * x
    """returning value"""
    return multi_by
