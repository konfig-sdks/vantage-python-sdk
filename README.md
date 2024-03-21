<div align="center">

[![Visit Vantage](./header.png)](https://vantage.sh)

# Vantage<a id="vantage"></a>

Vantage API


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`vantage.access_grants.create_grant`](#vantageaccess_grantscreate_grant)
  * [`vantage.access_grants.delete`](#vantageaccess_grantsdelete)
  * [`vantage.access_grants.get_specific_grant`](#vantageaccess_grantsget_specific_grant)
  * [`vantage.access_grants.list_accessible`](#vantageaccess_grantslist_accessible)
  * [`vantage.access_grants.update_grant_token`](#vantageaccess_grantsupdate_grant_token)
  * [`vantage.business_metrics.create_new_metric`](#vantagebusiness_metricscreate_new_metric)
  * [`vantage.business_metrics.delete_existing_metric`](#vantagebusiness_metricsdelete_existing_metric)
  * [`vantage.business_metrics.get_all_metrics`](#vantagebusiness_metricsget_all_metrics)
  * [`vantage.business_metrics.get_metric_by_id`](#vantagebusiness_metricsget_metric_by_id)
  * [`vantage.business_metrics.update_existing_metric`](#vantagebusiness_metricsupdate_existing_metric)
  * [`vantage.business_metrics.update_values_csv`](#vantagebusiness_metricsupdate_values_csv)
  * [`vantage.costs.create_dashboard`](#vantagecostscreate_dashboard)
  * [`vantage.costs.create_report`](#vantagecostscreate_report)
  * [`vantage.costs.delete_cost_report`](#vantagecostsdelete_cost_report)
  * [`vantage.costs.delete_dashboard`](#vantagecostsdelete_dashboard)
  * [`vantage.costs.get_all`](#vantagecostsget_all)
  * [`vantage.costs.get_all_cost_reports`](#vantagecostsget_all_cost_reports)
  * [`vantage.costs.get_cost_report`](#vantagecostsget_cost_report)
  * [`vantage.costs.get_specific_dashboard`](#vantagecostsget_specific_dashboard)
  * [`vantage.costs.list_cost_report`](#vantagecostslist_cost_report)
  * [`vantage.costs.update_dashboard`](#vantagecostsupdate_dashboard)
  * [`vantage.costs.update_report`](#vantagecostsupdate_report)
  * [`vantage.dashboards.create_dashboard`](#vantagedashboardscreate_dashboard)
  * [`vantage.dashboards.delete_dashboard`](#vantagedashboardsdelete_dashboard)
  * [`vantage.dashboards.get_all`](#vantagedashboardsget_all)
  * [`vantage.dashboards.get_specific_dashboard`](#vantagedashboardsget_specific_dashboard)
  * [`vantage.dashboards.update_dashboard`](#vantagedashboardsupdate_dashboard)
  * [`vantage.filters.create_saved_filter_for_cost_reports`](#vantagefilterscreate_saved_filter_for_cost_reports)
  * [`vantage.filters.delete_saved_filter`](#vantagefiltersdelete_saved_filter)
  * [`vantage.filters.get_cost_report_filters`](#vantagefiltersget_cost_report_filters)
  * [`vantage.filters.get_saved_filter`](#vantagefiltersget_saved_filter)
  * [`vantage.filters.update_saved_filter_for_cost_reports`](#vantagefiltersupdate_saved_filter_for_cost_reports)
  * [`vantage.folders.create_folder_for_cost_reports`](#vantagefolderscreate_folder_for_cost_reports)
  * [`vantage.folders.delete_folder_for_cost_reports`](#vantagefoldersdelete_folder_for_cost_reports)
  * [`vantage.folders.get_specific_folder`](#vantagefoldersget_specific_folder)
  * [`vantage.folders.list_cost_reports`](#vantagefolderslist_cost_reports)
  * [`vantage.folders.update_folder_for_cost_reports`](#vantagefoldersupdate_folder_for_cost_reports)
  * [`vantage.notifications.create_report_notification`](#vantagenotificationscreate_report_notification)
  * [`vantage.notifications.delete_report_notification`](#vantagenotificationsdelete_report_notification)
  * [`vantage.notifications.get_all_report_notifications`](#vantagenotificationsget_all_report_notifications)
  * [`vantage.notifications.get_report_notification`](#vantagenotificationsget_report_notification)
  * [`vantage.notifications.update_report_notification`](#vantagenotificationsupdate_report_notification)
  * [`vantage.ping.health_check`](#vantagepinghealth_check)
  * [`vantage.prices.get_product`](#vantagepricesget_product)
  * [`vantage.prices.get_product_price`](#vantagepricesget_product_price)
  * [`vantage.prices.get_product_prices`](#vantagepricesget_product_prices)
  * [`vantage.prices.list_available_products`](#vantagepriceslist_available_products)
  * [`vantage.segments.create_segment`](#vantagesegmentscreate_segment)
  * [`vantage.segments.get_segment_by_id`](#vantagesegmentsget_segment_by_id)
  * [`vantage.segments.list`](#vantagesegmentslist)
  * [`vantage.segments.remove_segment`](#vantagesegmentsremove_segment)
  * [`vantage.segments.update_segment_by_id`](#vantagesegmentsupdate_segment_by_id)
  * [`vantage.teams.create_new_team`](#vantageteamscreate_new_team)
  * [`vantage.teams.get_specific_team`](#vantageteamsget_specific_team)
  * [`vantage.teams.list_accessible`](#vantageteamslist_accessible)
  * [`vantage.teams.remove_team`](#vantageteamsremove_team)
  * [`vantage.teams.update_team`](#vantageteamsupdate_team)
  * [`vantage.users.get_specific_user`](#vantageusersget_specific_user)
  * [`vantage.users.list_accessible`](#vantageuserslist_accessible)
  * [`vantage.workspaces.get_specific_workspace`](#vantageworkspacesget_specific_workspace)
  * [`vantage.workspaces.list_accessible`](#vantageworkspaceslist_accessible)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Vantage&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from vantage_python_sdk import Vantage, ApiException

vantage = Vantage(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    create_grant_response = vantage.access_grants.create_grant(
        resource_token="string_example",
        team_token="string_example",
        access="denied",
    )
    print(create_grant_response)
except ApiException as e:
    print("Exception when calling AccessGrantsApi.create_grant: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 422:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 403:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 404:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 406:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from vantage_python_sdk import Vantage, ApiException

vantage = Vantage(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        create_grant_response = await vantage.access_grants.acreate_grant(
            resource_token="string_example",
            team_token="string_example",
            access="denied",
        )
        print(create_grant_response)
    except ApiException as e:
        print("Exception when calling AccessGrantsApi.create_grant: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["links"])
            pprint(e.body["errors"])
        if e.status == 422:
            pprint(e.body["links"])
            pprint(e.body["errors"])
        if e.status == 403:
            pprint(e.body["links"])
            pprint(e.body["errors"])
        if e.status == 404:
            pprint(e.body["links"])
            pprint(e.body["errors"])
        if e.status == 406:
            pprint(e.body["links"])
            pprint(e.body["errors"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from vantage_python_sdk import Vantage, ApiException

vantage = Vantage(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    create_grant_response = vantage.access_grants.raw.create_grant(
        resource_token="string_example",
        team_token="string_example",
        access="denied",
    )
    pprint(create_grant_response.body)
    pprint(create_grant_response.body["token"])
    pprint(create_grant_response.body["resource_token"])
    pprint(create_grant_response.body["access"])
    pprint(create_grant_response.body["team_token"])
    pprint(create_grant_response.body["created_at"])
    pprint(create_grant_response.body["created_by"])
    pprint(create_grant_response.headers)
    pprint(create_grant_response.status)
    pprint(create_grant_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccessGrantsApi.create_grant: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 422:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 403:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 404:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    if e.status == 406:
        pprint(e.body["links"])
        pprint(e.body["errors"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `vantage.access_grants.create_grant`<a id="vantageaccess_grantscreate_grant"></a>

Create an Access Grant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_grant_response = vantage.access_grants.create_grant(
    resource_token="string_example",
    team_token="string_example",
    access="denied",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resource_token: `str`<a id="resource_token-str"></a>

The token of the resource for which you are granting access.

##### team_token: `str`<a id="team_token-str"></a>

The token of the Team you want to grant access to.

##### access: `str`<a id="access-str"></a>

The access level you want to grant. Defaults to 'allowed'.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostAccessGrants`](./vantage_python_sdk/type/post_access_grants.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessGrant`](./vantage_python_sdk/pydantic/access_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access_grants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.access_grants.delete`<a id="vantageaccess_grantsdelete"></a>

Delete an Access Grant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = vantage.access_grants.delete(
    access_grant_token="access_grant_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access_grant_token: `str`<a id="access_grant_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AccessGrant`](./vantage_python_sdk/pydantic/access_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access_grants/{access_grant_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.access_grants.get_specific_grant`<a id="vantageaccess_grantsget_specific_grant"></a>

Return a specific Access Grant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_grant_response = vantage.access_grants.get_specific_grant(
    access_grant_token="access_grant_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access_grant_token: `str`<a id="access_grant_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AccessGrant`](./vantage_python_sdk/pydantic/access_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access_grants/{access_grant_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.access_grants.list_accessible`<a id="vantageaccess_grantslist_accessible"></a>

Return all Access Grants that the current API token has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessible_response = vantage.access_grants.list_accessible(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`AccessGrants`](./vantage_python_sdk/pydantic/access_grants.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access_grants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.access_grants.update_grant_token`<a id="vantageaccess_grantsupdate_grant_token"></a>

Update an AccessGrant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_grant_token_response = vantage.access_grants.update_grant_token(
    access="denied",
    access_grant_token="access_grant_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### access: `str`<a id="access-str"></a>

Allowed or denied access to resource.

##### access_grant_token: `str`<a id="access_grant_token-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutAccessGrants`](./vantage_python_sdk/type/put_access_grants.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AccessGrant`](./vantage_python_sdk/pydantic/access_grant.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access_grants/{access_grant_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.create_new_metric`<a id="vantagebusiness_metricscreate_new_metric"></a>

Create a new Business Metric.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_metric_response = vantage.business_metrics.create_new_metric(
    title="string_example",
    cost_report_tokens_with_metadata=[
        {
            "cost_report_token": "cost_report_token_example",
            "unit_scale": "per_unit",
        }
    ],
    values=[
        {
            "date": "1970-01-01T00:00:00.00Z",
            "amount": 3.14,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the Business Metric.

##### cost_report_tokens_with_metadata: [`PostBusinessMetricsCostReportTokensWithMetadata`](./vantage_python_sdk/type/post_business_metrics_cost_report_tokens_with_metadata.py)<a id="cost_report_tokens_with_metadata-postbusinessmetricscostreporttokenswithmetadatavantage_python_sdktypepost_business_metrics_cost_report_tokens_with_metadatapy"></a>

##### values: [`PostBusinessMetricsValues`](./vantage_python_sdk/type/post_business_metrics_values.py)<a id="values-postbusinessmetricsvaluesvantage_python_sdktypepost_business_metrics_valuespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostBusinessMetrics`](./vantage_python_sdk/type/post_business_metrics.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetric`](./vantage_python_sdk/pydantic/business_metric.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.delete_existing_metric`<a id="vantagebusiness_metricsdelete_existing_metric"></a>

Deletes an existing BusinessMetric.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_existing_metric_response = vantage.business_metrics.delete_existing_metric(
    business_metric_token="business_metric_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### business_metric_token: `str`<a id="business_metric_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetric`](./vantage_python_sdk/pydantic/business_metric.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics/{business_metric_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.get_all_metrics`<a id="vantagebusiness_metricsget_all_metrics"></a>

Return all Business Metrics that the current API token has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_metrics_response = vantage.business_metrics.get_all_metrics(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetrics`](./vantage_python_sdk/pydantic/business_metrics.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.get_metric_by_id`<a id="vantagebusiness_metricsget_metric_by_id"></a>

Return a specific Business Metric.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metric_by_id_response = vantage.business_metrics.get_metric_by_id(
    business_metric_token="business_metric_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### business_metric_token: `str`<a id="business_metric_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetric`](./vantage_python_sdk/pydantic/business_metric.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics/{business_metric_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.update_existing_metric`<a id="vantagebusiness_metricsupdate_existing_metric"></a>

Updates an existing BusinessMetric.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_metric_response = vantage.business_metrics.update_existing_metric(
    business_metric_token="business_metric_token_example",
    title="string_example",
    cost_report_tokens_with_metadata=[
        {
            "cost_report_token": "cost_report_token_example",
            "unit_scale": "per_unit",
        }
    ],
    values=[
        {
            "date": "1970-01-01T00:00:00.00Z",
            "amount": 3.14,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### business_metric_token: `str`<a id="business_metric_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the BusinessMetric.

##### cost_report_tokens_with_metadata: [`PutBusinessMetricsCostReportTokensWithMetadata`](./vantage_python_sdk/type/put_business_metrics_cost_report_tokens_with_metadata.py)<a id="cost_report_tokens_with_metadata-putbusinessmetricscostreporttokenswithmetadatavantage_python_sdktypeput_business_metrics_cost_report_tokens_with_metadatapy"></a>

##### values: [`PutBusinessMetricsValues`](./vantage_python_sdk/type/put_business_metrics_values.py)<a id="values-putbusinessmetricsvaluesvantage_python_sdktypeput_business_metrics_valuespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutBusinessMetrics`](./vantage_python_sdk/type/put_business_metrics.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetric`](./vantage_python_sdk/pydantic/business_metric.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics/{business_metric_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.business_metrics.update_values_csv`<a id="vantagebusiness_metricsupdate_values_csv"></a>

Updates the values for an existing BusinessMetric from a CSV file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_values_csv_response = vantage.business_metrics.update_values_csv(
    business_metric_token="business_metric_token_example",
    csv=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### business_metric_token: `str`<a id="business_metric_token-str"></a>

##### csv: `IO`<a id="csv-io"></a>

CSV file containing BusinessMetric dates and amounts

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessMetricsUpdateValuesCsvRequest`](./vantage_python_sdk/type/business_metrics_update_values_csv_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessMetric`](./vantage_python_sdk/pydantic/business_metric.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/business_metrics/{business_metric_token}/values.csv` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.create_dashboard`<a id="vantagecostscreate_dashboard"></a>

Create a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_dashboard_response = vantage.costs.create_dashboard(
    title="string_example",
    end_date="string_example",
    widget_tokens=["string_example"],
    saved_filter_tokens=["string_example"],
    date_bin="cumulative",
    date_interval="this_month",
    start_date="string_example",
    workspace_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the Dashboard.

##### end_date: `str`<a id="end_date-str"></a>

The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### widget_tokens: [`PostDashboardsWidgetTokens`](./vantage_python_sdk/type/post_dashboards_widget_tokens.py)<a id="widget_tokens-postdashboardswidgettokensvantage_python_sdktypepost_dashboards_widget_tokenspy"></a>

##### saved_filter_tokens: [`PostDashboardsSavedFilterTokens`](./vantage_python_sdk/type/post_dashboards_saved_filter_tokens.py)<a id="saved_filter_tokens-postdashboardssavedfiltertokensvantage_python_sdktypepost_dashboards_saved_filter_tokenspy"></a>

##### date_bin: `str`<a id="date_bin-str"></a>

Determines how to group costs in the Dashboard.

##### date_interval: `str`<a id="date_interval-str"></a>

Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.

##### start_date: `str`<a id="start_date-str"></a>

The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the Dashboard to. Required if the API token is associated with multiple Workspaces.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostDashboards`](./vantage_python_sdk/type/post_dashboards.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.create_report`<a id="vantagecostscreate_report"></a>

Create a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_report_response = vantage.costs.create_report(
    title="string_example",
    workspace_token="string_example",
    groupings="string_example",
    filter="string_example",
    saved_filter_tokens=["string_example"],
    business_metric_tokens_with_metadata=[
        {
            "business_metric_token": "business_metric_token_example",
            "unit_scale": "per_unit",
        }
    ],
    folder_token="string_example",
    settings={
        "include_credits": False,
        "include_refunds": False,
        "include_discounts": True,
        "include_tax": True,
        "amortize": True,
        "unallocated": False,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the CostReport.

##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the Cost Report to. Ignored if 'folder_token' is set. Required if the API token is associated with multiple Workspaces.

##### groupings: `str`<a id="groupings-str"></a>

Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region

##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.

##### saved_filter_tokens: [`PostCostReportsSavedFilterTokens`](./vantage_python_sdk/type/post_cost_reports_saved_filter_tokens.py)<a id="saved_filter_tokens-postcostreportssavedfiltertokensvantage_python_sdktypepost_cost_reports_saved_filter_tokenspy"></a>

##### business_metric_tokens_with_metadata: [`PostCostReportsBusinessMetricTokensWithMetadata`](./vantage_python_sdk/type/post_cost_reports_business_metric_tokens_with_metadata.py)<a id="business_metric_tokens_with_metadata-postcostreportsbusinessmetrictokenswithmetadatavantage_python_sdktypepost_cost_reports_business_metric_tokens_with_metadatapy"></a>

##### folder_token: `str`<a id="folder_token-str"></a>

The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.

##### settings: [`PostCostReportsSettings`](./vantage_python_sdk/type/post_cost_reports_settings.py)<a id="settings-postcostreportssettingsvantage_python_sdktypepost_cost_reports_settingspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostCostReports`](./vantage_python_sdk/type/post_cost_reports.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostReport`](./vantage_python_sdk/pydantic/cost_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost_reports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.delete_cost_report`<a id="vantagecostsdelete_cost_report"></a>

Delete a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_cost_report_response = vantage.costs.delete_cost_report(
    cost_report_token="cost_report_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CostReport`](./vantage_python_sdk/pydantic/cost_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost_reports/{cost_report_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.delete_dashboard`<a id="vantagecostsdelete_dashboard"></a>

Delete a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_dashboard_response = vantage.costs.delete_dashboard(
    dashboard_token="dashboard_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.get_all`<a id="vantagecostsget_all"></a>

Return all Dashboards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = vantage.costs.get_all(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboards`](./vantage_python_sdk/pydantic/dashboards.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.get_all_cost_reports`<a id="vantagecostsget_all_cost_reports"></a>

Return all CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_cost_reports_response = vantage.costs.get_all_cost_reports(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`CostReports`](./vantage_python_sdk/pydantic/cost_reports.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost_reports` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.get_cost_report`<a id="vantagecostsget_cost_report"></a>

Return a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cost_report_response = vantage.costs.get_cost_report(
    cost_report_token="cost_report_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CostReport`](./vantage_python_sdk/pydantic/cost_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost_reports/{cost_report_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.get_specific_dashboard`<a id="vantagecostsget_specific_dashboard"></a>

Return a specific Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_dashboard_response = vantage.costs.get_specific_dashboard(
    dashboard_token="dashboard_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.list_cost_report`<a id="vantagecostslist_cost_report"></a>

Return all Costs for a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_cost_report_response = vantage.costs.list_cost_report(
    cost_report_token="cost_report_token_example",
    start_date="string_example",
    end_date="string_example",
    groupings=["string_example"],
    order="desc",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

The CostReport token.

##### start_date: `str`<a id="start_date-str"></a>

First date you would like to filter costs from. ISO 8601 formatted.

##### end_date: `str`<a id="end_date-str"></a>

Last date you would like to filter costs to. ISO 8601 formatted.

##### groupings: List[`str`]<a id="groupings-liststr"></a>

Group the results by specific field(s). Defaults to provider, service, account_id. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region

##### order: `str`<a id="order-str"></a>

Whether to order costs by date in an ascending or descending manner.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Costs`](./vantage_python_sdk/pydantic/costs.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/costs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.update_dashboard`<a id="vantagecostsupdate_dashboard"></a>

Update a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_dashboard_response = vantage.costs.update_dashboard(
    end_date="string_example",
    dashboard_token="dashboard_token_example",
    title="string_example",
    widget_tokens=["string_example"],
    saved_filter_tokens=["string_example"],
    date_bin="cumulative",
    date_interval="this_month",
    start_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### end_date: `str`<a id="end_date-str"></a>

The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the Dashboard.

##### widget_tokens: [`PutDashboardsWidgetTokens`](./vantage_python_sdk/type/put_dashboards_widget_tokens.py)<a id="widget_tokens-putdashboardswidgettokensvantage_python_sdktypeput_dashboards_widget_tokenspy"></a>

##### saved_filter_tokens: [`PutDashboardsSavedFilterTokens`](./vantage_python_sdk/type/put_dashboards_saved_filter_tokens.py)<a id="saved_filter_tokens-putdashboardssavedfiltertokensvantage_python_sdktypeput_dashboards_saved_filter_tokenspy"></a>

##### date_bin: `str`<a id="date_bin-str"></a>

Determines how to group costs in the Dashboard.

##### date_interval: `str`<a id="date_interval-str"></a>

Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.

##### start_date: `str`<a id="start_date-str"></a>

The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutDashboards`](./vantage_python_sdk/type/put_dashboards.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.costs.update_report`<a id="vantagecostsupdate_report"></a>

Update a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_report_response = vantage.costs.update_report(
    cost_report_token="cost_report_token_example",
    title="string_example",
    groupings="string_example",
    filter="string_example",
    saved_filter_tokens=["string_example"],
    business_metric_tokens_with_metadata=[
        {
            "business_metric_token": "business_metric_token_example",
            "unit_scale": "per_unit",
        }
    ],
    folder_token="string_example",
    settings={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the CostReport.

##### groupings: `str`<a id="groupings-str"></a>

Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:<tag_value>. If providing multiple groupings, join as comma separated values: groupings=provider,service,region

##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql.

##### saved_filter_tokens: [`PutCostReportsSavedFilterTokens`](./vantage_python_sdk/type/put_cost_reports_saved_filter_tokens.py)<a id="saved_filter_tokens-putcostreportssavedfiltertokensvantage_python_sdktypeput_cost_reports_saved_filter_tokenspy"></a>

##### business_metric_tokens_with_metadata: [`PutCostReportsBusinessMetricTokensWithMetadata`](./vantage_python_sdk/type/put_cost_reports_business_metric_tokens_with_metadata.py)<a id="business_metric_tokens_with_metadata-putcostreportsbusinessmetrictokenswithmetadatavantage_python_sdktypeput_cost_reports_business_metric_tokens_with_metadatapy"></a>

##### folder_token: `str`<a id="folder_token-str"></a>

The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to.

##### settings: [`PutCostReportsSettings`](./vantage_python_sdk/type/put_cost_reports_settings.py)<a id="settings-putcostreportssettingsvantage_python_sdktypeput_cost_reports_settingspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutCostReports`](./vantage_python_sdk/type/put_cost_reports.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostReport`](./vantage_python_sdk/pydantic/cost_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cost_reports/{cost_report_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.dashboards.create_dashboard`<a id="vantagedashboardscreate_dashboard"></a>

Create a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_dashboard_response = vantage.dashboards.create_dashboard(
    title="string_example",
    end_date="string_example",
    widget_tokens=["string_example"],
    saved_filter_tokens=["string_example"],
    date_bin="cumulative",
    date_interval="this_month",
    start_date="string_example",
    workspace_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the Dashboard.

##### end_date: `str`<a id="end_date-str"></a>

The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### widget_tokens: [`PostDashboardsWidgetTokens`](./vantage_python_sdk/type/post_dashboards_widget_tokens.py)<a id="widget_tokens-postdashboardswidgettokensvantage_python_sdktypepost_dashboards_widget_tokenspy"></a>

##### saved_filter_tokens: [`PostDashboardsSavedFilterTokens`](./vantage_python_sdk/type/post_dashboards_saved_filter_tokens.py)<a id="saved_filter_tokens-postdashboardssavedfiltertokensvantage_python_sdktypepost_dashboards_saved_filter_tokenspy"></a>

##### date_bin: `str`<a id="date_bin-str"></a>

Determines how to group costs in the Dashboard.

##### date_interval: `str`<a id="date_interval-str"></a>

Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.

##### start_date: `str`<a id="start_date-str"></a>

The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the Dashboard to. Required if the API token is associated with multiple Workspaces.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostDashboards`](./vantage_python_sdk/type/post_dashboards.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.dashboards.delete_dashboard`<a id="vantagedashboardsdelete_dashboard"></a>

Delete a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_dashboard_response = vantage.dashboards.delete_dashboard(
    dashboard_token="dashboard_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.dashboards.get_all`<a id="vantagedashboardsget_all"></a>

Return all Dashboards.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = vantage.dashboards.get_all(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboards`](./vantage_python_sdk/pydantic/dashboards.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.dashboards.get_specific_dashboard`<a id="vantagedashboardsget_specific_dashboard"></a>

Return a specific Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_dashboard_response = vantage.dashboards.get_specific_dashboard(
    dashboard_token="dashboard_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.dashboards.update_dashboard`<a id="vantagedashboardsupdate_dashboard"></a>

Update a Dashboard.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_dashboard_response = vantage.dashboards.update_dashboard(
    end_date="string_example",
    dashboard_token="dashboard_token_example",
    title="string_example",
    widget_tokens=["string_example"],
    saved_filter_tokens=["string_example"],
    date_bin="cumulative",
    date_interval="this_month",
    start_date="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### end_date: `str`<a id="end_date-str"></a>

The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

##### dashboard_token: `str`<a id="dashboard_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the Dashboard.

##### widget_tokens: [`PutDashboardsWidgetTokens`](./vantage_python_sdk/type/put_dashboards_widget_tokens.py)<a id="widget_tokens-putdashboardswidgettokensvantage_python_sdktypeput_dashboards_widget_tokenspy"></a>

##### saved_filter_tokens: [`PutDashboardsSavedFilterTokens`](./vantage_python_sdk/type/put_dashboards_saved_filter_tokens.py)<a id="saved_filter_tokens-putdashboardssavedfiltertokensvantage_python_sdktypeput_dashboards_saved_filter_tokenspy"></a>

##### date_bin: `str`<a id="date_bin-str"></a>

Determines how to group costs in the Dashboard.

##### date_interval: `str`<a id="date_interval-str"></a>

Determines the date range in the Dashboard. Incompatible with 'start_date' and 'end_date' parameters.

##### start_date: `str`<a id="start_date-str"></a>

The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with 'date_interval' parameter.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutDashboards`](./vantage_python_sdk/type/put_dashboards.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Dashboard`](./vantage_python_sdk/pydantic/dashboard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/dashboards/{dashboard_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.filters.create_saved_filter_for_cost_reports`<a id="vantagefilterscreate_saved_filter_for_cost_reports"></a>

Create a SavedFilter for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_saved_filter_for_cost_reports_response = (
    vantage.filters.create_saved_filter_for_cost_reports(
        title="string_example",
        workspace_token="string_example",
        filter="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the SavedFilter.

##### workspace_token: `str`<a id="workspace_token-str"></a>

The Workspace to associate the SavedFilter with. Required if the API token is associated with multiple Workspaces.

##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the SavedFilter, which subsequently gets applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostSavedFilters`](./vantage_python_sdk/type/post_saved_filters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SavedFilter`](./vantage_python_sdk/pydantic/saved_filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saved_filters` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.filters.delete_saved_filter`<a id="vantagefiltersdelete_saved_filter"></a>

Delete a SavedFilter for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_saved_filter_response = vantage.filters.delete_saved_filter(
    saved_filter_token="saved_filter_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### saved_filter_token: `str`<a id="saved_filter_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SavedFilter`](./vantage_python_sdk/pydantic/saved_filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saved_filters/{saved_filter_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.filters.get_cost_report_filters`<a id="vantagefiltersget_cost_report_filters"></a>

Return all SavedFilters that can be applied to a CostReport.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cost_report_filters_response = vantage.filters.get_cost_report_filters(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`SavedFilters`](./vantage_python_sdk/pydantic/saved_filters.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saved_filters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.filters.get_saved_filter`<a id="vantagefiltersget_saved_filter"></a>

Return a specific SavedFilter.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_saved_filter_response = vantage.filters.get_saved_filter(
    saved_filter_token="saved_filter_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### saved_filter_token: `str`<a id="saved_filter_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SavedFilter`](./vantage_python_sdk/pydantic/saved_filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saved_filters/{saved_filter_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.filters.update_saved_filter_for_cost_reports`<a id="vantagefiltersupdate_saved_filter_for_cost_reports"></a>

Update a SavedFilter for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_saved_filter_for_cost_reports_response = (
    vantage.filters.update_saved_filter_for_cost_reports(
        saved_filter_token="saved_filter_token_example",
        title="string_example",
        filter="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### saved_filter_token: `str`<a id="saved_filter_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the SavedFilter.

##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the SavedFilter, which subsequently gets applied to a CostReport. Additional documentation available at https://docs.vantage.sh/vql.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutSavedFilters`](./vantage_python_sdk/type/put_saved_filters.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SavedFilter`](./vantage_python_sdk/pydantic/saved_filter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/saved_filters/{saved_filter_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.folders.create_folder_for_cost_reports`<a id="vantagefolderscreate_folder_for_cost_reports"></a>

Create a Folder for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_folder_for_cost_reports_response = (
    vantage.folders.create_folder_for_cost_reports(
        title="string_example",
        parent_folder_token="string_example",
        saved_filter_tokens=["string_example"],
        workspace_token="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the Folder.

##### parent_folder_token: `str`<a id="parent_folder_token-str"></a>

The token of the parent Folder.

##### saved_filter_tokens: [`PostFoldersSavedFilterTokens`](./vantage_python_sdk/type/post_folders_saved_filter_tokens.py)<a id="saved_filter_tokens-postfolderssavedfiltertokensvantage_python_sdktypepost_folders_saved_filter_tokenspy"></a>

##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the Folder to. Ignored if 'parent_folder_token' is set. Required if the API token is associated with multiple Workspaces.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostFolders`](./vantage_python_sdk/type/post_folders.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./vantage_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.folders.delete_folder_for_cost_reports`<a id="vantagefoldersdelete_folder_for_cost_reports"></a>

Delete a Folder for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_folder_for_cost_reports_response = (
    vantage.folders.delete_folder_for_cost_reports(
        folder_token="folder_token_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_token: `str`<a id="folder_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./vantage_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.folders.get_specific_folder`<a id="vantagefoldersget_specific_folder"></a>

Return a specific Folder for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_folder_response = vantage.folders.get_specific_folder(
    folder_token="folder_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_token: `str`<a id="folder_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./vantage_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.folders.list_cost_reports`<a id="vantagefolderslist_cost_reports"></a>

Return all Folders for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_cost_reports_response = vantage.folders.list_cost_reports(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Folders`](./vantage_python_sdk/pydantic/folders.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.folders.update_folder_for_cost_reports`<a id="vantagefoldersupdate_folder_for_cost_reports"></a>

Update a Folder for CostReports.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_folder_for_cost_reports_response = (
    vantage.folders.update_folder_for_cost_reports(
        folder_token="folder_token_example",
        title="string_example",
        parent_folder_token="string_example",
        saved_filter_tokens=["string_example"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### folder_token: `str`<a id="folder_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the Folder.

##### parent_folder_token: `str`<a id="parent_folder_token-str"></a>

The token of the parent Folder.

##### saved_filter_tokens: [`PutFoldersSavedFilterTokens`](./vantage_python_sdk/type/put_folders_saved_filter_tokens.py)<a id="saved_filter_tokens-putfolderssavedfiltertokensvantage_python_sdktypeput_folders_saved_filter_tokenspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutFolders`](./vantage_python_sdk/type/put_folders.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Folder`](./vantage_python_sdk/pydantic/folder.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/folders/{folder_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.notifications.create_report_notification`<a id="vantagenotificationscreate_report_notification"></a>

Create a ReportNotification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_report_notification_response = vantage.notifications.create_report_notification(
    title="string_example",
    cost_report_token="string_example",
    frequency="string_example",
    change="string_example",
    workspace_token="string_example",
    user_tokens=["string_example"],
    recipient_channels=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the ReportNotification.

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

The CostReport token.

##### frequency: `str`<a id="frequency-str"></a>

The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.

##### change: `str`<a id="change-str"></a>

The type of change the ReportNotification is tracking. Possible values: percentage, dollars.

##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the ReportNotification to. Required if the API token is associated with multiple Workspaces.

##### user_tokens: [`PostReportNotificationsUserTokens`](./vantage_python_sdk/type/post_report_notifications_user_tokens.py)<a id="user_tokens-postreportnotificationsusertokensvantage_python_sdktypepost_report_notifications_user_tokenspy"></a>

##### recipient_channels: [`PostReportNotificationsRecipientChannels`](./vantage_python_sdk/type/post_report_notifications_recipient_channels.py)<a id="recipient_channels-postreportnotificationsrecipientchannelsvantage_python_sdktypepost_report_notifications_recipient_channelspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostReportNotifications`](./vantage_python_sdk/type/post_report_notifications.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReportNotification`](./vantage_python_sdk/pydantic/report_notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report_notifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.notifications.delete_report_notification`<a id="vantagenotificationsdelete_report_notification"></a>

Delete a ReportNotification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_report_notification_response = vantage.notifications.delete_report_notification(
    report_notification_token="report_notification_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_notification_token: `str`<a id="report_notification_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReportNotification`](./vantage_python_sdk/pydantic/report_notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report_notifications/{report_notification_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.notifications.get_all_report_notifications`<a id="vantagenotificationsget_all_report_notifications"></a>

Return all ReportNotifications.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_report_notifications_response = (
    vantage.notifications.get_all_report_notifications(
        page=1,
        limit=1,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportNotifications`](./vantage_python_sdk/pydantic/report_notifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report_notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.notifications.get_report_notification`<a id="vantagenotificationsget_report_notification"></a>

Return a ReportNotification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_report_notification_response = vantage.notifications.get_report_notification(
    report_notification_token="report_notification_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_notification_token: `str`<a id="report_notification_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReportNotification`](./vantage_python_sdk/pydantic/report_notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report_notifications/{report_notification_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.notifications.update_report_notification`<a id="vantagenotificationsupdate_report_notification"></a>

Update a ReportNotification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_report_notification_response = vantage.notifications.update_report_notification(
    report_notification_token="report_notification_token_example",
    title="string_example",
    cost_report_token="string_example",
    user_tokens=["string_example"],
    recipient_channels=["string_example"],
    frequency="string_example",
    change="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### report_notification_token: `str`<a id="report_notification_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the ReportNotification.

##### cost_report_token: `str`<a id="cost_report_token-str"></a>

The CostReport token.

##### user_tokens: [`PutReportNotificationsUserTokens`](./vantage_python_sdk/type/put_report_notifications_user_tokens.py)<a id="user_tokens-putreportnotificationsusertokensvantage_python_sdktypeput_report_notifications_user_tokenspy"></a>

##### recipient_channels: [`PutReportNotificationsRecipientChannels`](./vantage_python_sdk/type/put_report_notifications_recipient_channels.py)<a id="recipient_channels-putreportnotificationsrecipientchannelsvantage_python_sdktypeput_report_notifications_recipient_channelspy"></a>

##### frequency: `str`<a id="frequency-str"></a>

The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly.

##### change: `str`<a id="change-str"></a>

The type of change the ReportNotification is tracking. Possible values: percentage, dollars.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutReportNotifications`](./vantage_python_sdk/type/put_report_notifications.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReportNotification`](./vantage_python_sdk/pydantic/report_notification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report_notifications/{report_notification_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.ping.health_check`<a id="vantagepinghealth_check"></a>

This is a health check endpoint that can be used to determine Vantage API healthiness. It will return 200 if everything is running smoothly.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
vantage.ping.health_check()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/ping` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.prices.get_product`<a id="vantagepricesget_product"></a>

Return a product

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_response = vantage.prices.get_product(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Product`](./vantage_python_sdk/pydantic/product.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.prices.get_product_price`<a id="vantagepricesget_product_price"></a>

Returns a price

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_price_response = vantage.prices.get_product_price(
    product_id="product_id_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_id: `str`<a id="product_id-str"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Price`](./vantage_python_sdk/pydantic/price.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{product_id}/prices/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.prices.get_product_prices`<a id="vantagepricesget_product_prices"></a>

Return available Prices across all Regions for a Product.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_prices_response = vantage.prices.get_product_prices(
    product_id="product_id_example",
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_id: `str`<a id="product_id-str"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000

#### 🔄 Return<a id="🔄-return"></a>

[`Prices`](./vantage_python_sdk/pydantic/prices.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{product_id}/prices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.prices.list_available_products`<a id="vantagepriceslist_available_products"></a>

Return available Products for a Service. For example, with a Provider of AWS and a Service of EC2, Products will be a list of all EC2 Instances. By default, this endpoint returns all Products across all Services and Providers but has optional query parameters for filtering listed below.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_available_products_response = vantage.prices.list_available_products(
    provider_id="string_example",
    service_id="string_example",
    name="string_example",
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### provider_id: `str`<a id="provider_id-str"></a>

Query by Provider to list all Products across all Services for a Provider. e.g. aws

##### service_id: `str`<a id="service_id-str"></a>

Query by Service to list all Products for a specific provider service. e.g. aws-ec2

##### name: `str`<a id="name-str"></a>

Query by name of the Product to see a list of products which match that name. e.g. m5a.16xlarge

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000

#### 🔄 Return<a id="🔄-return"></a>

[`Products`](./vantage_python_sdk/pydantic/products.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.segments.create_segment`<a id="vantagesegmentscreate_segment"></a>

Create a Segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_segment_response = vantage.segments.create_segment(
    title="string_example",
    description="string_example",
    priority=1,
    track_unallocated=False,
    report_settings={},
    workspace_token="string_example",
    filter="string_example",
    parent_segment_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

The title of the Segment.

##### description: `str`<a id="description-str"></a>

The description of the Segment.

##### priority: `int`<a id="priority-int"></a>

The priority of the Segment.

##### track_unallocated: `bool`<a id="track_unallocated-bool"></a>

Track Unallocated Costs which are not assigned to any of the created Segments.

##### report_settings: [`PostSegmentsReportSettings`](./vantage_python_sdk/type/post_segments_report_settings.py)<a id="report_settings-postsegmentsreportsettingsvantage_python_sdktypepost_segments_report_settingspy"></a>


##### workspace_token: `str`<a id="workspace_token-str"></a>

The token of the Workspace to add the Segment to. Ignored if 'segment_token' is set. Required if the API token is associated with multiple Workspaces.

##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.

##### parent_segment_token: `str`<a id="parent_segment_token-str"></a>

The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostSegments`](./vantage_python_sdk/type/post_segments.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Segment`](./vantage_python_sdk/pydantic/segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/segments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.segments.get_segment_by_id`<a id="vantagesegmentsget_segment_by_id"></a>

Return a Segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_segment_by_id_response = vantage.segments.get_segment_by_id(
    segment_token="segment_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### segment_token: `str`<a id="segment_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Segment`](./vantage_python_sdk/pydantic/segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/segments/{segment_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.segments.list`<a id="vantagesegmentslist"></a>

Return all Segments.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = vantage.segments.list(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Segments`](./vantage_python_sdk/pydantic/segments.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/segments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.segments.remove_segment`<a id="vantagesegmentsremove_segment"></a>

Delete a Segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_segment_response = vantage.segments.remove_segment(
    segment_token="segment_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### segment_token: `str`<a id="segment_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Segment`](./vantage_python_sdk/pydantic/segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/segments/{segment_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.segments.update_segment_by_id`<a id="vantagesegmentsupdate_segment_by_id"></a>

Update a Segment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_segment_by_id_response = vantage.segments.update_segment_by_id(
    segment_token="segment_token_example",
    title="string_example",
    description="string_example",
    priority=1,
    track_unallocated=False,
    report_settings={},
    filter="string_example",
    parent_segment_token="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### segment_token: `str`<a id="segment_token-str"></a>

##### title: `str`<a id="title-str"></a>

The title of the Segment.

##### description: `str`<a id="description-str"></a>

The description of the Segment.

##### priority: `int`<a id="priority-int"></a>

The priority of the Segment.

##### track_unallocated: `bool`<a id="track_unallocated-bool"></a>

Track Unallocated Costs which are not assigned to any of the created Segments.

##### report_settings: [`PutSegmentsReportSettings`](./vantage_python_sdk/type/put_segments_report_settings.py)<a id="report_settings-putsegmentsreportsettingsvantage_python_sdktypeput_segments_report_settingspy"></a>


##### filter: `str`<a id="filter-str"></a>

The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql.

##### parent_segment_token: `str`<a id="parent_segment_token-str"></a>

The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutSegments`](./vantage_python_sdk/type/put_segments.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Segment`](./vantage_python_sdk/pydantic/segment.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/segments/{segment_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.teams.create_new_team`<a id="vantageteamscreate_new_team"></a>

Create a new Team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_team_response = vantage.teams.create_new_team(
    name="string_example",
    description="string_example",
    workspace_tokens=["string_example"],
    user_tokens=["string_example"],
    user_emails=["string_example"],
    role="owner",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the Team.

##### description: `str`<a id="description-str"></a>

The description of the Team.

##### workspace_tokens: [`PostTeamsWorkspaceTokens`](./vantage_python_sdk/type/post_teams_workspace_tokens.py)<a id="workspace_tokens-postteamsworkspacetokensvantage_python_sdktypepost_teams_workspace_tokenspy"></a>

##### user_tokens: [`PostTeamsUserTokens`](./vantage_python_sdk/type/post_teams_user_tokens.py)<a id="user_tokens-postteamsusertokensvantage_python_sdktypepost_teams_user_tokenspy"></a>

##### user_emails: [`PostTeamsUserEmails`](./vantage_python_sdk/type/post_teams_user_emails.py)<a id="user_emails-postteamsuseremailsvantage_python_sdktypepost_teams_user_emailspy"></a>

##### role: `str`<a id="role-str"></a>

The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostTeams`](./vantage_python_sdk/type/post_teams.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./vantage_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.teams.get_specific_team`<a id="vantageteamsget_specific_team"></a>

Return a specific Team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_team_response = vantage.teams.get_specific_team(
    team_token="team_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_token: `str`<a id="team_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./vantage_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.teams.list_accessible`<a id="vantageteamslist_accessible"></a>

Return all Teams that the current API token has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessible_response = vantage.teams.list_accessible(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Teams`](./vantage_python_sdk/pydantic/teams.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.teams.remove_team`<a id="vantageteamsremove_team"></a>

Delete a Team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_team_response = vantage.teams.remove_team(
    team_token="team_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_token: `str`<a id="team_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./vantage_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.teams.update_team`<a id="vantageteamsupdate_team"></a>

Update a Team.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_team_response = vantage.teams.update_team(
    team_token="team_token_example",
    description="string_example",
    name="string_example",
    workspace_tokens=["string_example"],
    user_tokens=["string_example"],
    user_emails=["string_example"],
    role="owner",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### team_token: `str`<a id="team_token-str"></a>

##### description: `str`<a id="description-str"></a>

The description of the Team.

##### name: `str`<a id="name-str"></a>

The name of the Team.

##### workspace_tokens: [`PutTeamsWorkspaceTokens`](./vantage_python_sdk/type/put_teams_workspace_tokens.py)<a id="workspace_tokens-putteamsworkspacetokensvantage_python_sdktypeput_teams_workspace_tokenspy"></a>

##### user_tokens: [`PutTeamsUserTokens`](./vantage_python_sdk/type/put_teams_user_tokens.py)<a id="user_tokens-putteamsusertokensvantage_python_sdktypeput_teams_user_tokenspy"></a>

##### user_emails: [`PutTeamsUserEmails`](./vantage_python_sdk/type/put_teams_user_emails.py)<a id="user_emails-putteamsuseremailsvantage_python_sdktypeput_teams_user_emailspy"></a>

##### role: `str`<a id="role-str"></a>

The role to assign to the provided Users. Defaults to 'editor' which has editor permissions.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutTeams`](./vantage_python_sdk/type/put_teams.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Team`](./vantage_python_sdk/pydantic/team.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/teams/{team_token}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.users.get_specific_user`<a id="vantageusersget_specific_user"></a>

Return a specific User.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_user_response = vantage.users.get_specific_user(
    user_token="user_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_token: `str`<a id="user_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./vantage_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{user_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.users.list_accessible`<a id="vantageuserslist_accessible"></a>

Return all Users that the current API token has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessible_response = vantage.users.list_accessible(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Users`](./vantage_python_sdk/pydantic/users.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.workspaces.get_specific_workspace`<a id="vantageworkspacesget_specific_workspace"></a>

Return a specific Workspace.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_workspace_response = vantage.workspaces.get_specific_workspace(
    workspace_token="workspace_token_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### workspace_token: `str`<a id="workspace_token-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Workspace`](./vantage_python_sdk/pydantic/workspace.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces/{workspace_token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `vantage.workspaces.list_accessible`<a id="vantageworkspaceslist_accessible"></a>

Return all Workspaces that the current API token has access to.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accessible_response = vantage.workspaces.list_accessible(
    page=1,
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page of results to return.

##### limit: `int`<a id="limit-int"></a>

The amount of results to return. The maximum is 1000.

#### 🔄 Return<a id="🔄-return"></a>

[`Workspaces`](./vantage_python_sdk/pydantic/workspaces.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workspaces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
