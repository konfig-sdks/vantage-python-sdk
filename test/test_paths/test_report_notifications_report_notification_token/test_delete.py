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
from vantage_python_sdk.paths.report_notifications_report_notification_token import delete
from vantage_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestReportNotificationsReportNotificationToken(ApiTestMixin, unittest.TestCase):
    """
    ReportNotificationsReportNotificationToken unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204




if __name__ == '__main__':
    unittest.main()
