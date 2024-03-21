# coding: utf-8

# flake8: noqa

"""
    Vantage

    Vantage API

    The version of the OpenAPI document: 2.0.0
    Contact: support@vantage.sh
    Created by: https://www.vantage.sh
"""

__version__ = "2.0.0"

# import ApiClient
from vantage_python_sdk.api_client import ApiClient

# import Configuration
from vantage_python_sdk.configuration import Configuration

# import exceptions
from vantage_python_sdk.exceptions import OpenApiException
from vantage_python_sdk.exceptions import ApiAttributeError
from vantage_python_sdk.exceptions import ApiTypeError
from vantage_python_sdk.exceptions import ApiValueError
from vantage_python_sdk.exceptions import ApiKeyError
from vantage_python_sdk.exceptions import ApiException

from vantage_python_sdk.client import Vantage
