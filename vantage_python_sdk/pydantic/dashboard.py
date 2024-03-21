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

from vantage_python_sdk.pydantic.dashboard_saved_filter_tokens import DashboardSavedFilterTokens
from vantage_python_sdk.pydantic.dashboard_widget_tokens import DashboardWidgetTokens

class Dashboard(BaseModel):
    # The title of the Dashboard.
    title: typing.Optional[str] = Field(None, alias='title')

    token: typing.Optional[str] = Field(None, alias='token')

    widget_tokens: typing.Optional[DashboardWidgetTokens] = Field(None, alias='widget_tokens')

    saved_filter_tokens: typing.Optional[DashboardSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    # Determines how to group costs in the Dashboard.
    date_bin: typing.Optional[Literal["cumulative", "day", "week", "month"]] = Field(None, alias='date_bin')

    # Determines the date range in the Dashboard. Guaranteed to be set to 'custom' if 'start_date' and 'end_date' are set.
    date_interval: typing.Optional[Literal["this_month", "last_7_days", "last_30_days", "last_month", "last_3_months", "last_6_months", "custom", "last_12_months", "last_24_months", "last_36_months", "next_month", "next_3_months", "next_6_months", "next_12_months"]] = Field(None, alias='date_interval')

    # The start date for the date range for CostReports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.
    start_date: typing.Optional[str] = Field(None, alias='start_date')

    # The end date for the date range for CostReports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.
    end_date: typing.Optional[str] = Field(None, alias='end_date')

    # The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
    updated_at: typing.Optional[str] = Field(None, alias='updated_at')

    # The token for the Workspace the Dashboard is a part of.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
