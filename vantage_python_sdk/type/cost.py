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

from vantage_python_sdk.type.cost_tags import CostTags

class RequiredCost(TypedDict):
    pass

class OptionalCost(TypedDict, total=False):
    tags: CostTags

    links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The date the cost was accrued. ISO 8601 Formatted.
    accrued_at: str

    # The amount of the cost.
    amount: str

    # The currency of the cost.
    currency: str

    # The cost provider which incurred the cost.
    provider: str

    # The cost provider's billing account id that incurred the cost.
    billing_account_id: str

    # The cost provider's account id that incurred the cost.
    account_id: str

    # The service which incurred the cost.
    service: str

    # The region which incurred the cost.
    region: str

    # The resource id which incurred the cost.
    resource_id: str

    # The tag attached to the cost that was incurred. DEPRECATED: does not support multiple tags.
    tag: str

    # The category for the cost.
    cost_category: str

    # The subcategory for the cost.
    cost_subcategory: str

class Cost(RequiredCost, OptionalCost):
    pass
