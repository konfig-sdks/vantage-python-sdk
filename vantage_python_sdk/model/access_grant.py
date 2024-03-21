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


class AccessGrant(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    AccessGrant model
    """


    class MetaOapg:
        
        class properties:
            token = schemas.StrSchema
            resource_token = schemas.StrSchema
            access = schemas.StrSchema
            team_token = schemas.StrSchema
            created_at = schemas.StrSchema
            created_by = schemas.StrSchema
            __annotations__ = {
                "token": token,
                "resource_token": resource_token,
                "access": access,
                "team_token": team_token,
                "created_at": created_at,
                "created_by": created_by,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_token"]) -> MetaOapg.properties.resource_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_token"]) -> MetaOapg.properties.team_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token", "resource_token", "access", "team_token", "created_at", "created_by", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_token"]) -> typing.Union[MetaOapg.properties.resource_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_token"]) -> typing.Union[MetaOapg.properties.team_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union[MetaOapg.properties.created_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token", "resource_token", "access", "team_token", "created_at", "created_by", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        resource_token: typing.Union[MetaOapg.properties.resource_token, str, schemas.Unset] = schemas.unset,
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        team_token: typing.Union[MetaOapg.properties.team_token, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union[MetaOapg.properties.created_by, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessGrant':
        return super().__new__(
            cls,
            *args,
            token=token,
            resource_token=resource_token,
            access=access,
            team_token=team_token,
            created_at=created_at,
            created_by=created_by,
            _configuration=_configuration,
            **kwargs,
        )
