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


class RequiredPrice(TypedDict):
    pass

class OptionalPrice(TypedDict, total=False):
    id: str

    # The unit in which the amount is billed.
    unit: str

    # The region the price is specific to.
    region: str

    # The part of the product the price applies to. (compute, transfer, etc..)
    rate_type: str

    # The currency of the amount.
    currency: str

    # The amount of money this specific product price costs.
    amount: typing.Union[int, float]

    # Service specific metadata.
    details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Price(RequiredPrice, OptionalPrice):
    pass
