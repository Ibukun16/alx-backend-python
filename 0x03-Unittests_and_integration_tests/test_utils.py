#!/usr/bin/env python3
"""
write the first unit test for utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from
unittest.TestCase. Implement the
TestAccessNestedMap.test_access_nested_map method to
test that the method returns what it is supposed to.
Decorate the method with @parameterized.expand to test
the function for the following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing Nested Map function

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test method return output"""
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """Test method that return corect output for exception case"""
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ({}, ("a"), 1),
        ({"a": 1}, ("a", "b"), 2)
    ])
    def test_access_nested_map_exception(self, nested_map, path, wrong_output):
        """Test method that raises KeyError for exception cases
        that expect an output
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(wrong_output, context.exception)


class TestGetJson(unittest.TestCase):
    """Class for testing GetJson function

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Return correct output for get_json"""
        attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as cor_response:
            self.assertEqual(get_json(test_url), test_payload)
            cor_response.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Class for testing memoization

    Args:
        unittest (_type_): _description_
    """
    def test_memoize(self) -> None:
        """A function that Test for memoize"""

        class TestClass:
            """The Test class"""
            def a_method(self):
                """Method that always return 42"""
                return 42

            @memoize
            def a_property(self):
                """Function that returns memoized property

                Return:
                        _type_: _description_
                """
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as res:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            res.assert_called_once()
