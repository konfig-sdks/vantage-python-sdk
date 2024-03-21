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


class User(BaseModel):
    token: typing.Optional[str] = Field(None, alias='token')

    # The name of the User.
    name: typing.Optional[str] = Field(None, alias='name')

    # The email of the User.
    email: typing.Optional[str] = Field(None, alias='email')

    # The role of the User.
    role: typing.Optional[str] = Field(None, alias='role')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
