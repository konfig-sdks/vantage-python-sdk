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

from vantage_python_sdk.pydantic.put_business_metrics_cost_report_tokens_with_metadata import PutBusinessMetricsCostReportTokensWithMetadata
from vantage_python_sdk.pydantic.put_business_metrics_values import PutBusinessMetricsValues

class PutBusinessMetrics(BaseModel):
    # The title of the BusinessMetric.
    title: typing.Optional[str] = Field(None, alias='title')

    cost_report_tokens_with_metadata: typing.Optional[PutBusinessMetricsCostReportTokensWithMetadata] = Field(None, alias='cost_report_tokens_with_metadata')

    values: typing.Optional[PutBusinessMetricsValues] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
