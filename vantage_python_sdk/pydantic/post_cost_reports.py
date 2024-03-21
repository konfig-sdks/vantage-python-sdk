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

from vantage_python_sdk.pydantic.post_cost_reports_business_metric_tokens_with_metadata import PostCostReportsBusinessMetricTokensWithMetadata
from vantage_python_sdk.pydantic.post_cost_reports_saved_filter_tokens import PostCostReportsSavedFilterTokens
from vantage_python_sdk.pydantic.post_cost_reports_settings import PostCostReportsSettings

class PostCostReports(BaseModel):
    # The title of the CostReport.
    title: str = Field(alias='title')

    # The token of the Workspace to add the Cost Report to. Ignored if 'folder_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    # Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region
    groupings: typing.Optional[str] = Field(None, alias='groupings')

    # The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    saved_filter_tokens: typing.Optional[PostCostReportsSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    business_metric_tokens_with_metadata: typing.Optional[PostCostReportsBusinessMetricTokensWithMetadata] = Field(None, alias='business_metric_tokens_with_metadata')

    # The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.
    folder_token: typing.Optional[str] = Field(None, alias='folder_token')

    settings: typing.Optional[PostCostReportsSettings] = Field(None, alias='settings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
