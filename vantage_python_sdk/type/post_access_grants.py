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


class RequiredPostAccessGrants(TypedDict):
    # The token of the resource for which you are granting access.
    resource_token: str

    # The token of the Team you want to grant access to.
    team_token: str

class OptionalPostAccessGrants(TypedDict, total=False):
    # The access level you want to grant. Defaults to 'allowed'.
    access: str

class PostAccessGrants(RequiredPostAccessGrants, OptionalPostAccessGrants):
    pass
