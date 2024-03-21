# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from vantage_python_sdk.type.put_report_notifications_recipient_channels import PutReportNotificationsRecipientChannels
from vantage_python_sdk.type.put_report_notifications_user_tokens import PutReportNotificationsUserTokens

class RequiredPutReportNotifications(TypedDict):
    pass

class OptionalPutReportNotifications(TypedDict, total=False):
    # The title of the ReportNotification.
    title: str

    # The CostReport token.
    cost_report_token: str

    user_tokens: PutReportNotificationsUserTokens

    recipient_channels: PutReportNotificationsRecipientChannels

    # The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
    frequency: str

    # The type of change the ReportNotification is tracking. Possible values: percentage, dollars.
    change: str

class PutReportNotifications(RequiredPutReportNotifications, OptionalPutReportNotifications):
    pass
