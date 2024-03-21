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


class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    token: str

    # The name of the User.
    name: str

    # The email of the User.
    email: str

    # The role of the User.
    role: str

class User(RequiredUser, OptionalUser):
    pass
