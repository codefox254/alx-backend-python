#!/usr/bin/env python3
"""Test suite for utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the correct value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError for invalid paths"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns the expected result with mocked requests.get"""
        with patch('utils.requests.get') as mock_get:
            # Mock the response to have a .json method that returns test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and assert the result is as expected
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Ensure requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for memoize decorator"""

    class TestClass:
        """Test class for memoize functionality"""

        def a_method(self):
            """Simple method that returns 42"""
            return 42

        @memoize
        def a_property(self):
            """Memoized property that calls a_method"""
            return self.a_method()

    def test_memoize(self):
        """Test that a_method is called only once even if a_property is accessed twice"""
        test_instance = self.TestClass()

        with patch.object(self.TestClass, 'a_method', return_value=42) as mock_method:
            # Access a_property twice
            first_call = test_instance.a_property
            second_call = test_instance.a_property

            # Verify that the correct value is returned
            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)

            # Ensure a_method was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
