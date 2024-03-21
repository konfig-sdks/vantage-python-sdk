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


class ReportNotification(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    ReportNotification model
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            token = schemas.StrSchema
            cost_report_token = schemas.StrSchema
        
            @staticmethod
            def user_tokens() -> typing.Type['ReportNotificationUserTokens']:
                return ReportNotificationUserTokens
        
            @staticmethod
            def recipient_channels() -> typing.Type['ReportNotificationRecipientChannels']:
                return ReportNotificationRecipientChannels
            
            
            class frequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "daily": "DAILY",
                        "weekly": "WEEKLY",
                        "monthly": "MONTHLY",
                    }
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("daily")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("monthly")
            
            
            class change(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "percentage": "PERCENTAGE",
                        "dollars": "DOLLARS",
                    }
                
                @schemas.classproperty
                def PERCENTAGE(cls):
                    return cls("percentage")
                
                @schemas.classproperty
                def DOLLARS(cls):
                    return cls("dollars")
            __annotations__ = {
                "title": title,
                "token": token,
                "cost_report_token": cost_report_token,
                "user_tokens": user_tokens,
                "recipient_channels": recipient_channels,
                "frequency": frequency,
                "change": change,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost_report_token"]) -> MetaOapg.properties.cost_report_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_tokens"]) -> 'ReportNotificationUserTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_channels"]) -> 'ReportNotificationRecipientChannels': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> MetaOapg.properties.frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["change"]) -> MetaOapg.properties.change: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "token", "cost_report_token", "user_tokens", "recipient_channels", "frequency", "change", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost_report_token"]) -> typing.Union[MetaOapg.properties.cost_report_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_tokens"]) -> typing.Union['ReportNotificationUserTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_channels"]) -> typing.Union['ReportNotificationRecipientChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> typing.Union[MetaOapg.properties.frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["change"]) -> typing.Union[MetaOapg.properties.change, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "token", "cost_report_token", "user_tokens", "recipient_channels", "frequency", "change", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        token: typing.Union[MetaOapg.properties.token, str, schemas.Unset] = schemas.unset,
        cost_report_token: typing.Union[MetaOapg.properties.cost_report_token, str, schemas.Unset] = schemas.unset,
        user_tokens: typing.Union['ReportNotificationUserTokens', schemas.Unset] = schemas.unset,
        recipient_channels: typing.Union['ReportNotificationRecipientChannels', schemas.Unset] = schemas.unset,
        frequency: typing.Union[MetaOapg.properties.frequency, str, schemas.Unset] = schemas.unset,
        change: typing.Union[MetaOapg.properties.change, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportNotification':
        return super().__new__(
            cls,
            *args,
            title=title,
            token=token,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.report_notification_recipient_channels import ReportNotificationRecipientChannels
from vantage_python_sdk.model.report_notification_user_tokens import ReportNotificationUserTokens
