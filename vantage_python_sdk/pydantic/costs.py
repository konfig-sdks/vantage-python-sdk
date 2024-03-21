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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from vantage_python_sdk.pydantic.cost import Cost

class Costs(BaseModel):
    links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='links')

    # The sum of all costs for the CostReport for the requested period, rounded to 2 decimal places, alongside the ISO 4217 currency code.
    total_cost: typing.Optional[str] = Field(None, alias='total_cost')

    costs: typing.Optional[typing.List[Cost]] = Field(None, alias='costs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
