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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from vantage_python_sdk.pydantic.post_folders_saved_filter_tokens import PostFoldersSavedFilterTokens

class PostFolders(BaseModel):
    # The title of the Folder.
    title: str = Field(alias='title')

    # The token of the parent Folder.
    parent_folder_token: typing.Optional[str] = Field(None, alias='parent_folder_token')

    saved_filter_tokens: typing.Optional[PostFoldersSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    # The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
