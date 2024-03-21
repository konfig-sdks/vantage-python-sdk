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

from vantage_python_sdk.type.post_folders_saved_filter_tokens import PostFoldersSavedFilterTokens

class RequiredPostFolders(TypedDict):
    # The title of the Folder.
    title: str

class OptionalPostFolders(TypedDict, total=False):
    # The token of the parent Folder.
    parent_folder_token: str

    saved_filter_tokens: PostFoldersSavedFilterTokens

    # The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: str

class PostFolders(RequiredPostFolders, OptionalPostFolders):
    pass
