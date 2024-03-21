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

from vantage_python_sdk.pydantic.put_report_notifications_recipient_channels import PutReportNotificationsRecipientChannels
from vantage_python_sdk.pydantic.put_report_notifications_user_tokens import PutReportNotificationsUserTokens

class PutReportNotifications(BaseModel):
    # The title of the ReportNotification.
    title: typing.Optional[str] = Field(None, alias='title')

    # The CostReport token.
    cost_report_token: typing.Optional[str] = Field(None, alias='cost_report_token')

    user_tokens: typing.Optional[PutReportNotificationsUserTokens] = Field(None, alias='user_tokens')

    recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = Field(None, alias='recipient_channels')

    # The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.
    frequency: typing.Optional[str] = Field(None, alias='frequency')

    # The type of change the ReportNotification is tracking. Possible values: percentage, dollars.
    change: typing.Optional[str] = Field(None, alias='change')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
