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

from vantage_python_sdk.model.put_teams_user_tokens import PutTeamsUserTokens as PutTeamsUserTokensSchema
from vantage_python_sdk.model.put_teams_user_emails import PutTeamsUserEmails as PutTeamsUserEmailsSchema
from vantage_python_sdk.model.errors import Errors as ErrorsSchema
from vantage_python_sdk.model.put_teams_workspace_tokens import PutTeamsWorkspaceTokens as PutTeamsWorkspaceTokensSchema
from vantage_python_sdk.model.team import Team as TeamSchema
from vantage_python_sdk.model.put_teams import PutTeams as PutTeamsSchema

from vantage_python_sdk.type.put_teams_user_tokens import PutTeamsUserTokens
from vantage_python_sdk.type.put_teams import PutTeams
from vantage_python_sdk.type.team import Team
from vantage_python_sdk.type.put_teams_user_emails import PutTeamsUserEmails
from vantage_python_sdk.type.errors import Errors
from vantage_python_sdk.type.put_teams_workspace_tokens import PutTeamsWorkspaceTokens

from ...api_client import Dictionary
from vantage_python_sdk.pydantic.put_teams_user_emails import PutTeamsUserEmails as PutTeamsUserEmailsPydantic
from vantage_python_sdk.pydantic.errors import Errors as ErrorsPydantic
from vantage_python_sdk.pydantic.put_teams import PutTeams as PutTeamsPydantic
from vantage_python_sdk.pydantic.put_teams_user_tokens import PutTeamsUserTokens as PutTeamsUserTokensPydantic
from vantage_python_sdk.pydantic.team import Team as TeamPydantic
from vantage_python_sdk.pydantic.put_teams_workspace_tokens import PutTeamsWorkspaceTokens as PutTeamsWorkspaceTokensPydantic

from . import path

# Path params
TeamTokenSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'team_token': typing.Union[TeamTokenSchema, str, ],
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


request_path_team_token = api_client.PathParameter(
    name="team_token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TeamTokenSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = PutTeamsSchema


request_body_put_teams = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'oauth2',
]
SchemaFor200ResponseBodyApplicationJson = TeamSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Team


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Team


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
SchemaFor403ResponseBodyApplicationJson = ErrorsSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Errors


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Errors


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
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
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_team_mapped_args(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if workspace_tokens is not None:
            _body["workspace_tokens"] = workspace_tokens
        if user_tokens is not None:
            _body["user_tokens"] = user_tokens
        if user_emails is not None:
            _body["user_emails"] = user_emails
        if role is not None:
            _body["role"] = role
        args.body = _body
        if team_token is not None:
            _path_params["team_token"] = team_token
        args.path = _path_params
        return args

    async def _aupdate_team_oapg(
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
            request_path_team_token,
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
            path_template='/teams/{team_token}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_put_teams.serialize(body, content_type)
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


    def _update_team_oapg(
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
            request_path_team_token,
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
            path_template='/teams/{team_token}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_put_teams.serialize(body, content_type)
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


class UpdateTeamRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_team(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_team_mapped_args(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )
        return await self._aupdate_team_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_team(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_team_mapped_args(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )
        return self._update_team_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateTeam(BaseApi):

    async def aupdate_team(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TeamPydantic:
        raw_response = await self.raw.aupdate_team(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
            **kwargs,
        )
        if validate:
            return TeamPydantic(**raw_response.body)
        return api_client.construct_model_instance(TeamPydantic, raw_response.body)
    
    
    def update_team(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TeamPydantic:
        raw_response = self.raw.update_team(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )
        if validate:
            return TeamPydantic(**raw_response.body)
        return api_client.construct_model_instance(TeamPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_team_mapped_args(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )
        return await self._aupdate_team_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        team_token: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        workspace_tokens: typing.Optional[PutTeamsWorkspaceTokens] = None,
        user_tokens: typing.Optional[PutTeamsUserTokens] = None,
        user_emails: typing.Optional[PutTeamsUserEmails] = None,
        role: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_team_mapped_args(
            team_token=team_token,
            description=description,
            name=name,
            workspace_tokens=workspace_tokens,
            user_tokens=user_tokens,
            user_emails=user_emails,
            role=role,
        )
        return self._update_team_oapg(
            body=args.body,
            path_params=args.path,
        )

