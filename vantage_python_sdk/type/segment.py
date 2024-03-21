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

from vantage_python_sdk.type.segment_report_settings import SegmentReportSettings

class RequiredSegment(TypedDict):
    pass

class OptionalSegment(TypedDict, total=False):
    # The title of the Segment.
    title: str

    # The description of the Segment.
    description: str

    token: str

    # The token of the parent Segment of this Segment.
    parent_segment_token: str

    # Track Unallocated Costs which are not assigned to any of the created Segments.
    track_unallocated: bool

    report_settings: SegmentReportSettings

    # Costs are assigned in priority order across all Segments with assigned filters.
    priority: int

    # The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    # The date and time, in UTC, the Segment was created. ISO 8601 Formatted.
    created_at: str

    # The token for the Workspace the Segment is a part of.
    workspace_token: str

class Segment(RequiredSegment, OptionalSegment):
    pass
