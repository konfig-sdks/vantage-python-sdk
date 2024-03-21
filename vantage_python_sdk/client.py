# coding: utf-8
"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

import typing
import inspect
from datetime import date, datetime
from vantage_python_sdk.client_custom import ClientCustom
from vantage_python_sdk.configuration import Configuration
from vantage_python_sdk.api_client import ApiClient
from vantage_python_sdk.type_util import copy_signature
from vantage_python_sdk.apis.tags.access_grants_api import AccessGrantsApi
from vantage_python_sdk.apis.tags.business_metrics_api import BusinessMetricsApi
from vantage_python_sdk.apis.tags.costs_api import CostsApi
from vantage_python_sdk.apis.tags.dashboards_api import DashboardsApi
from vantage_python_sdk.apis.tags.filters_api import FiltersApi
from vantage_python_sdk.apis.tags.folders_api import FoldersApi
from vantage_python_sdk.apis.tags.notifications_api import NotificationsApi
from vantage_python_sdk.apis.tags.ping_api import PingApi
from vantage_python_sdk.apis.tags.prices_api import PricesApi
from vantage_python_sdk.apis.tags.segments_api import SegmentsApi
from vantage_python_sdk.apis.tags.teams_api import TeamsApi
from vantage_python_sdk.apis.tags.users_api import UsersApi
from vantage_python_sdk.apis.tags.workspaces_api import WorkspacesApi



class Vantage(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.access_grants: AccessGrantsApi = AccessGrantsApi(api_client)
        self.business_metrics: BusinessMetricsApi = BusinessMetricsApi(api_client)
        self.costs: CostsApi = CostsApi(api_client)
        self.dashboards: DashboardsApi = DashboardsApi(api_client)
        self.filters: FiltersApi = FiltersApi(api_client)
        self.folders: FoldersApi = FoldersApi(api_client)
        self.notifications: NotificationsApi = NotificationsApi(api_client)
        self.ping: PingApi = PingApi(api_client)
        self.prices: PricesApi = PricesApi(api_client)
        self.segments: SegmentsApi = SegmentsApi(api_client)
        self.teams: TeamsApi = TeamsApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
        self.workspaces: WorkspacesApi = WorkspacesApi(api_client)
