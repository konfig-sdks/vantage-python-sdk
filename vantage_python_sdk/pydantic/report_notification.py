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

from vantage_python_sdk.pydantic.report_notification_recipient_channels import ReportNotificationRecipientChannels
from vantage_python_sdk.pydantic.report_notification_user_tokens import ReportNotificationUserTokens

class ReportNotification(BaseModel):
    # The title of the ReportNotification.
    title: typing.Optional[str] = Field(None, alias='title')

    token: typing.Optional[str] = Field(None, alias='token')

    # The token for a CostReport the ReportNotification is applied to.
    cost_report_token: typing.Optional[str] = Field(None, alias='cost_report_token')

    user_tokens: typing.Optional[ReportNotificationUserTokens] = Field(None, alias='user_tokens')

    recipient_channels: typing.Optional[ReportNotificationRecipientChannels] = Field(None, alias='recipient_channels')

    # The frequency the ReportNotification is sent.
    frequency: typing.Optional[Literal["daily", "weekly", "monthly"]] = Field(None, alias='frequency')

    # The type of change the ReportNotification is tracking.
    change: typing.Optional[Literal["percentage", "dollars"]] = Field(None, alias='change')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
