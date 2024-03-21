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

from vantage_python_sdk.type.business_metric_cost_report_tokens_with_metadata import BusinessMetricCostReportTokensWithMetadata
from vantage_python_sdk.type.business_metric_values import BusinessMetricValues

class RequiredBusinessMetric(TypedDict):
    pass

class OptionalBusinessMetric(TypedDict, total=False):
    # The title of the BusinessMetric.
    title: str

    # The token of the BusinessMetric.
    token: str

    # The token of the User who created the BusinessMetric.
    created_by_token: str

    cost_report_tokens_with_metadata: BusinessMetricCostReportTokensWithMetadata

    values: BusinessMetricValues

class BusinessMetric(RequiredBusinessMetric, OptionalBusinessMetric):
    pass
