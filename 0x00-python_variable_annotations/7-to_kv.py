#!/usr/bin/env python3
"""passing multiple types as parameters"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v * v))
