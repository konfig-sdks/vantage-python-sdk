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

from vantage_python_sdk.type.folder_saved_filter_tokens import FolderSavedFilterTokens

class RequiredFolder(TypedDict):
    pass

class OptionalFolder(TypedDict, total=False):
    # The title of the Folder.
    title: str

    token: str

    # The token for the parent Folder, if any.
    parent_folder_token: str

    saved_filter_tokens: FolderSavedFilterTokens

    # The date and time, in UTC, the Folder was created. ISO 8601 Formatted.
    created_at: str

    # The date and time, in UTC, the Folder was last updated at. ISO 8601 Formatted.
    updated_at: str

    # The token for the Workspace the Folder is a part of.
    workspace_token: str

class Folder(RequiredFolder, OptionalFolder):
    pass
