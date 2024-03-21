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

from vantage_python_sdk.type.put_teams_user_emails import PutTeamsUserEmails
from vantage_python_sdk.type.put_teams_user_tokens import PutTeamsUserTokens
from vantage_python_sdk.type.put_teams_workspace_tokens import PutTeamsWorkspaceTokens

class RequiredPutTeams(TypedDict):
    pass

class OptionalPutTeams(TypedDict, total=False):
    # The description of the Team.
    description: str

    # The name of the Team.
    name: str

    workspace_tokens: PutTeamsWorkspaceTokens

    user_tokens: PutTeamsUserTokens

    user_emails: PutTeamsUserEmails

    # The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.
    role: str

class PutTeams(RequiredPutTeams, OptionalPutTeams):
    pass
