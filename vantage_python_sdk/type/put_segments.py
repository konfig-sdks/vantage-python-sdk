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

from vantage_python_sdk.type.put_segments_report_settings import PutSegmentsReportSettings

class RequiredPutSegments(TypedDict):
    pass

class OptionalPutSegments(TypedDict, total=False):
    # The title of the Segment.
    title: str

    # The description of the Segment.
    description: str

    # The priority of the Segment.
    priority: int

    # Track Unallocated Costs which are not assigned to any of the created Segments.
    track_unallocated: bool

    report_settings: PutSegmentsReportSettings

    # The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.
    filter: str

    # The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.
    parent_segment_token: str

class PutSegments(RequiredPutSegments, OptionalPutSegments):
    pass
