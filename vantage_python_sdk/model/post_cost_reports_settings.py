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


class PostCostReportsSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Report settings.
    """


    class MetaOapg:
        
        class properties:
            include_credits = schemas.BoolSchema
            include_refunds = schemas.BoolSchema
            include_discounts = schemas.BoolSchema
            include_tax = schemas.BoolSchema
            amortize = schemas.BoolSchema
            unallocated = schemas.BoolSchema
            __annotations__ = {
                "include_credits": include_credits,
                "include_refunds": include_refunds,
                "include_discounts": include_discounts,
                "include_tax": include_tax,
                "amortize": amortize,
                "unallocated": unallocated,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_credits"]) -> MetaOapg.properties.include_credits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_refunds"]) -> MetaOapg.properties.include_refunds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_discounts"]) -> MetaOapg.properties.include_discounts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_tax"]) -> MetaOapg.properties.include_tax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amortize"]) -> MetaOapg.properties.amortize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unallocated"]) -> MetaOapg.properties.unallocated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["include_credits", "include_refunds", "include_discounts", "include_tax", "amortize", "unallocated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_credits"]) -> typing.Union[MetaOapg.properties.include_credits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_refunds"]) -> typing.Union[MetaOapg.properties.include_refunds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_discounts"]) -> typing.Union[MetaOapg.properties.include_discounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_tax"]) -> typing.Union[MetaOapg.properties.include_tax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amortize"]) -> typing.Union[MetaOapg.properties.amortize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unallocated"]) -> typing.Union[MetaOapg.properties.unallocated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["include_credits", "include_refunds", "include_discounts", "include_tax", "amortize", "unallocated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        include_credits: typing.Union[MetaOapg.properties.include_credits, bool, schemas.Unset] = schemas.unset,
        include_refunds: typing.Union[MetaOapg.properties.include_refunds, bool, schemas.Unset] = schemas.unset,
        include_discounts: typing.Union[MetaOapg.properties.include_discounts, bool, schemas.Unset] = schemas.unset,
        include_tax: typing.Union[MetaOapg.properties.include_tax, bool, schemas.Unset] = schemas.unset,
        amortize: typing.Union[MetaOapg.properties.amortize, bool, schemas.Unset] = schemas.unset,
        unallocated: typing.Union[MetaOapg.properties.unallocated, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostCostReportsSettings':
        return super().__new__(
            cls,
            *args,
            include_credits=include_credits,
            include_refunds=include_refunds,
            include_discounts=include_discounts,
            include_tax=include_tax,
            amortize=amortize,
            unallocated=unallocated,
            _configuration=_configuration,
            **kwargs,
        )
