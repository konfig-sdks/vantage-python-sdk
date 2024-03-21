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


class RequiredPutSavedFilters(TypedDict):
    pass

class OptionalPutSavedFilters(TypedDict, total=False):
    # The title of the SavedFilter.
    title: str

    # The filter query language to apply to the SavedFilter, which subsequently gets applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

class PutSavedFilters(RequiredPutSavedFilters, OptionalPutSavedFilters):
    pass
