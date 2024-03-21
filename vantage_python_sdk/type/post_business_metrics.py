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

from vantage_python_sdk.type.post_business_metrics_cost_report_tokens_with_metadata import PostBusinessMetricsCostReportTokensWithMetadata
from vantage_python_sdk.type.post_business_metrics_values import PostBusinessMetricsValues

class RequiredPostBusinessMetrics(TypedDict):
    # The title of the Business Metric.
    title: str

class OptionalPostBusinessMetrics(TypedDict, total=False):
    cost_report_tokens_with_metadata: PostBusinessMetricsCostReportTokensWithMetadata

    values: PostBusinessMetricsValues

class PostBusinessMetrics(RequiredPostBusinessMetrics, OptionalPostBusinessMetrics):
    pass
