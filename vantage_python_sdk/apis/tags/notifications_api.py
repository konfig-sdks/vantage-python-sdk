# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from vantage_python_sdk.paths.report_notifications.post import CreateReportNotification
from vantage_python_sdk.paths.report_notifications_report_notification_token.delete import DeleteReportNotification
from vantage_python_sdk.paths.report_notifications.get import GetAllReportNotifications
from vantage_python_sdk.paths.report_notifications_report_notification_token.get import GetReportNotification
from vantage_python_sdk.paths.report_notifications_report_notification_token.put import UpdateReportNotification
from vantage_python_sdk.apis.tags.notifications_api_raw import NotificationsApiRaw


class NotificationsApi(
    CreateReportNotification,
    DeleteReportNotification,
    GetAllReportNotifications,
    GetReportNotification,
    UpdateReportNotification,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: NotificationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = NotificationsApiRaw(api_client)
