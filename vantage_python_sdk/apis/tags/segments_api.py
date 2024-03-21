# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from vantage_python_sdk.paths.segments.post import CreateSegment
from vantage_python_sdk.paths.segments_segment_token.get import GetSegmentById
from vantage_python_sdk.paths.segments.get import List
from vantage_python_sdk.paths.segments_segment_token.delete import RemoveSegment
from vantage_python_sdk.paths.segments_segment_token.put import UpdateSegmentById
from vantage_python_sdk.apis.tags.segments_api_raw import SegmentsApiRaw


class SegmentsApi(
    CreateSegment,
    GetSegmentById,
    List,
    RemoveSegment,
    UpdateSegmentById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SegmentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SegmentsApiRaw(api_client)
