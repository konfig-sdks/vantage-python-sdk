# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from vantage_python_sdk import schemas  # noqa: F401


class PostSegments(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Create a Segment.
    """


    class MetaOapg:
        required = {
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            description = schemas.StrSchema
            priority = schemas.Int32Schema
            track_unallocated = schemas.BoolSchema
        
            @staticmethod
            def report_settings() -> typing.Type['PostSegmentsReportSettings']:
                return PostSegmentsReportSettings
            workspace_token = schemas.StrSchema
            filter = schemas.StrSchema
            parent_segment_token = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "description": description,
                "priority": priority,
                "track_unallocated": track_unallocated,
                "report_settings": report_settings,
                "workspace_token": workspace_token,
                "filter": filter,
                "parent_segment_token": parent_segment_token,
            }
    
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["track_unallocated"]) -> MetaOapg.properties.track_unallocated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_settings"]) -> 'PostSegmentsReportSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_token"]) -> MetaOapg.properties.workspace_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_segment_token"]) -> MetaOapg.properties.parent_segment_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "description", "priority", "track_unallocated", "report_settings", "workspace_token", "filter", "parent_segment_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["track_unallocated"]) -> typing.Union[MetaOapg.properties.track_unallocated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_settings"]) -> typing.Union['PostSegmentsReportSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_token"]) -> typing.Union[MetaOapg.properties.workspace_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_segment_token"]) -> typing.Union[MetaOapg.properties.parent_segment_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "description", "priority", "track_unallocated", "report_settings", "workspace_token", "filter", "parent_segment_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        track_unallocated: typing.Union[MetaOapg.properties.track_unallocated, bool, schemas.Unset] = schemas.unset,
        report_settings: typing.Union['PostSegmentsReportSettings', schemas.Unset] = schemas.unset,
        workspace_token: typing.Union[MetaOapg.properties.workspace_token, str, schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        parent_segment_token: typing.Union[MetaOapg.properties.parent_segment_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostSegments':
        return super().__new__(
            cls,
            *args,
            title=title,
            description=description,
            priority=priority,
            track_unallocated=track_unallocated,
            report_settings=report_settings,
            workspace_token=workspace_token,
            filter=filter,
            parent_segment_token=parent_segment_token,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.post_segments_report_settings import PostSegmentsReportSettings