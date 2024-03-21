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
from vantage_python_sdk.paths.access_grants_access_grant_token import delete
from vantage_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAccessGrantsAccessGrantToken(ApiTestMixin, unittest.TestCase):
    """
    AccessGrantsAccessGrantToken unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204




if __name__ == '__main__':
    unittest.main()
