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

    @parameterized.expand([
        ({}, ('a'), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         nest_map: Dict, path: Tuple[str],
                                         expected: Exception):
        """testing the exceptions raised by the utils function"""
        with self.assertRaises(expected):
            access_nested_map(nest_map, path)


class TestGetJson(unittest.TestCase):
    """testing the get json function and mocking the requests model"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        attrs = {'json.return_value': payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(url), payload)
            req_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
