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

from vantage_python_sdk.type.cost import Cost

class RequiredCosts(TypedDict):
    pass

class OptionalCosts(TypedDict, total=False):
    links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The sum of all costs for the CostReport for the requested period, rounded to 2 decimal places, alongside the ISO 4217 currency code.
    total_cost: str

    costs: typing.List[Cost]

class Costs(RequiredCosts, OptionalCosts):
    pass
