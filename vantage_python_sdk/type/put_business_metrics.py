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

from vantage_python_sdk.type.put_business_metrics_cost_report_tokens_with_metadata import PutBusinessMetricsCostReportTokensWithMetadata
from vantage_python_sdk.type.put_business_metrics_values import PutBusinessMetricsValues

class RequiredPutBusinessMetrics(TypedDict):
    pass

class OptionalPutBusinessMetrics(TypedDict, total=False):
    # The title of the BusinessMetric.
    title: str

    cost_report_tokens_with_metadata: PutBusinessMetricsCostReportTokensWithMetadata

    values: PutBusinessMetricsValues

class PutBusinessMetrics(RequiredPutBusinessMetrics, OptionalPutBusinessMetrics):
    pass
