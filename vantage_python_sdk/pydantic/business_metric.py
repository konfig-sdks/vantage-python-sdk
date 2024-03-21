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

from vantage_python_sdk.pydantic.business_metric_cost_report_tokens_with_metadata import BusinessMetricCostReportTokensWithMetadata
from vantage_python_sdk.pydantic.business_metric_values import BusinessMetricValues

class BusinessMetric(BaseModel):
    # The title of the BusinessMetric.
    title: typing.Optional[str] = Field(None, alias='title')

    # The token of the BusinessMetric.
    token: typing.Optional[str] = Field(None, alias='token')

    # The token of the User who created the BusinessMetric.
    created_by_token: typing.Optional[str] = Field(None, alias='created_by_token')

    cost_report_tokens_with_metadata: typing.Optional[BusinessMetricCostReportTokensWithMetadata] = Field(None, alias='cost_report_tokens_with_metadata')

    values: typing.Optional[BusinessMetricValues] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
