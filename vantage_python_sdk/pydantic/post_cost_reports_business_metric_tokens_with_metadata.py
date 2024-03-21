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

from vantage_python_sdk.pydantic.post_cost_reports_business_metric_tokens_with_metadata_item import PostCostReportsBusinessMetricTokensWithMetadataItem

PostCostReportsBusinessMetricTokensWithMetadata = typing.List[PostCostReportsBusinessMetricTokensWithMetadataItem]