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

from vantage_python_sdk.pydantic.product import Product

class Products(BaseModel):
    links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='links')

    products: typing.Optional[typing.List[Product]] = Field(None, alias='products')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )