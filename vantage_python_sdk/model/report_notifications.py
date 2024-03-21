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


class ReportNotifications(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    ReportNotifications model
    """


    class MetaOapg:
        
        class properties:
            links = schemas.DictSchema
            
            
            class report_notifications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReportNotification']:
                        return ReportNotification
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ReportNotification'], typing.List['ReportNotification']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'report_notifications':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReportNotification':
                    return super().__getitem__(i)
            __annotations__ = {
                "links": links,
                "report_notifications": report_notifications,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["report_notifications"]) -> MetaOapg.properties.report_notifications: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["links", "report_notifications", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["report_notifications"]) -> typing.Union[MetaOapg.properties.report_notifications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["links", "report_notifications", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        links: typing.Union[MetaOapg.properties.links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        report_notifications: typing.Union[MetaOapg.properties.report_notifications, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportNotifications':
        return super().__new__(
            cls,
            *args,
            links=links,
            report_notifications=report_notifications,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.report_notification import ReportNotification