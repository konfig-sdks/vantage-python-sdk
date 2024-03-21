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


class AccessGrant(BaseModel):
    token: typing.Optional[str] = Field(None, alias='token')

    # The token for any resource the AccessGrant is applied to.
    resource_token: typing.Optional[str] = Field(None, alias='resource_token')

    # The access status of the AccessGrant.
    access: typing.Optional[str] = Field(None, alias='access')

    # The Team token for which an AccessGrant is applied to.
    team_token: typing.Optional[str] = Field(None, alias='team_token')

    # The date and time, in UTC, the AccessGrant was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The token for the User who created the AccessGrant.
    created_by: typing.Optional[str] = Field(None, alias='created_by')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
