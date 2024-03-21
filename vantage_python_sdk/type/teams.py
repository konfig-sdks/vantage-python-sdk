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

from vantage_python_sdk.type.team import Team

class RequiredTeams(TypedDict):
    pass

class OptionalTeams(TypedDict, total=False):
    links: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    teams: typing.List[Team]

class Teams(RequiredTeams, OptionalTeams):
    pass