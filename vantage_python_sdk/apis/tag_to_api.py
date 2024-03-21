import typing_extensions

from vantage_python_sdk.apis.tags import TagValues
from vantage_python_sdk.apis.tags.costs_api import CostsApi
from vantage_python_sdk.apis.tags.business_metrics_api import BusinessMetricsApi
from vantage_python_sdk.apis.tags.folders_api import FoldersApi
from vantage_python_sdk.apis.tags.filters_api import FiltersApi
from vantage_python_sdk.apis.tags.segments_api import SegmentsApi
from vantage_python_sdk.apis.tags.dashboards_api import DashboardsApi
from vantage_python_sdk.apis.tags.teams_api import TeamsApi
from vantage_python_sdk.apis.tags.access_grants_api import AccessGrantsApi
from vantage_python_sdk.apis.tags.notifications_api import NotificationsApi
from vantage_python_sdk.apis.tags.prices_api import PricesApi
from vantage_python_sdk.apis.tags.workspaces_api import WorkspacesApi
from vantage_python_sdk.apis.tags.users_api import UsersApi
from vantage_python_sdk.apis.tags.ping_api import PingApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COSTS: CostsApi,
        TagValues.BUSINESS_METRICS: BusinessMetricsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.FILTERS: FiltersApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.ACCESS_GRANTS: AccessGrantsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.PRICES: PricesApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.USERS: UsersApi,
        TagValues.PING: PingApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COSTS: CostsApi,
        TagValues.BUSINESS_METRICS: BusinessMetricsApi,
        TagValues.FOLDERS: FoldersApi,
        TagValues.FILTERS: FiltersApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.ACCESS_GRANTS: AccessGrantsApi,
        TagValues.NOTIFICATIONS: NotificationsApi,
        TagValues.PRICES: PricesApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.USERS: UsersApi,
        TagValues.PING: PingApi,
    }
)
