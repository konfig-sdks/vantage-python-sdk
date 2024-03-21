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

from vantage_python_sdk.type.post_segments_report_settings import PostSegmentsReportSettings

class RequiredPostSegments(TypedDict):
    # The title of the Segment.
    title: str

class OptionalPostSegments(TypedDict, total=False):
    # The description of the Segment.
    description: str

    # The priority of the Segment.
    priority: int

    # Track Unallocated Costs which are not assigned to any of the created Segments.
    track_unallocated: bool

    report_settings: PostSegmentsReportSettings

    # The token of the Workspace to add the Segment to. Ignored if 'segment_token' is set. Required if the API token is associated with multiple Workspaces.
    workspace_token: str

    # The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    # The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.
    parent_segment_token: str

class PostSegments(RequiredPostSegments, OptionalPostSegments):
    pass
