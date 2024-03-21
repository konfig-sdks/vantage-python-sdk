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

from vantage_python_sdk.model.post_report_notifications import PostReportNotifications as PostReportNotificationsSchema
from vantage_python_sdk.model.errors import Errors as ErrorsSchema
from vantage_python_sdk.model.post_report_notifications_recipient_channels import PostReportNotificationsRecipientChannels as PostReportNotificationsRecipientChannelsSchema
from vantage_python_sdk.model.report_notification import ReportNotification as ReportNotificationSchema
from vantage_python_sdk.model.post_report_notifications_user_tokens import PostReportNotificationsUserTokens as PostReportNotificationsUserTokensSchema

from vantage_python_sdk.type.post_report_notifications_recipient_channels import PostReportNotificationsRecipientChannels
from vantage_python_sdk.type.post_report_notifications import PostReportNotifications
from vantage_python_sdk.type.report_notification import ReportNotification
from vantage_python_sdk.type.post_report_notifications_user_tokens import PostReportNotificationsUserTokens
from vantage_python_sdk.type.errors import Errors

from ...api_client import Dictionary
from vantage_python_sdk.pydantic.errors import Errors as ErrorsPydantic
from vantage_python_sdk.pydantic.post_report_notifications import PostReportNotifications as PostReportNotificationsPydantic
from vantage_python_sdk.pydantic.report_notification import ReportNotification as ReportNotificationPydantic
from vantage_python_sdk.pydantic.post_report_notifications_recipient_channels import PostReportNotificationsRecipientChannels as PostReportNotificationsRecipientChannelsPydantic
from vantage_python_sdk.pydantic.post_report_notifications_user_tokens import PostReportNotificationsUserTokens as PostReportNotificationsUserTokensPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = PostReportNotificationsSchema


request_body_post_report_notifications = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
]
SchemaFor201ResponseBodyApplicationJson = ReportNotificationSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: ReportNotification


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: ReportNotification


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
SchemaFor422ResponseBodyApplicationJson = ErrorsSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: Errors


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: Errors


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_report_notification_mapped_args(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if title is not None:
            _body["title"] = title
        if cost_report_token is not None:
            _body["cost_report_token"] = cost_report_token
        if workspace_token is not None:
            _body["workspace_token"] = workspace_token
        if user_tokens is not None:
            _body["user_tokens"] = user_tokens
        if recipient_channels is not None:
            _body["recipient_channels"] = recipient_channels
        if frequency is not None:
            _body["frequency"] = frequency
        if change is not None:
            _body["change"] = change
        args.body = _body
        return args

    async def _acreate_report_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/report_notifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_post_report_notifications.serialize(body, content_type)
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


    def _create_report_notification_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
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
            path_template='/report_notifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_post_report_notifications.serialize(body, content_type)
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


class CreateReportNotificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_report_notification(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_report_notification_mapped_args(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )
        return await self._acreate_report_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_report_notification(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_report_notification_mapped_args(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )
        return self._create_report_notification_oapg(
            body=args.body,
        )

class CreateReportNotification(BaseApi):

    async def acreate_report_notification(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportNotificationPydantic:
        raw_response = await self.raw.acreate_report_notification(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
            **kwargs,
        )
        if validate:
            return ReportNotificationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportNotificationPydantic, raw_response.body)
    
    
    def create_report_notification(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
        validate: bool = False,
    ) -> ReportNotificationPydantic:
        raw_response = self.raw.create_report_notification(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )
        if validate:
            return ReportNotificationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportNotificationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_report_notification_mapped_args(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )
        return await self._acreate_report_notification_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        title: str,
        cost_report_token: str,
        frequency: str,
        change: str,
        workspace_token: typing.Optional[str] = None,
        user_tokens: typing.Optional[PostReportNotificationsUserTokens] = None,
        recipient_channels: typing.Optional[PostReportNotificationsRecipientChannels] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_report_notification_mapped_args(
            title=title,
            cost_report_token=cost_report_token,
            frequency=frequency,
            change=change,
            workspace_token=workspace_token,
            user_tokens=user_tokens,
            recipient_channels=recipient_channels,
        )
        return self._create_report_notification_oapg(
            body=args.body,
        )
