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

from vantage_python_sdk.pydantic.post_dashboards_saved_filter_tokens import PostDashboardsSavedFilterTokens
from vantage_python_sdk.pydantic.post_dashboards_widget_tokens import PostDashboardsWidgetTokens

class PostDashboards(BaseModel):
    # The title of the Dashboard.
    title: str = Field(alias='title')

    # The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    end_date: str = Field(alias='end_date')

    widget_tokens: typing.Optional[PostDashboardsWidgetTokens] = Field(None, alias='widget_tokens')

    saved_filter_tokens: typing.Optional[PostDashboardsSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    # Determines how to group costs in the Dashboard.
    date_bin: typing.Optional[Literal["cumulative", "day", "week", "month"]] = Field(None, alias='date_bin')

    # Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.
    date_interval: typing.Optional[Literal["this_month", "last_7_days", "last_30_days", "last_month", "last_3_months", "last_6_months", "custom", "last_12_months", "last_24_months", "last_36_months", "next_month", "next_3_months", "next_6_months", "next_12_months"]] = Field(None, alias='date_interval')

    # The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    start_date: typing.Optional[str] = Field(None, alias='start_date')

    # The token of the Workspace to add the Dashboard to. Required if the API token is associated with multiple Workspaces.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )