#!/usr/bin/env python3
"""fixing types in code"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
      typing.Union[typing.Any, None]:
    """return from the function"""
    if lst:
        return lst[0]
    else:
        return None
