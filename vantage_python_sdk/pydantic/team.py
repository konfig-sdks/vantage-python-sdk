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

from vantage_python_sdk.pydantic.team_user_emails import TeamUserEmails
from vantage_python_sdk.pydantic.team_user_tokens import TeamUserTokens
from vantage_python_sdk.pydantic.team_workspace_tokens import TeamWorkspaceTokens

class Team(BaseModel):
    # The description of the Team.
    description: typing.Optional[str] = Field(None, alias='description')

    token: typing.Optional[str] = Field(None, alias='token')

    # The name of the Team.
    name: typing.Optional[str] = Field(None, alias='name')

    workspace_tokens: typing.Optional[TeamWorkspaceTokens] = Field(None, alias='workspace_tokens')

    user_emails: typing.Optional[TeamUserEmails] = Field(None, alias='user_emails')

    user_tokens: typing.Optional[TeamUserTokens] = Field(None, alias='user_tokens')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
