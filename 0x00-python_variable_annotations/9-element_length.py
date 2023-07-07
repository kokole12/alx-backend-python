#!/usr/bin/env python3
"""annotating function for the correct output"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returning the result"""
    return [(i, len(i)) for i in lst]
