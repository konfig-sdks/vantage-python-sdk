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


class RequiredPostBusinessMetricsCostReportTokensWithMetadataItem(TypedDict):
    # The token of the CostReport the BusinessMetric is attached to.
    cost_report_token: str

class OptionalPostBusinessMetricsCostReportTokensWithMetadataItem(TypedDict, total=False):
    # Determines the scale of the BusinessMetric's values within the CostReport.
    unit_scale: str

class PostBusinessMetricsCostReportTokensWithMetadataItem(RequiredPostBusinessMetricsCostReportTokensWithMetadataItem, OptionalPostBusinessMetricsCostReportTokensWithMetadataItem):
    pass
