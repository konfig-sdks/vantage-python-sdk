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

from vantage_python_sdk.type.report_notification_recipient_channels import ReportNotificationRecipientChannels
from vantage_python_sdk.type.report_notification_user_tokens import ReportNotificationUserTokens

class RequiredReportNotification(TypedDict):
    pass

class OptionalReportNotification(TypedDict, total=False):
    # The title of the ReportNotification.
    title: str

    token: str

    # The token for a CostReport the ReportNotification is applied to.
    cost_report_token: str

    user_tokens: ReportNotificationUserTokens

    recipient_channels: ReportNotificationRecipientChannels

    # The frequency the ReportNotification is sent.
    frequency: str

    # The type of change the ReportNotification is tracking.
    change: str

class ReportNotification(RequiredReportNotification, OptionalReportNotification):
    pass
