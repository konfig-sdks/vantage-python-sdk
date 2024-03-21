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


class PostAccessGrants(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Create an Access Grant.
    """


    class MetaOapg:
        required = {
            "team_token",
            "resource_token",
        }
        
        class properties:
            resource_token = schemas.StrSchema
            team_token = schemas.StrSchema
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "denied": "DENIED",
                        "allowed": "ALLOWED",
                    }
                
                @schemas.classproperty
                def DENIED(cls):
                    return cls("denied")
                
                @schemas.classproperty
                def ALLOWED(cls):
                    return cls("allowed")
            __annotations__ = {
                "resource_token": resource_token,
                "team_token": team_token,
                "access": access,
            }
    
    team_token: MetaOapg.properties.team_token
    resource_token: MetaOapg.properties.resource_token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_token"]) -> MetaOapg.properties.resource_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_token"]) -> MetaOapg.properties.team_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_token", "team_token", "access", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_token"]) -> MetaOapg.properties.resource_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_token"]) -> MetaOapg.properties.team_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_token", "team_token", "access", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        team_token: typing.Union[MetaOapg.properties.team_token, str, ],
        resource_token: typing.Union[MetaOapg.properties.resource_token, str, ],
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostAccessGrants':
        return super().__new__(
            cls,
            *args,
            team_token=team_token,
            resource_token=resource_token,
            access=access,
            _configuration=_configuration,
            **kwargs,
        )