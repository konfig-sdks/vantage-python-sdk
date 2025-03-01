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


class PutBusinessMetricsCostReportTokensWithMetadataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cost_report_token",
        }
        
        class properties:
            cost_report_token = schemas.StrSchema
            
            
            class unit_scale(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UNIT(cls):
                    return cls("per_unit")
                
                @schemas.classproperty
                def HUNDRED(cls):
                    return cls("per_hundred")
                
                @schemas.classproperty
                def THOUSAND(cls):
                    return cls("per_thousand")
                
                @schemas.classproperty
                def MILLION(cls):
                    return cls("per_million")
                
                @schemas.classproperty
                def BILLION(cls):
                    return cls("per_billion")
            __annotations__ = {
                "cost_report_token": cost_report_token,
                "unit_scale": unit_scale,
            }
    
    cost_report_token: MetaOapg.properties.cost_report_token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost_report_token"]) -> MetaOapg.properties.cost_report_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit_scale"]) -> MetaOapg.properties.unit_scale: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cost_report_token", "unit_scale", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost_report_token"]) -> MetaOapg.properties.cost_report_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit_scale"]) -> typing.Union[MetaOapg.properties.unit_scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cost_report_token", "unit_scale", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cost_report_token: typing.Union[MetaOapg.properties.cost_report_token, str, ],
        unit_scale: typing.Union[MetaOapg.properties.unit_scale, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PutBusinessMetricsCostReportTokensWithMetadataItem':
        return super().__new__(
            cls,
            *args,
            cost_report_token=cost_report_token,
            unit_scale=unit_scale,
            _configuration=_configuration,
            **kwargs,
        )
