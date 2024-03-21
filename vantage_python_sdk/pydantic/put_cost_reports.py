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

from vantage_python_sdk.pydantic.put_cost_reports_business_metric_tokens_with_metadata import PutCostReportsBusinessMetricTokensWithMetadata
from vantage_python_sdk.pydantic.put_cost_reports_saved_filter_tokens import PutCostReportsSavedFilterTokens
from vantage_python_sdk.pydantic.put_cost_reports_settings import PutCostReportsSettings

class PutCostReports(BaseModel):
    # The title of the CostReport.
    title: typing.Optional[str] = Field(None, alias='title')

    # Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region
    groupings: typing.Optional[str] = Field(None, alias='groupings')

    # The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    saved_filter_tokens: typing.Optional[PutCostReportsSavedFilterTokens] = Field(None, alias='saved_filter_tokens')

    business_metric_tokens_with_metadata: typing.Optional[PutCostReportsBusinessMetricTokensWithMetadata] = Field(None, alias='business_metric_tokens_with_metadata')

    # The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.
    folder_token: typing.Optional[str] = Field(None, alias='folder_token')

    settings: typing.Optional[PutCostReportsSettings] = Field(None, alias='settings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
