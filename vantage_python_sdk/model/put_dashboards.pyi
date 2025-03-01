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


class PutDashboards(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Update a Dashboard.
    """


    class MetaOapg:
        required = {
            "end_date",
        }
        
        class properties:
            end_date = schemas.StrSchema
            title = schemas.StrSchema
        
            @staticmethod
            def widget_tokens() -> typing.Type['PutDashboardsWidgetTokens']:
                return PutDashboardsWidgetTokens
        
            @staticmethod
            def saved_filter_tokens() -> typing.Type['PutDashboardsSavedFilterTokens']:
                return PutDashboardsSavedFilterTokens
            
            
            class date_bin(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CUMULATIVE(cls):
                    return cls("cumulative")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("day")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("week")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("month")
            
            
            class date_interval(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def THIS_MONTH(cls):
                    return cls("this_month")
                
                @schemas.classproperty
                def LAST_7_DAYS(cls):
                    return cls("last_7_days")
                
                @schemas.classproperty
                def LAST_30_DAYS(cls):
                    return cls("last_30_days")
                
                @schemas.classproperty
                def LAST_MONTH(cls):
                    return cls("last_month")
                
                @schemas.classproperty
                def LAST_3_MONTHS(cls):
                    return cls("last_3_months")
                
                @schemas.classproperty
                def LAST_6_MONTHS(cls):
                    return cls("last_6_months")
                
                @schemas.classproperty
                def CUSTOM(cls):
                    return cls("custom")
                
                @schemas.classproperty
                def LAST_12_MONTHS(cls):
                    return cls("last_12_months")
                
                @schemas.classproperty
                def LAST_24_MONTHS(cls):
                    return cls("last_24_months")
                
                @schemas.classproperty
                def LAST_36_MONTHS(cls):
                    return cls("last_36_months")
                
                @schemas.classproperty
                def NEXT_MONTH(cls):
                    return cls("next_month")
                
                @schemas.classproperty
                def NEXT_3_MONTHS(cls):
                    return cls("next_3_months")
                
                @schemas.classproperty
                def NEXT_6_MONTHS(cls):
                    return cls("next_6_months")
                
                @schemas.classproperty
                def NEXT_12_MONTHS(cls):
                    return cls("next_12_months")
            start_date = schemas.StrSchema
            __annotations__ = {
                "end_date": end_date,
                "title": title,
                "widget_tokens": widget_tokens,
                "saved_filter_tokens": saved_filter_tokens,
                "date_bin": date_bin,
                "date_interval": date_interval,
                "start_date": start_date,
            }
    
    end_date: MetaOapg.properties.end_date
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widget_tokens"]) -> 'PutDashboardsWidgetTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["saved_filter_tokens"]) -> 'PutDashboardsSavedFilterTokens': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_bin"]) -> MetaOapg.properties.date_bin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_interval"]) -> MetaOapg.properties.date_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["end_date", "title", "widget_tokens", "saved_filter_tokens", "date_bin", "date_interval", "start_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widget_tokens"]) -> typing.Union['PutDashboardsWidgetTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["saved_filter_tokens"]) -> typing.Union['PutDashboardsSavedFilterTokens', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_bin"]) -> typing.Union[MetaOapg.properties.date_bin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_interval"]) -> typing.Union[MetaOapg.properties.date_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["end_date", "title", "widget_tokens", "saved_filter_tokens", "date_bin", "date_interval", "start_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        end_date: typing.Union[MetaOapg.properties.end_date, str, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        widget_tokens: typing.Union['PutDashboardsWidgetTokens', schemas.Unset] = schemas.unset,
        saved_filter_tokens: typing.Union['PutDashboardsSavedFilterTokens', schemas.Unset] = schemas.unset,
        date_bin: typing.Union[MetaOapg.properties.date_bin, str, schemas.Unset] = schemas.unset,
        date_interval: typing.Union[MetaOapg.properties.date_interval, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PutDashboards':
        return super().__new__(
            cls,
            *args,
            end_date=end_date,
            title=title,
            widget_tokens=widget_tokens,
            saved_filter_tokens=saved_filter_tokens,
            date_bin=date_bin,
            date_interval=date_interval,
            start_date=start_date,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.put_dashboards_saved_filter_tokens import PutDashboardsSavedFilterTokens
from vantage_python_sdk.model.put_dashboards_widget_tokens import PutDashboardsWidgetTokens
