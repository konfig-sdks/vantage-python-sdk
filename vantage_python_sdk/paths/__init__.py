# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vantage_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    WORKSPACES = "/workspaces"
    WORKSPACES_WORKSPACE_TOKEN = "/workspaces/{workspace_token}"
    FOLDERS = "/folders"
    FOLDERS_FOLDER_TOKEN = "/folders/{folder_token}"
    SAVED_FILTERS = "/saved_filters"
    SAVED_FILTERS_SAVED_FILTER_TOKEN = "/saved_filters/{saved_filter_token}"
    COST_REPORTS = "/cost_reports"
    COST_REPORTS_COST_REPORT_TOKEN = "/cost_reports/{cost_report_token}"
    SEGMENTS = "/segments"
    SEGMENTS_SEGMENT_TOKEN = "/segments/{segment_token}"
    DASHBOARDS = "/dashboards"
    DASHBOARDS_DASHBOARD_TOKEN = "/dashboards/{dashboard_token}"
    COSTS = "/costs"
    TEAMS = "/teams"
    TEAMS_TEAM_TOKEN = "/teams/{team_token}"
    ACCESS_GRANTS = "/access_grants"
    ACCESS_GRANTS_ACCESS_GRANT_TOKEN = "/access_grants/{access_grant_token}"
    REPORT_NOTIFICATIONS = "/report_notifications"
    REPORT_NOTIFICATIONS_REPORT_NOTIFICATION_TOKEN = "/report_notifications/{report_notification_token}"
    USERS = "/users"
    USERS_USER_TOKEN = "/users/{user_token}"
    BUSINESS_METRICS = "/business_metrics"
    BUSINESS_METRICS_BUSINESS_METRIC_TOKEN = "/business_metrics/{business_metric_token}"
    BUSINESS_METRICS_BUSINESS_METRIC_TOKEN_VALUES_CSV = "/business_metrics/{business_metric_token}/values.csv"
    PRODUCTS = "/products"
    PRODUCTS_ID = "/products/{id}"
    PRODUCTS_PRODUCT_ID_PRICES = "/products/{product_id}/prices"
    PRODUCTS_PRODUCT_ID_PRICES_ID = "/products/{product_id}/prices/{id}"
    PING = "/ping"
