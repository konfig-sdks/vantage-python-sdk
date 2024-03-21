# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

import unittest

import os
from pprint import pprint
from vantage_python_sdk import Vantage

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        vantage = Vantage(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(vantage)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
