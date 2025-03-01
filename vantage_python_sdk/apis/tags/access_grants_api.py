# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from vantage_python_sdk.paths.access_grants.post import CreateGrant
from vantage_python_sdk.paths.access_grants_access_grant_token.delete import Delete
from vantage_python_sdk.paths.access_grants_access_grant_token.get import GetSpecificGrant
from vantage_python_sdk.paths.access_grants.get import ListAccessible
from vantage_python_sdk.paths.access_grants_access_grant_token.put import UpdateGrantToken
from vantage_python_sdk.apis.tags.access_grants_api_raw import AccessGrantsApiRaw


class AccessGrantsApi(
    CreateGrant,
    Delete,
    GetSpecificGrant,
    ListAccessible,
    UpdateGrantToken,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AccessGrantsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AccessGrantsApiRaw(api_client)
