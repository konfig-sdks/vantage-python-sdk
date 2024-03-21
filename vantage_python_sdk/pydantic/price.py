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


class Price(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    # The unit in which the amount is billed.
    unit: typing.Optional[str] = Field(None, alias='unit')

    # The region the price is specific to.
    region: typing.Optional[str] = Field(None, alias='region')

    # The part of the product the price applies to. (compute, transfer, etc..)
    rate_type: typing.Optional[str] = Field(None, alias='rate_type')

    # The currency of the amount.
    currency: typing.Optional[str] = Field(None, alias='currency')

    # The amount of money this specific product price costs.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Service specific metadata.
    details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
