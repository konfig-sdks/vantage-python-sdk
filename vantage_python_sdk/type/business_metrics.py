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

from vantage_python_sdk.type.business_metric import BusinessMetric

class RequiredBusinessMetrics(TypedDict):
    pass

class OptionalBusinessMetrics(TypedDict, total=False):
    business_metrics: typing.List[BusinessMetric]

class BusinessMetrics(RequiredBusinessMetrics, OptionalBusinessMetrics):
    pass
