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


class RequiredProduct(TypedDict):
    pass

class OptionalProduct(TypedDict, total=False):
    id: str

    # The category of the cloud product
    category: str

    # The common name of the product.
    name: str

    # A unique slug for the service the product belongs to.
    service_id: str

    # A unique slug for the provider the product belongs to.
    provider_id: str

    # An object of metadata about the product.
    details: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class Product(RequiredProduct, OptionalProduct):
    pass
