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

from vantage_python_sdk.type.put_dashboards_saved_filter_tokens import PutDashboardsSavedFilterTokens
from vantage_python_sdk.type.put_dashboards_widget_tokens import PutDashboardsWidgetTokens

class RequiredPutDashboards(TypedDict):
    # The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    end_date: str

class OptionalPutDashboards(TypedDict, total=False):
    # The title of the Dashboard.
    title: str

    widget_tokens: PutDashboardsWidgetTokens

    saved_filter_tokens: PutDashboardsSavedFilterTokens

    # Determines how to group costs in the Dashboard.
    date_bin: str

    # Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.
    date_interval: str

    # The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    start_date: str

class PutDashboards(RequiredPutDashboards, OptionalPutDashboards):
    pass
