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

from vantage_python_sdk.pydantic.cost_tags import CostTags

class Cost(BaseModel):
    tags: typing.Optional[CostTags] = Field(None, alias='tags')

    links: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='links')

    # The date the cost was accrued. ISO 8601 Formatted.
    accrued_at: typing.Optional[str] = Field(None, alias='accrued_at')

    # The amount of the cost.
    amount: typing.Optional[str] = Field(None, alias='amount')

    # The currency of the cost.
    currency: typing.Optional[str] = Field(None, alias='currency')

    # The cost provider which incurred the cost.
    provider: typing.Optional[Literal["aws", "azure", "gcp", "snowflake", "databricks", "mongo", "datadog", "fastly", "new_relic", "opencost", "open_ai", "oracle", "confluent", "planetscale", "coralogix", "kubernetes"]] = Field(None, alias='provider')

    # The cost provider's billing account id that incurred the cost.
    billing_account_id: typing.Optional[str] = Field(None, alias='billing_account_id')

    # The cost provider's account id that incurred the cost.
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # The service which incurred the cost.
    service: typing.Optional[str] = Field(None, alias='service')

    # The region which incurred the cost.
    region: typing.Optional[str] = Field(None, alias='region')

    # The resource id which incurred the cost.
    resource_id: typing.Optional[str] = Field(None, alias='resource_id')

    # The tag attached to the cost that was incurred. DEPRECATED: does not support multiple tags.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # The category for the cost.
    cost_category: typing.Optional[str] = Field(None, alias='cost_category')

    # The subcategory for the cost.
    cost_subcategory: typing.Optional[str] = Field(None, alias='cost_subcategory')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
