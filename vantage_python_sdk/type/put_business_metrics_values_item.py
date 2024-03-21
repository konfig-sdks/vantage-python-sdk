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


class RequiredPutBusinessMetricsValuesItem(TypedDict):
    date: datetime

    amount: typing.Union[int, float]

class OptionalPutBusinessMetricsValuesItem(TypedDict, total=False):
    pass

class PutBusinessMetricsValuesItem(RequiredPutBusinessMetricsValuesItem, OptionalPutBusinessMetricsValuesItem):
    pass
