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


class SavedFilter(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    SavedFilter model
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            token = schemas.StrSchema
        
            @staticmethod
            def cost_report_tokens() -> typing.Type['SavedFilterCostReportTokens']:
                return SavedFilterCostReportTokens
            filter = schemas.StrSchema
            created_at = schemas.StrSchema
            created_by = schemas.StrSchema
            workspace_token = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "token": token,
                "cost_report_tokens": cost_report_tokens,
                "filter": filter,
                "created_at": created_at,
                "created_by": created_by,
                "workspace_token": workspace_token,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost_report_tokens"]) -> 'SavedFilterCostReportTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> MetaOapg.properties.filter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_token"]) -> MetaOapg.properties.workspace_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "token", "cost_report_tokens", "filter", "created_at", "created_by", "workspace_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost_report_tokens"]) -> typing.Union['SavedFilterCostReportTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union[MetaOapg.properties.filter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_token"]) -> typing.Union[MetaOapg.properties.workspace_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "token", "cost_report_tokens", "filter", "created_at", "created_by", "workspace_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        cost_report_tokens: typing.Union['SavedFilterCostReportTokens', schemas.Unset] = schemas.unset,
        filter: typing.Union[MetaOapg.properties.filter, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union[MetaOapg.properties.created_by, str, schemas.Unset] = schemas.unset,
        workspace_token: typing.Union[MetaOapg.properties.workspace_token, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SavedFilter':
        return super().__new__(
            cls,
            *args,
            title=title,
            token=token,
            cost_report_tokens=cost_report_tokens,
            filter=filter,
            created_at=created_at,
            created_by=created_by,
            workspace_token=workspace_token,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.saved_filter_cost_report_tokens import SavedFilterCostReportTokens
