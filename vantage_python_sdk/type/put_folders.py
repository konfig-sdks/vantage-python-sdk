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

from vantage_python_sdk.type.put_folders_saved_filter_tokens import PutFoldersSavedFilterTokens

class RequiredPutFolders(TypedDict):
    pass

class OptionalPutFolders(TypedDict, total=False):
    # The title of the Folder.
    title: str

    # The token of the parent Folder.
    parent_folder_token: str

    saved_filter_tokens: PutFoldersSavedFilterTokens

class PutFolders(RequiredPutFolders, OptionalPutFolders):
    pass
