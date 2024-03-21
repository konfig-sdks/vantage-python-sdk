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

from vantage_python_sdk.pydantic.cost_report_business_metric_tokens_with_metadata import CostReportBusinessMetricTokensWithMetadata
from vantage_python_sdk.pydantic.cost_report_saved_filter_tokens import CostReportSavedFilterTokens
from vantage_python_sdk.pydantic.cost_report_settings import CostReportSettings

class CostReport(BaseModel):
    # The title of the CostReport.
    title: typing.Optional[str] = Field(None, alias='title')

    token: typing.Optional[str] = Field(None, alias='token')

    # The token for the Folder the CostReport is a part of.
    folder_token: typing.Optional[str] = Field(None, alias='folder_token')

    saved_filter_tokens: typing.Optional[CostReportSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    business_metric_tokens_with_metadata: typing.Optional[CostReportBusinessMetricTokensWithMetadata] = Field(None, alias='business_metric_tokens_with_metadata')

    # The filter applied to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    # The grouping aggregations applied to the filtered data.
    groupings: typing.Optional[str] = Field(None, alias='groupings')

    settings: typing.Optional[CostReportSettings] = Field(None, alias='settings')

    # The date and time, in UTC, the report was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The token for the Workspace the CostReport is a part of.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
