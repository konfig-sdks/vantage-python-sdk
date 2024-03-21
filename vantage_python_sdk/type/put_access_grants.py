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


class RequiredPutAccessGrants(TypedDict):
    # Allowed or denied access to resource.
    access: str

class OptionalPutAccessGrants(TypedDict, total=False):
    pass

class PutAccessGrants(RequiredPutAccessGrants, OptionalPutAccessGrants):
    pass
