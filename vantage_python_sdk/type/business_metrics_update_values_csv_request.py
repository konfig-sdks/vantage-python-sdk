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


class RequiredBusinessMetricsUpdateValuesCsvRequest(TypedDict):
    # CSV file containing BusinessMetric dates and amounts
    csv: typing.IO

class OptionalBusinessMetricsUpdateValuesCsvRequest(TypedDict, total=False):
    pass

class BusinessMetricsUpdateValuesCsvRequest(RequiredBusinessMetricsUpdateValuesCsvRequest, OptionalBusinessMetricsUpdateValuesCsvRequest):
    pass
