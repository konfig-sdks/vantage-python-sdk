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


class RequiredAccessGrant(TypedDict):
    pass

class OptionalAccessGrant(TypedDict, total=False):
    token: str

    # The token for any resource the AccessGrant is applied to.
    resource_token: str

    # The access status of the AccessGrant.
    access: str

    # The Team token for which an AccessGrant is applied to.
    team_token: str

    # The date and time, in UTC, the AccessGrant was created. ISO 8601 Formatted.
    created_at: str

    # The token for the User who created the AccessGrant.
    created_by: str

class AccessGrant(RequiredAccessGrant, OptionalAccessGrant):
    pass
