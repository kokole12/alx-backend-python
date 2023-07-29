#!/usr/bin/env python3
"""testing the utils.py"""
import unittest
from unittest.mock import patch, Mock
from typing import Dict, Tuple, Union
from parameterized import parameterized, parameterized_class
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """Testing the accesNested map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nest_map: Dict,
                               path: Tuple[str],
                               expect: Union[Dict, int]) -> None:
        self.assertEqual(access_nested_map(nest_map, path), expect)


if __name__ == "__main__":
    unittest.main()
