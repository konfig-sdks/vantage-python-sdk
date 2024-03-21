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

from vantage_python_sdk.type.cost_report_business_metric_tokens_with_metadata import CostReportBusinessMetricTokensWithMetadata
from vantage_python_sdk.type.cost_report_saved_filter_tokens import CostReportSavedFilterTokens
from vantage_python_sdk.type.cost_report_settings import CostReportSettings

class RequiredCostReport(TypedDict):
    pass

class OptionalCostReport(TypedDict, total=False):
    # The title of the CostReport.
    title: str

    token: str

    # The token for the Folder the CostReport is a part of.
    folder_token: str

    saved_filter_tokens: CostReportSavedFilterTokens

    business_metric_tokens_with_metadata: CostReportBusinessMetricTokensWithMetadata

    # The filter applied to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    # The grouping aggregations applied to the filtered data.
    groupings: str

    settings: CostReportSettings

    # The date and time, in UTC, the report was created. ISO 8601 Formatted.
    created_at: str

    # The token for the Workspace the CostReport is a part of.
    workspace_token: str

class CostReport(RequiredCostReport, OptionalCostReport):
    pass
