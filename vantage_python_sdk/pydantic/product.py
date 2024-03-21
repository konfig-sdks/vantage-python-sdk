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


class Product(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    # The category of the cloud product
    category: typing.Optional[str] = Field(None, alias='category')

    # The common name of the product.
    name: typing.Optional[str] = Field(None, alias='name')

    # A unique slug for the service the product belongs to.
    service_id: typing.Optional[str] = Field(None, alias='service_id')

    # A unique slug for the provider the product belongs to.
    provider_id: typing.Optional[str] = Field(None, alias='provider_id')

    # An object of metadata about the product.
    details: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
