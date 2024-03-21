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


class RequiredPutCostReportsBusinessMetricTokensWithMetadataItem(TypedDict):
    # The token of the BusinessMetric to attach to the CostReport.
    business_metric_token: str

class OptionalPutCostReportsBusinessMetricTokensWithMetadataItem(TypedDict, total=False):
    # Determines the scale of the BusinessMetric's values within the CostReport.
    unit_scale: str

class PutCostReportsBusinessMetricTokensWithMetadataItem(RequiredPutCostReportsBusinessMetricTokensWithMetadataItem, OptionalPutCostReportsBusinessMetricTokensWithMetadataItem):
    pass
