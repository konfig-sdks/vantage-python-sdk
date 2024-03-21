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


class RequiredSegmentReportSettings(TypedDict):
    pass

class OptionalSegmentReportSettings(TypedDict, total=False):
    include_credits: bool

    include_refunds: bool

    include_discounts: bool

    include_tax: bool

    amortize: bool

class SegmentReportSettings(RequiredSegmentReportSettings, OptionalSegmentReportSettings):
    pass
