import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def _assert_ok_response(self, endpoint, expected_body):
        url = f"{BASE_URL}{endpoint}"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(expected_body, response.read().decode("utf-8"))

    def _assert_bad_request(self, endpoint):
        url = f"{BASE_URL}{endpoint}"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)

        self.assertEqual(http.client.BAD_REQUEST, context.exception.code)

    def test_api_add(self):
        self._assert_ok_response("/calc/add/2/2", "4")

    def test_api_substract(self):
        self._assert_ok_response("/calc/substract/5/2", "3")

    def test_api_multiply(self):
        self._assert_ok_response("/calc/multiply/5/2", "10")

    def test_api_divide(self):
        self._assert_ok_response("/calc/divide/5/2", "2.5")

    def test_api_power(self):
        self._assert_ok_response("/calc/power/2/3", "8.0")

    def test_api_sqrt(self):
        self._assert_ok_response("/calc/sqrt/9", "3.0")

    def test_api_log10(self):
        self._assert_ok_response("/calc/log10/100", "2.0")

    def test_api_add_bad_request(self):
        self._assert_bad_request("/calc/add/a/2")

    def test_api_divide_bad_request(self):
        self._assert_bad_request("/calc/divide/1/0")

    def test_api_sqrt_bad_request(self):
        self._assert_bad_request("/calc/sqrt/-1")

    def test_api_log10_bad_request(self):
        self._assert_bad_request("/calc/log10/0")
