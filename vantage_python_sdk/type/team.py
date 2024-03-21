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

from vantage_python_sdk.type.team_user_emails import TeamUserEmails
from vantage_python_sdk.type.team_user_tokens import TeamUserTokens
from vantage_python_sdk.type.team_workspace_tokens import TeamWorkspaceTokens

class RequiredTeam(TypedDict):
    pass

class OptionalTeam(TypedDict, total=False):
    # The description of the Team.
    description: str

    token: str

    # The name of the Team.
    name: str

    workspace_tokens: TeamWorkspaceTokens

    user_emails: TeamUserEmails

    user_tokens: TeamUserTokens

class Team(RequiredTeam, OptionalTeam):
    pass
