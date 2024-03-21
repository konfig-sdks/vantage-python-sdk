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

from vantage_python_sdk.type.post_cost_reports_business_metric_tokens_with_metadata import PostCostReportsBusinessMetricTokensWithMetadata
from vantage_python_sdk.type.post_cost_reports_saved_filter_tokens import PostCostReportsSavedFilterTokens
from vantage_python_sdk.type.post_cost_reports_settings import PostCostReportsSettings

class RequiredPostCostReports(TypedDict):
    # The title of the CostReport.
    title: str

class OptionalPostCostReports(TypedDict, total=False):
    # The token of the Workspace to add the Cost Report to. Ignored if 'folder_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: str

    # Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region
    groupings: str

    # The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    saved_filter_tokens: PostCostReportsSavedFilterTokens

    business_metric_tokens_with_metadata: PostCostReportsBusinessMetricTokensWithMetadata

    # The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.
    folder_token: str

    settings: PostCostReportsSettings

class PostCostReports(RequiredPostCostReports, OptionalPostCostReports):
    pass
