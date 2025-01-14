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


class PutBusinessMetrics(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Updates an existing BusinessMetric.
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def cost_report_tokens_with_metadata() -> typing.Type['PutBusinessMetricsCostReportTokensWithMetadata']:
                return PutBusinessMetricsCostReportTokensWithMetadata
        
            @staticmethod
            def values() -> typing.Type['PutBusinessMetricsValues']:
                return PutBusinessMetricsValues
            __annotations__ = {
                "title": title,
                "cost_report_tokens_with_metadata": cost_report_tokens_with_metadata,
                "values": values,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost_report_tokens_with_metadata"]) -> 'PutBusinessMetricsCostReportTokensWithMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["values"]) -> 'PutBusinessMetricsValues': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "cost_report_tokens_with_metadata", "values", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost_report_tokens_with_metadata"]) -> typing.Union['PutBusinessMetricsCostReportTokensWithMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["values"]) -> typing.Union['PutBusinessMetricsValues', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "cost_report_tokens_with_metadata", "values", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        cost_report_tokens_with_metadata: typing.Union['PutBusinessMetricsCostReportTokensWithMetadata', schemas.Unset] = schemas.unset,
        values: typing.Union['PutBusinessMetricsValues', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PutBusinessMetrics':
        return super().__new__(
            cls,
            *args,
            title=title,
            cost_report_tokens_with_metadata=cost_report_tokens_with_metadata,
            values=values,
            _configuration=_configuration,
            **kwargs,
        )

from vantage_python_sdk.model.put_business_metrics_cost_report_tokens_with_metadata import PutBusinessMetricsCostReportTokensWithMetadata
from vantage_python_sdk.model.put_business_metrics_values import PutBusinessMetricsValues
