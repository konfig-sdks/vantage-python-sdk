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

from vantage_python_sdk.pydantic.post_segments_report_settings import PostSegmentsReportSettings

class PostSegments(BaseModel):
    # The title of the Segment.
    title: str = Field(alias='title')

    # The description of the Segment.
    description: typing.Optional[str] = Field(None, alias='description')

    # The priority of the Segment.
    priority: typing.Optional[int] = Field(None, alias='priority')

    # Track Unallocated Costs which are not assigned to any of the created Segments.
    track_unallocated: typing.Optional[bool] = Field(None, alias='track_unallocated')

    report_settings: typing.Optional[PostSegmentsReportSettings] = Field(None, alias='report_settings')

    # The token of the Workspace to add the Segment to. Ignored if 'segment_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: typing.Optional[str] = Field(None, alias='workspace_token')

    # The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.
    filter: typing.Optional[str] = Field(None, alias='filter')

    # The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.
    parent_segment_token: typing.Optional[str] = Field(None, alias='parent_segment_token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
