# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from vantage_python_sdk.paths.dashboards.post import CreateDashboardRaw
from vantage_python_sdk.paths.cost_reports.post import CreateReportRaw
from vantage_python_sdk.paths.cost_reports_cost_report_token.delete import DeleteCostReportRaw
from vantage_python_sdk.paths.dashboards_dashboard_token.delete import DeleteDashboardRaw
from vantage_python_sdk.paths.dashboards.get import GetAllRaw
from vantage_python_sdk.paths.cost_reports.get import GetAllCostReportsRaw
from vantage_python_sdk.paths.cost_reports_cost_report_token.get import GetCostReportRaw
from vantage_python_sdk.paths.dashboards_dashboard_token.get import GetSpecificDashboardRaw
from vantage_python_sdk.paths.costs.get import ListCostReportRaw
from vantage_python_sdk.paths.dashboards_dashboard_token.put import UpdateDashboardRaw
from vantage_python_sdk.paths.cost_reports_cost_report_token.put import UpdateReportRaw


class CostsApiRaw(
    CreateDashboardRaw,
    CreateReportRaw,
    DeleteCostReportRaw,
    DeleteDashboardRaw,
    GetAllRaw,
    GetAllCostReportsRaw,
    GetCostReportRaw,
    GetSpecificDashboardRaw,
    ListCostReportRaw,
    UpdateDashboardRaw,
    UpdateReportRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass