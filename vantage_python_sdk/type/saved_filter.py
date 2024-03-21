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

from vantage_python_sdk.type.saved_filter_cost_report_tokens import SavedFilterCostReportTokens

class RequiredSavedFilter(TypedDict):
    pass

class OptionalSavedFilter(TypedDict, total=False):
    # The title of the SavedFilter.
    title: str

    token: str

    cost_report_tokens: SavedFilterCostReportTokens

    # The SavedFilter's filter, applied to any relevant CostReports. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    # The date and time, in UTC, the report was created. ISO 8601 Formatted.
    created_at: str

    # The User who created the SavedFilter.
    created_by: str

    # The token for the Workspace the SavedFilter is a part of.
    workspace_token: str

class SavedFilter(RequiredSavedFilter, OptionalSavedFilter):
    pass
