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


class PostAccessGrants(BaseModel):
    # The token of the resource for which you are granting access.
    resource_token: str = Field(alias='resource_token')

    # The token of the Team you want to grant access to.
    team_token: str = Field(alias='team_token')

    # The access level you want to grant. Defaults to 'allowed'.
    access: typing.Optional[Literal["denied", "allowed"]] = Field(None, alias='access')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
