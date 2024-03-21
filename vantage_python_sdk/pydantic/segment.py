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

from vantage_python_sdk.pydantic.segment_report_settings import SegmentReportSettings

class Segment(BaseModel):
    # The title of the Segment.
    title: typing.Optional[str] = Field(None, alias='title')

    # The description of the Segment.
    description: typing.Optional[str] = Field(None, alias='description')

    token: typing.Optional[str] = Field(None, alias='token')

    # The token of the parent Segment of this Segment.
    parent_segment_token: typing.Optional[str] = Field(None, alias='parent_segment_token')

    # Track Unallocated Costs which are not assigned to any of the created Segments.
    track_unallocated: typing.Optional[bool] = Field(None, alias='track_unallocated')

    report_settings: typing.Optional[SegmentReportSettings] = Field(None, alias='report_settings')

    # Costs are assigned in priority order across all Segments with assigned filters.
    priority: typing.Optional[int] = Field(None, alias='priority')

    # The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    # The date and time, in UTC, the Segment was created. ISO 8601 Formatted.
    created_at: typing.Optional[str] = Field(None, alias='created_at')

    # The token for the Workspace the Segment is a part of.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
