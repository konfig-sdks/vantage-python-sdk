# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from vantage_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from vantage_python_sdk.api_response import AsyncGeneratorResponse
from vantage_python_sdk import api_client, exceptions
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

from vantage_python_sdk.model.products import Products as ProductsSchema

from vantage_python_sdk.type.products import Products

from ...api_client import Dictionary
from vantage_python_sdk.pydantic.products import Products as ProductsPydantic

# Query params
ProviderIdSchema = schemas.StrSchema
ServiceIdSchema = schemas.StrSchema
NameSchema = schemas.StrSchema
PageSchema = schemas.Int32Schema
LimitSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'provider_id': typing.Union[ProviderIdSchema, str, ],
        'service_id': typing.Union[ServiceIdSchema, str, ],
        'name': typing.Union[NameSchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_provider_id = api_client.QueryParameter(
    name="provider_id",
    style=api_client.ParameterStyle.FORM,
    schema=ProviderIdSchema,
    explode=True,
)
request_query_service_id = api_client.QueryParameter(
    name="service_id",
    style=api_client.ParameterStyle.FORM,
    schema=ServiceIdSchema,
    explode=True,
)
request_query_name = api_client.QueryParameter(
    name="name",
    style=api_client.ParameterStyle.FORM,
    schema=NameSchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ProductsSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Products


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Products


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_available_products_mapped_args(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if provider_id is not None:
            _query_params["provider_id"] = provider_id
        if service_id is not None:
            _query_params["service_id"] = service_id
        if name is not None:
            _query_params["name"] = name
        if page is not None:
            _query_params["page"] = page
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _alist_available_products_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_provider_id,
            request_query_service_id,
            request_query_name,
            request_query_page,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/products',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_available_products_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_provider_id,
            request_query_service_id,
            request_query_name,
            request_query_page,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/products',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAvailableProductsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_available_products(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_products_mapped_args(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
        return await self._alist_available_products_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_available_products(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_products_mapped_args(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
        return self._list_available_products_oapg(
            query_params=args.query,
        )

class ListAvailableProducts(BaseApi):

    async def alist_available_products(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProductsPydantic:
        raw_response = await self.raw.alist_available_products(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
            **kwargs,
        )
        if validate:
            return ProductsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductsPydantic, raw_response.body)
    
    
    def list_available_products(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> ProductsPydantic:
        raw_response = self.raw.list_available_products(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
        if validate:
            return ProductsPydantic(**raw_response.body)
        return api_client.construct_model_instance(ProductsPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_available_products_mapped_args(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
        return await self._alist_available_products_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        provider_id: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_available_products_mapped_args(
            provider_id=provider_id,
            service_id=service_id,
            name=name,
            page=page,
            limit=limit,
        )
        return self._list_available_products_oapg(
            query_params=args.query,
        )

