# coding: utf-8

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

from vantage_python_sdk.paths.business_metrics.post import CreateNewMetric
from vantage_python_sdk.paths.business_metrics_business_metric_token.delete import DeleteExistingMetric
from vantage_python_sdk.paths.business_metrics.get import GetAllMetrics
from vantage_python_sdk.paths.business_metrics_business_metric_token.get import GetMetricById
from vantage_python_sdk.paths.business_metrics_business_metric_token.put import UpdateExistingMetric
from vantage_python_sdk.paths.business_metrics_business_metric_token_values_csv.put import UpdateValuesCsv
from vantage_python_sdk.apis.tags.business_metrics_api_raw import BusinessMetricsApiRaw


class BusinessMetricsApi(
    CreateNewMetric,
    DeleteExistingMetric,
    GetAllMetrics,
    GetMetricById,
    UpdateExistingMetric,
    UpdateValuesCsv,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BusinessMetricsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BusinessMetricsApiRaw(api_client)
