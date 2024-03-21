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

from vantage_python_sdk.type.dashboard_saved_filter_tokens import DashboardSavedFilterTokens
from vantage_python_sdk.type.dashboard_widget_tokens import DashboardWidgetTokens

class RequiredDashboard(TypedDict):
    pass

class OptionalDashboard(TypedDict, total=False):
    # The title of the Dashboard.
    title: str

    token: str

    widget_tokens: DashboardWidgetTokens

    saved_filter_tokens: DashboardSavedFilterTokens

    # Determines how to group costs in the Dashboard.
    date_bin: str

    # Determines the date range in the Dashboard. Guaranteed to be set to 'custom' if 'start_date' and 'end_date' are set.
    date_interval: str

    # The start date for the date range for CostReports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.
    start_date: str

    # The end date for the date range for CostReports in the Dashboard. ISO 8601 Formatted. Overwrites 'date_interval' if set.
    end_date: str

    # The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
    created_at: str

    # The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted.
    updated_at: str

    # The token for the Workspace the Dashboard is a part of.
    workspace_token: str

class Dashboard(RequiredDashboard, OptionalDashboard):
    pass
