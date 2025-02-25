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


class PutTeams(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Update a Team.
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def workspace_tokens() -> typing.Type['PutTeamsWorkspaceTokens']:
                return PutTeamsWorkspaceTokens
        
            @staticmethod
            def user_tokens() -> typing.Type['PutTeamsUserTokens']:
                return PutTeamsUserTokens
        
            @staticmethod
            def user_emails() -> typing.Type['PutTeamsUserEmails']:
                return PutTeamsUserEmails
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "owner": "OWNER",
                        "editor": "EDITOR",
                        "viewer": "VIEWER",
                    }
                
                @schemas.classproperty
                def OWNER(cls):
                    return cls("owner")
                
                @schemas.classproperty
                def EDITOR(cls):
                    return cls("editor")
                
                @schemas.classproperty
                def VIEWER(cls):
                    return cls("viewer")
            __annotations__ = {
                "description": description,
                "name": name,
                "workspace_tokens": workspace_tokens,
                "user_tokens": user_tokens,
                "user_emails": user_emails,
                "role": role,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_tokens"]) -> 'PutTeamsWorkspaceTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_tokens"]) -> 'PutTeamsUserTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_emails"]) -> 'PutTeamsUserEmails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "workspace_tokens", "user_tokens", "user_emails", "role", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_tokens"]) -> typing.Union['PutTeamsWorkspaceTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_tokens"]) -> typing.Union['PutTeamsUserTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_emails"]) -> typing.Union['PutTeamsUserEmails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "workspace_tokens", "user_tokens", "user_emails", "role", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        workspace_tokens: typing.Union['PutTeamsWorkspaceTokens', schemas.Unset] = schemas.unset,
        user_tokens: typing.Union['PutTeamsUserTokens', schemas.Unset] = schemas.unset,
        user_emails: typing.Union['PutTeamsUserEmails', schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PutTeams':
        return super().__new__(
            cls,
            *args,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.put_teams_user_emails import PutTeamsUserEmails
from vantage_python_sdk.model.put_teams_user_tokens import PutTeamsUserTokens
from vantage_python_sdk.model.put_teams_workspace_tokens import PutTeamsWorkspaceTokens
