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

from vantage_python_sdk.model.errors import Errors as ErrorsSchema
from vantage_python_sdk.model.put_report_notifications_user_tokens import PutReportNotificationsUserTokens as PutReportNotificationsUserTokensSchema
from vantage_python_sdk.model.put_report_notifications import PutReportNotifications as PutReportNotificationsSchema
from vantage_python_sdk.model.put_report_notifications_recipient_channels import PutReportNotificationsRecipientChannels as PutReportNotificationsRecipientChannelsSchema
from vantage_python_sdk.model.report_notification import ReportNotification as ReportNotificationSchema

from vantage_python_sdk.type.put_report_notifications import PutReportNotifications
from vantage_python_sdk.type.put_report_notifications_user_tokens import PutReportNotificationsUserTokens
from vantage_python_sdk.type.put_report_notifications_recipient_channels import PutReportNotificationsRecipientChannels
from vantage_python_sdk.type.report_notification import ReportNotification
from vantage_python_sdk.type.errors import Errors

from ...api_client import Dictionary
from vantage_python_sdk.pydantic.errors import Errors as ErrorsPydantic
from vantage_python_sdk.pydantic.put_report_notifications import PutReportNotifications as PutReportNotificationsPydantic
from vantage_python_sdk.pydantic.put_report_notifications_recipient_channels import PutReportNotificationsRecipientChannels as PutReportNotificationsRecipientChannelsPydantic
from vantage_python_sdk.pydantic.report_notification import ReportNotification as ReportNotificationPydantic
from vantage_python_sdk.pydantic.put_report_notifications_user_tokens import PutReportNotificationsUserTokens as PutReportNotificationsUserTokensPydantic

# Path params
ReportNotificationTokenSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'report_notification_token': typing.Union[ReportNotificationTokenSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_report_notification_token = api_client.PathParameter(
    name="report_notification_token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ReportNotificationTokenSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PutReportNotificationsSchema


request_body_put_report_notifications = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ReportNotificationSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReportNotification


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReportNotification


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorsSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Errors


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Errors


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorsSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Errors


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Errors


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_report_notification_mapped_args(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if title is not None:
            _body["title"] = title
        if cost_report_token is not None:
            _body["cost_report_token"] = cost_report_token
        if user_tokens is not None:
            _body["user_tokens"] = user_tokens
        if recipient_channels is not None:
            _body["recipient_channels"] = recipient_channels
        if frequency is not None:
            _body["frequency"] = frequency
        if change is not None:
            _body["change"] = change
        args.body = _body
        if report_notification_token is not None:
            _path_params["report_notification_token"] = report_notification_token
        args.path = _path_params
        return args

    async def _aupdate_report_notification_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_notification_token,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/report_notifications/{report_notification_token}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_put_report_notifications.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_report_notification_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
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
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_report_notification_token,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/report_notifications/{report_notification_token}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_put_report_notifications.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateReportNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_report_notification(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_report_notification_mapped_args(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )
        return await self._aupdate_report_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_report_notification(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_report_notification_mapped_args(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )
        return self._update_report_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateReportNotification(BaseApi):

    async def aupdate_report_notification(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportNotificationPydantic:
        raw_response = await self.raw.aupdate_report_notification(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
            **kwargs,
        )
        if validate:
            return ReportNotificationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportNotificationPydantic, raw_response.body)
    
    
    def update_report_notification(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ReportNotificationPydantic:
        raw_response = self.raw.update_report_notification(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )
        if validate:
            return ReportNotificationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportNotificationPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_report_notification_mapped_args(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )
        return await self._aupdate_report_notification_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        report_notification_token: str,
        title: typing.Optional[str] = None,
        cost_report_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PutReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PutReportNotificationsRecipientChannels] = None,
        frequency: typing.Optional[str] = None,
        change: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_report_notification_mapped_args(
            report_notification_token=report_notification_token,
            title=title,
            cost_report_token=cost_report_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            frequency=frequency,
            change=change,
        )
        return self._update_report_notification_oapg(
            body=args.body,
            path_params=args.path,
        )

