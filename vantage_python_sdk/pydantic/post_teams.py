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

from vantage_python_sdk.pydantic.post_teams_user_emails import PostTeamsUserEmails
from vantage_python_sdk.pydantic.post_teams_user_tokens import PostTeamsUserTokens
from vantage_python_sdk.pydantic.post_teams_workspace_tokens import PostTeamsWorkspaceTokens

class PostTeams(BaseModel):
    # The name of the Team.
    name: str = Field(alias='name')

    # The description of the Team.
    description: typing.Optional[str] = Field(None, alias='description')

    workspace_tokens: typing.Optional[PostTeamsWorkspaceTokens] = Field(None, alias='workspace_tokens')

    user_tokens: typing.Optional[PostTeamsUserTokens] = Field(None, alias='user_tokens')

    user_emails: typing.Optional[PostTeamsUserEmails] = Field(None, alias='user_emails')

    # The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.
    role: typing.Optional[Literal["owner", "editor", "viewer"]] = Field(None, alias='role')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
