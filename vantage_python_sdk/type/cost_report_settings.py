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


class RequiredCostReportSettings(TypedDict):
    pass

class OptionalCostReportSettings(TypedDict, total=False):
    # Report will include credits.
    include_credits: bool

    # Report will include refunds.
    include_refunds: bool

    # Report will include discounts.
    include_discounts: bool

    # Report will include tax.
    include_tax: bool

    # Report will amortize.
    amortize: bool

    # Report will show unallocated costs.
    unallocated: bool

class CostReportSettings(RequiredCostReportSettings, OptionalCostReportSettings):
    pass
