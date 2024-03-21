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


class PostCostReportsBusinessMetricTokensWithMetadataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "business_metric_token",
        }
        
        class properties:
            business_metric_token = schemas.StrSchema
            
            
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
                "business_metric_token": business_metric_token,
                "unit_scale": unit_scale,
            }
    
    business_metric_token: MetaOapg.properties.business_metric_token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business_metric_token"]) -> MetaOapg.properties.business_metric_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit_scale"]) -> MetaOapg.properties.unit_scale: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["business_metric_token", "unit_scale", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business_metric_token"]) -> MetaOapg.properties.business_metric_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit_scale"]) -> typing.Union[MetaOapg.properties.unit_scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["business_metric_token", "unit_scale", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        business_metric_token: typing.Union[MetaOapg.properties.business_metric_token, str, ],
        unit_scale: typing.Union[MetaOapg.properties.unit_scale, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostCostReportsBusinessMetricTokensWithMetadataItem':
        return super().__new__(
            cls,
            *args,
            business_metric_token=business_metric_token,
            unit_scale=unit_scale,
            _configuration=_configuration,
            **kwargs,
        )