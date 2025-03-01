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


class PostBusinessMetricsCostReportTokensWithMetadataItem(BaseModel):
    # The token of the CostReport the BusinessMetric is attached to.
    cost_report_token: str = Field(alias='cost_report_token')

    # Determines the scale of the BusinessMetric's values within the CostReport.
    unit_scale: typing.Optional[Literal["per_unit", "per_hundred", "per_thousand", "per_million", "per_billion"]] = Field(None, alias='unit_scale')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
