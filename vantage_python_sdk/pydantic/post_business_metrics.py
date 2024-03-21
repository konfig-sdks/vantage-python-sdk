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

from vantage_python_sdk.pydantic.post_business_metrics_cost_report_tokens_with_metadata import PostBusinessMetricsCostReportTokensWithMetadata
from vantage_python_sdk.pydantic.post_business_metrics_values import PostBusinessMetricsValues

class PostBusinessMetrics(BaseModel):
    # The title of the Business Metric.
    title: str = Field(alias='title')

    cost_report_tokens_with_metadata: typing.Optional[PostBusinessMetricsCostReportTokensWithMetadata] = Field(None, alias='cost_report_tokens_with_metadata')

    values: typing.Optional[PostBusinessMetricsValues] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
