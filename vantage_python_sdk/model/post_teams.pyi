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


class PostTeams(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Create a new Team.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def workspace_tokens() -> typing.Type['PostTeamsWorkspaceTokens']:
                return PostTeamsWorkspaceTokens
        
            @staticmethod
            def user_tokens() -> typing.Type['PostTeamsUserTokens']:
                return PostTeamsUserTokens
        
            @staticmethod
            def user_emails() -> typing.Type['PostTeamsUserEmails']:
                return PostTeamsUserEmails
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
                "name": name,
                "description": description,
                "workspace_tokens": workspace_tokens,
                "user_tokens": user_tokens,
                "user_emails": user_emails,
                "role": role,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_tokens"]) -> 'PostTeamsWorkspaceTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_tokens"]) -> 'PostTeamsUserTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_emails"]) -> 'PostTeamsUserEmails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "workspace_tokens", "user_tokens", "user_emails", "role", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_tokens"]) -> typing.Union['PostTeamsWorkspaceTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_tokens"]) -> typing.Union['PostTeamsUserTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_emails"]) -> typing.Union['PostTeamsUserEmails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "workspace_tokens", "user_tokens", "user_emails", "role", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        workspace_tokens: typing.Union['PostTeamsWorkspaceTokens', schemas.Unset] = schemas.unset,
        user_tokens: typing.Union['PostTeamsUserTokens', schemas.Unset] = schemas.unset,
        user_emails: typing.Union['PostTeamsUserEmails', schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostTeams':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.post_teams_user_emails import PostTeamsUserEmails
from vantage_python_sdk.model.post_teams_user_tokens import PostTeamsUserTokens
from vantage_python_sdk.model.post_teams_workspace_tokens import PostTeamsWorkspaceTokens