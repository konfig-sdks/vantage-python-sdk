# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

import unittest
from unittest.mock import patch

import urllib3

import vantage_python_sdk
from vantage_python_sdk.paths.segments import post
from vantage_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSegments(ApiTestMixin, unittest.TestCase):
    """
    Segments unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201






if __name__ == '__main__':
    unittest.main()
