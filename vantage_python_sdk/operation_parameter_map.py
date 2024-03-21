operation_parameter_map = {
    '/access_grants-POST': {
        'parameters': [
            {
                'name': 'resource_token'
            },
            {
                'name': 'team_token'
            },
            {
                'name': 'access'
            },
        ]
    },
    '/access_grants/{access_grant_token}-DELETE': {
        'parameters': [
            {
                'name': 'access_grant_token'
            },
        ]
    },
    '/access_grants/{access_grant_token}-GET': {
        'parameters': [
            {
                'name': 'access_grant_token'
            },
        ]
    },
    '/access_grants-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/access_grants/{access_grant_token}-PUT': {
        'parameters': [
            {
                'name': 'access'
            },
            {
                'name': 'access_grant_token'
            },
        ]
    },
    '/business_metrics-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'cost_report_tokens_with_metadata'
            },
            {
                'name': 'values'
            },
        ]
    },
    '/business_metrics/{business_metric_token}-DELETE': {
        'parameters': [
            {
                'name': 'business_metric_token'
            },
        ]
    },
    '/business_metrics-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/business_metrics/{business_metric_token}-GET': {
        'parameters': [
            {
                'name': 'business_metric_token'
            },
        ]
    },
    '/business_metrics/{business_metric_token}-PUT': {
        'parameters': [
            {
                'name': 'business_metric_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'cost_report_tokens_with_metadata'
            },
            {
                'name': 'values'
            },
        ]
    },
    '/business_metrics/{business_metric_token}/values.csv-PUT': {
        'parameters': [
            {
                'name': 'business_metric_token'
            },
            {
                'name': 'csv'
            },
        ]
    },
    '/dashboards-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'widget_tokens'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'date_bin'
            },
            {
                'name': 'date_interval'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'workspace_token'
            },
        ]
    },
    '/cost_reports-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'workspace_token'
            },
            {
                'name': 'groupings'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'business_metric_tokens_with_metadata'
            },
            {
                'name': 'folder_token'
            },
            {
                'name': 'settings'
            },
        ]
    },
    '/cost_reports/{cost_report_token}-DELETE': {
        'parameters': [
            {
                'name': 'cost_report_token'
            },
        ]
    },
    '/dashboards/{dashboard_token}-DELETE': {
        'parameters': [
            {
                'name': 'dashboard_token'
            },
        ]
    },
    '/dashboards-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/cost_reports-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/cost_reports/{cost_report_token}-GET': {
        'parameters': [
            {
                'name': 'cost_report_token'
            },
        ]
    },
    '/dashboards/{dashboard_token}-GET': {
        'parameters': [
            {
                'name': 'dashboard_token'
            },
        ]
    },
    '/costs-GET': {
        'parameters': [
            {
                'name': 'cost_report_token'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'groupings'
            },
            {
                'name': 'order'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/dashboards/{dashboard_token}-PUT': {
        'parameters': [
            {
                'name': 'end_date'
            },
            {
                'name': 'dashboard_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'widget_tokens'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'date_bin'
            },
            {
                'name': 'date_interval'
            },
            {
                'name': 'start_date'
            },
        ]
    },
    '/cost_reports/{cost_report_token}-PUT': {
        'parameters': [
            {
                'name': 'cost_report_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'groupings'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'business_metric_tokens_with_metadata'
            },
            {
                'name': 'folder_token'
            },
            {
                'name': 'settings'
            },
        ]
    },
    '/dashboards-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'widget_tokens'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'date_bin'
            },
            {
                'name': 'date_interval'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'workspace_token'
            },
        ]
    },
    '/dashboards/{dashboard_token}-DELETE': {
        'parameters': [
            {
                'name': 'dashboard_token'
            },
        ]
    },
    '/dashboards-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/dashboards/{dashboard_token}-GET': {
        'parameters': [
            {
                'name': 'dashboard_token'
            },
        ]
    },
    '/dashboards/{dashboard_token}-PUT': {
        'parameters': [
            {
                'name': 'end_date'
            },
            {
                'name': 'dashboard_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'widget_tokens'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'date_bin'
            },
            {
                'name': 'date_interval'
            },
            {
                'name': 'start_date'
            },
        ]
    },
    '/saved_filters-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'workspace_token'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/saved_filters/{saved_filter_token}-DELETE': {
        'parameters': [
            {
                'name': 'saved_filter_token'
            },
        ]
    },
    '/saved_filters-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/saved_filters/{saved_filter_token}-GET': {
        'parameters': [
            {
                'name': 'saved_filter_token'
            },
        ]
    },
    '/saved_filters/{saved_filter_token}-PUT': {
        'parameters': [
            {
                'name': 'saved_filter_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/folders-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'parent_folder_token'
            },
            {
                'name': 'saved_filter_tokens'
            },
            {
                'name': 'workspace_token'
            },
        ]
    },
    '/folders/{folder_token}-DELETE': {
        'parameters': [
            {
                'name': 'folder_token'
            },
        ]
    },
    '/folders/{folder_token}-GET': {
        'parameters': [
            {
                'name': 'folder_token'
            },
        ]
    },
    '/folders-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/folders/{folder_token}-PUT': {
        'parameters': [
            {
                'name': 'folder_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'parent_folder_token'
            },
            {
                'name': 'saved_filter_tokens'
            },
        ]
    },
    '/report_notifications-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'cost_report_token'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'change'
            },
            {
                'name': 'workspace_token'
            },
            {
                'name': 'user_tokens'
            },
            {
                'name': 'recipient_channels'
            },
        ]
    },
    '/report_notifications/{report_notification_token}-DELETE': {
        'parameters': [
            {
                'name': 'report_notification_token'
            },
        ]
    },
    '/report_notifications-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/report_notifications/{report_notification_token}-GET': {
        'parameters': [
            {
                'name': 'report_notification_token'
            },
        ]
    },
    '/report_notifications/{report_notification_token}-PUT': {
        'parameters': [
            {
                'name': 'report_notification_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'cost_report_token'
            },
            {
                'name': 'user_tokens'
            },
            {
                'name': 'recipient_channels'
            },
            {
                'name': 'frequency'
            },
            {
                'name': 'change'
            },
        ]
    },
    '/ping-GET': {
        'parameters': [
        ]
    },
    '/products/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/products/{product_id}/prices/{id}-GET': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/products/{product_id}/prices-GET': {
        'parameters': [
            {
                'name': 'product_id'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/products-GET': {
        'parameters': [
            {
                'name': 'provider_id'
            },
            {
                'name': 'service_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/segments-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'track_unallocated'
            },
            {
                'name': 'report_settings'
            },
            {
                'name': 'workspace_token'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'parent_segment_token'
            },
        ]
    },
    '/segments/{segment_token}-GET': {
        'parameters': [
            {
                'name': 'segment_token'
            },
        ]
    },
    '/segments-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/segments/{segment_token}-DELETE': {
        'parameters': [
            {
                'name': 'segment_token'
            },
        ]
    },
    '/segments/{segment_token}-PUT': {
        'parameters': [
            {
                'name': 'segment_token'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'priority'
            },
            {
                'name': 'track_unallocated'
            },
            {
                'name': 'report_settings'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'parent_segment_token'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'workspace_tokens'
            },
            {
                'name': 'user_tokens'
            },
            {
                'name': 'user_emails'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/teams/{team_token}-GET': {
        'parameters': [
            {
                'name': 'team_token'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/teams/{team_token}-DELETE': {
        'parameters': [
            {
                'name': 'team_token'
            },
        ]
    },
    '/teams/{team_token}-PUT': {
        'parameters': [
            {
                'name': 'team_token'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'workspace_tokens'
            },
            {
                'name': 'user_tokens'
            },
            {
                'name': 'user_emails'
            },
            {
                'name': 'role'
            },
        ]
    },
    '/users/{user_token}-GET': {
        'parameters': [
            {
                'name': 'user_token'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/workspaces/{workspace_token}-GET': {
        'parameters': [
            {
                'name': 'workspace_token'
            },
        ]
    },
    '/workspaces-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
};