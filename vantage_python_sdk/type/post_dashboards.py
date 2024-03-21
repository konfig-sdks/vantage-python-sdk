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

from vantage_python_sdk.type.post_dashboards_saved_filter_tokens import PostDashboardsSavedFilterTokens
from vantage_python_sdk.type.post_dashboards_widget_tokens import PostDashboardsWidgetTokens

class RequiredPostDashboards(TypedDict):
    # The title of the Dashboard.
    title: str

    # The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    end_date: str

class OptionalPostDashboards(TypedDict, total=False):
    widget_tokens: PostDashboardsWidgetTokens

    saved_filter_tokens: PostDashboardsSavedFilterTokens

    # Determines how to group costs in the Dashboard.
    date_bin: str

    # Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.
    date_interval: str

    # The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.
    start_date: str

    # The token of the Workspace to add the Dashboard to. Required if the API token is associated with multiple Workspaces.
    workspace_token: str

class PostDashboards(RequiredPostDashboards, OptionalPostDashboards):
    pass
