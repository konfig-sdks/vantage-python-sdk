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


class CostReportSettings(BaseModel):
    # Report will include credits.
    include_credits: typing.Optional[bool] = Field(None, alias='include_credits')

    # Report will include refunds.
    include_refunds: typing.Optional[bool] = Field(None, alias='include_refunds')

    # Report will include discounts.
    include_discounts: typing.Optional[bool] = Field(None, alias='include_discounts')

    # Report will include tax.
    include_tax: typing.Optional[bool] = Field(None, alias='include_tax')

    # Report will amortize.
    amortize: typing.Optional[bool] = Field(None, alias='amortize')

    # Report will show unallocated costs.
    unallocated: typing.Optional[bool] = Field(None, alias='unallocated')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
