import typing_extensions

from vantage_python_sdk.paths import PathValues
from vantage_python_sdk.apis.paths.workspaces import Workspaces
from vantage_python_sdk.apis.paths.workspaces_workspace_token import WorkspacesWorkspaceToken
from vantage_python_sdk.apis.paths.folders import Folders
from vantage_python_sdk.apis.paths.folders_folder_token import FoldersFolderToken
from vantage_python_sdk.apis.paths.saved_filters import SavedFilters
from vantage_python_sdk.apis.paths.saved_filters_saved_filter_token import SavedFiltersSavedFilterToken
from vantage_python_sdk.apis.paths.cost_reports import CostReports
from vantage_python_sdk.apis.paths.cost_reports_cost_report_token import CostReportsCostReportToken
from vantage_python_sdk.apis.paths.segments import Segments
from vantage_python_sdk.apis.paths.segments_segment_token import SegmentsSegmentToken
from vantage_python_sdk.apis.paths.dashboards import Dashboards
from vantage_python_sdk.apis.paths.dashboards_dashboard_token import DashboardsDashboardToken
from vantage_python_sdk.apis.paths.costs import Costs
from vantage_python_sdk.apis.paths.teams import Teams
from vantage_python_sdk.apis.paths.teams_team_token import TeamsTeamToken
from vantage_python_sdk.apis.paths.access_grants import AccessGrants
from vantage_python_sdk.apis.paths.access_grants_access_grant_token import AccessGrantsAccessGrantToken
from vantage_python_sdk.apis.paths.report_notifications import ReportNotifications
from vantage_python_sdk.apis.paths.report_notifications_report_notification_token import ReportNotificationsReportNotificationToken
from vantage_python_sdk.apis.paths.users import Users
from vantage_python_sdk.apis.paths.users_user_token import UsersUserToken
from vantage_python_sdk.apis.paths.business_metrics import BusinessMetrics
from vantage_python_sdk.apis.paths.business_metrics_business_metric_token import BusinessMetricsBusinessMetricToken
from vantage_python_sdk.apis.paths.business_metrics_business_metric_token_values_csv import BusinessMetricsBusinessMetricTokenValuesCsv
from vantage_python_sdk.apis.paths.products import Products
from vantage_python_sdk.apis.paths.products_id import ProductsId
from vantage_python_sdk.apis.paths.products_product_id_prices import ProductsProductIdPrices
from vantage_python_sdk.apis.paths.products_product_id_prices_id import ProductsProductIdPricesId
from vantage_python_sdk.apis.paths.ping import Ping

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_TOKEN: WorkspacesWorkspaceToken,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_FOLDER_TOKEN: FoldersFolderToken,
        PathValues.SAVED_FILTERS: SavedFilters,
        PathValues.SAVED_FILTERS_SAVED_FILTER_TOKEN: SavedFiltersSavedFilterToken,
        PathValues.COST_REPORTS: CostReports,
        PathValues.COST_REPORTS_COST_REPORT_TOKEN: CostReportsCostReportToken,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_SEGMENT_TOKEN: SegmentsSegmentToken,
        PathValues.DASHBOARDS: Dashboards,
        PathValues.DASHBOARDS_DASHBOARD_TOKEN: DashboardsDashboardToken,
        PathValues.COSTS: Costs,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_TOKEN: TeamsTeamToken,
        PathValues.ACCESS_GRANTS: AccessGrants,
        PathValues.ACCESS_GRANTS_ACCESS_GRANT_TOKEN: AccessGrantsAccessGrantToken,
        PathValues.REPORT_NOTIFICATIONS: ReportNotifications,
        PathValues.REPORT_NOTIFICATIONS_REPORT_NOTIFICATION_TOKEN: ReportNotificationsReportNotificationToken,
        PathValues.USERS: Users,
        PathValues.USERS_USER_TOKEN: UsersUserToken,
        PathValues.BUSINESS_METRICS: BusinessMetrics,
        PathValues.BUSINESS_METRICS_BUSINESS_METRIC_TOKEN: BusinessMetricsBusinessMetricToken,
        PathValues.BUSINESS_METRICS_BUSINESS_METRIC_TOKEN_VALUES_CSV: BusinessMetricsBusinessMetricTokenValuesCsv,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.PRODUCTS_PRODUCT_ID_PRICES: ProductsProductIdPrices,
        PathValues.PRODUCTS_PRODUCT_ID_PRICES_ID: ProductsProductIdPricesId,
        PathValues.PING: Ping,
    }
)

path_to_api = PathToApi(
    {
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_TOKEN: WorkspacesWorkspaceToken,
        PathValues.FOLDERS: Folders,
        PathValues.FOLDERS_FOLDER_TOKEN: FoldersFolderToken,
        PathValues.SAVED_FILTERS: SavedFilters,
        PathValues.SAVED_FILTERS_SAVED_FILTER_TOKEN: SavedFiltersSavedFilterToken,
        PathValues.COST_REPORTS: CostReports,
        PathValues.COST_REPORTS_COST_REPORT_TOKEN: CostReportsCostReportToken,
        PathValues.SEGMENTS: Segments,
        PathValues.SEGMENTS_SEGMENT_TOKEN: SegmentsSegmentToken,
        PathValues.DASHBOARDS: Dashboards,
        PathValues.DASHBOARDS_DASHBOARD_TOKEN: DashboardsDashboardToken,
        PathValues.COSTS: Costs,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_TOKEN: TeamsTeamToken,
        PathValues.ACCESS_GRANTS: AccessGrants,
        PathValues.ACCESS_GRANTS_ACCESS_GRANT_TOKEN: AccessGrantsAccessGrantToken,
        PathValues.REPORT_NOTIFICATIONS: ReportNotifications,
        PathValues.REPORT_NOTIFICATIONS_REPORT_NOTIFICATION_TOKEN: ReportNotificationsReportNotificationToken,
        PathValues.USERS: Users,
        PathValues.USERS_USER_TOKEN: UsersUserToken,
        PathValues.BUSINESS_METRICS: BusinessMetrics,
        PathValues.BUSINESS_METRICS_BUSINESS_METRIC_TOKEN: BusinessMetricsBusinessMetricToken,
        PathValues.BUSINESS_METRICS_BUSINESS_METRIC_TOKEN_VALUES_CSV: BusinessMetricsBusinessMetricTokenValuesCsv,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.PRODUCTS_PRODUCT_ID_PRICES: ProductsProductIdPrices,
        PathValues.PRODUCTS_PRODUCT_ID_PRICES_ID: ProductsProductIdPricesId,
        PathValues.PING: Ping,
    }
)
