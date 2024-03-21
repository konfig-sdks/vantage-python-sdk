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

from vantage_python_sdk.pydantic.saved_filter_cost_report_tokens import SavedFilterCostReportTokens

class SavedFilter(BaseModel):
    # The title of the SavedFilter.
    title: typing.Optional[str] = Field(None, alias='title')

    token: typing.Optional[str] = Field(None, alias='token')

    cost_report_tokens: typing.Optional[SavedFilterCostReportTokens] = Field(None, alias='cost_report_tokens')

    # The SavedFilter's filter, applied to any relevant CostReports. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    # The date and time, in UTC, the report was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The User who created the SavedFilter.
    created_by: typing.Optional[str] = Field(None, alias='created_by')

    # The token for the Workspace the SavedFilter is a part of.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
