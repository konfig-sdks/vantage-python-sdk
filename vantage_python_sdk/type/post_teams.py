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

from vantage_python_sdk.type.post_teams_user_emails import PostTeamsUserEmails
from vantage_python_sdk.type.post_teams_user_tokens import PostTeamsUserTokens
from vantage_python_sdk.type.post_teams_workspace_tokens import PostTeamsWorkspaceTokens

class RequiredPostTeams(TypedDict):
    # The name of the Team.
    name: str

class OptionalPostTeams(TypedDict, total=False):
    # The description of the Team.
    description: str

    workspace_tokens: PostTeamsWorkspaceTokens

    user_tokens: PostTeamsUserTokens

    user_emails: PostTeamsUserEmails

    # The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.
    role: str

class PostTeams(RequiredPostTeams, OptionalPostTeams):
    pass
