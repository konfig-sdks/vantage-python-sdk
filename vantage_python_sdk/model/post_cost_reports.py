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


class PostCostReports(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Create a CostReport.
    """


    class MetaOapg:
        required = {
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            workspace_token = schemas.StrSchema
            groupings = schemas.StrSchema
            filter = schemas.StrSchema
        
            @staticmethod
            def saved_filter_tokens() -> typing.Type['PostCostReportsSavedFilterTokens']:
                return PostCostReportsSavedFilterTokens
        
            @staticmethod
            def business_metric_tokens_with_metadata() -> typing.Type['PostCostReportsBusinessMetricTokensWithMetadata']:
                return PostCostReportsBusinessMetricTokensWithMetadata
            folder_token = schemas.StrSchema
        
            @staticmethod
            def settings() -> typing.Type['PostCostReportsSettings']:
                return PostCostReportsSettings
            __annotations__ = {
                "title": title,
                "workspace_token": workspace_token,
                "groupings": groupings,
                "filter": filter,
                "saved_filter_tokens": saved_filter_tokens,
                "business_metric_tokens_with_metadata": business_metric_tokens_with_metadata,
                "folder_token": folder_token,
                "settings": settings,
            }
    
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_token"]) -> MetaOapg.properties.workspace_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupings"]) -> MetaOapg.properties.groupings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saved_filter_tokens"]) -> 'PostCostReportsSavedFilterTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business_metric_tokens_with_metadata"]) -> 'PostCostReportsBusinessMetricTokensWithMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["folder_token"]) -> MetaOapg.properties.folder_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'PostCostReportsSettings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "workspace_token", "groupings", "filter", "saved_filter_tokens", "business_metric_tokens_with_metadata", "folder_token", "settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_token"]) -> typing.Union[MetaOapg.properties.workspace_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupings"]) -> typing.Union[MetaOapg.properties.groupings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saved_filter_tokens"]) -> typing.Union['PostCostReportsSavedFilterTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business_metric_tokens_with_metadata"]) -> typing.Union['PostCostReportsBusinessMetricTokensWithMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["folder_token"]) -> typing.Union[MetaOapg.properties.folder_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['PostCostReportsSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "workspace_token", "groupings", "filter", "saved_filter_tokens", "business_metric_tokens_with_metadata", "folder_token", "settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        workspace_token: typing.Union[MetaOapg.properties.workspace_token, str, schemas.Unset] = schemas.unset,
        groupings: typing.Union[MetaOapg.properties.groupings, str, schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        saved_filter_tokens: typing.Union['PostCostReportsSavedFilterTokens', schemas.Unset] = schemas.unset,
        business_metric_tokens_with_metadata: typing.Union['PostCostReportsBusinessMetricTokensWithMetadata', schemas.Unset] = schemas.unset,
        folder_token: typing.Union[MetaOapg.properties.folder_token, str, schemas.Unset] = schemas.unset,
        settings: typing.Union['PostCostReportsSettings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostCostReports':
        return super().__new__(
            cls,
            *args,
            title=title,
            workspace_token=workspace_token,
            groupings=groupings,
            filter=filter,
            saved_filter_tokens=saved_filter_tokens,
            business_metric_tokens_with_metadata=business_metric_tokens_with_metadata,
            folder_token=folder_token,
            settings=settings,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.post_cost_reports_business_metric_tokens_with_metadata import PostCostReportsBusinessMetricTokensWithMetadata
from vantage_python_sdk.model.post_cost_reports_saved_filter_tokens import PostCostReportsSavedFilterTokens
from vantage_python_sdk.model.post_cost_reports_settings import PostCostReportsSettings