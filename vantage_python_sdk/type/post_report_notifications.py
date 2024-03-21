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

from vantage_python_sdk.type.post_report_notifications_recipient_channels import PostReportNotificationsRecipientChannels
from vantage_python_sdk.type.post_report_notifications_user_tokens import PostReportNotificationsUserTokens

class RequiredPostReportNotifications(TypedDict):
    # The title of the ReportNotification.
    title: str

    # The CostReport token.
    cost_report_token: str

    # The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
    frequency: str

    # The type of change the ReportNotification is tracking. Possible values: percentage, dollars.
    change: str

class OptionalPostReportNotifications(TypedDict, total=False):
    # The token of the Workspace to add the ReportNotification to. Required if the API token is associated with multiple Workspaces.
    workspace_token: str

    user_tokens: PostReportNotificationsUserTokens

    recipient_channels: PostReportNotificationsRecipientChannels

class PostReportNotifications(RequiredPostReportNotifications, OptionalPostReportNotifications):
    pass
