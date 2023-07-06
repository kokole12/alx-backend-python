#!/usr/bin/3nv python3
"""make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multi_by(x: float) -> float:
        return multiplier * x

    return multi_by
