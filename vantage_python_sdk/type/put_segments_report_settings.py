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


class RequiredPutSegmentsReportSettings(TypedDict):
    pass

class OptionalPutSegmentsReportSettings(TypedDict, total=False):
    # Reports created under this Segment will include credits.
    include_credits: bool

    # Reports created under this Segment will include refunds.
    include_refunds: bool

    # Reports created under this Segment will include discounts.
    include_discounts: bool

    # Reports created under this Segment will include tax.
    include_tax: bool

    # Reports created under this Segment will amortize.
    amortize: bool

class PutSegmentsReportSettings(RequiredPutSegmentsReportSettings, OptionalPutSegmentsReportSettings):
    pass
