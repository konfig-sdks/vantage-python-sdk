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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from vantage_python_sdk.pydantic.post_report_notifications_recipient_channels import PostReportNotificationsRecipientChannels
from vantage_python_sdk.pydantic.post_report_notifications_user_tokens import PostReportNotificationsUserTokens

class PostReportNotifications(BaseModel):
    # The title of the ReportNotification.
    title: str = Field(alias='title')

    # The CostReport token.
    cost_report_token: str = Field(alias='cost_report_token')

    # The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
    frequency: str = Field(alias='frequency')

    # The type of change the ReportNotification is tracking. Possible values: percentage, dollars.
    change: str = Field(alias='change')

    # The token of the Workspace to add the ReportNotification to. Required if the API token is associated with multiple Workspaces.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    user_tokens: typing.Optional[PostReportNotificationsUserTokens] = Field(None, alias='user_tokens')

    recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = Field(None, alias='recipient_channels')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
