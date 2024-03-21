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

from vantage_python_sdk.pydantic.folder_saved_filter_tokens import FolderSavedFilterTokens

class Folder(BaseModel):
    # The title of the Folder.
    title: typing.Optional[str] = Field(None, alias='title')

    token: typing.Optional[str] = Field(None, alias='token')

    # The token for the parent Folder, if any.
    parent_folder_token: typing.Optional[str] = Field(None, alias='parent_folder_token')

    saved_filter_tokens: typing.Optional[FolderSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    # The date and time, in UTC, the Folder was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The date and time, in UTC, the Folder was last updated at. ISO 8601 Formatted.
    updated_at: typing.Optional[str] = Field(None, alias='updated_at')

    # The token for the Workspace the Folder is a part of.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
