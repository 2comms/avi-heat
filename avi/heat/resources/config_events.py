# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class ConfigUserPasswordChangeRequest(object):
    # all schemas
    user_email_schema = properties.Schema(
        properties.Schema.STRING,
        _("Email address of user"),
        required=False,
    )
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Matched username of email address"),
        required=False,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("client ip"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Password link is sent or rejected"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'user_email',
        'user',
        'client_ip',
        'status',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'user_email': user_email_schema,
        'user': user_schema,
        'client_ip': client_ip_schema,
        'status': status_schema,
    }


class ConfigUserLogin(object):
    # all schemas
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("client ip"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("error message if authentication failed"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'user',
        'status',
        'client_ip',
        'error_message',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'user': user_schema,
        'status': status_schema,
        'client_ip': client_ip_schema,
        'error_message': error_message_schema,
    }


class ConfigActionDetails(object):
    # all schemas
    path_schema = properties.Schema(
        properties.Schema.STRING,
        _("API path"),
        required=False,
    )
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    resource_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Config type of the resource"),
        required=False,
    )
    resource_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the resource"),
        required=False,
    )
    action_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the action"),
        required=False,
    )
    parameter_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Parameter data"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("Error message if request failed"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'path',
        'user',
        'status',
        'resource_type',
        'resource_name',
        'action_name',
        'parameter_data',
        'error_message',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'path': path_schema,
        'user': user_schema,
        'status': status_schema,
        'resource_type': resource_type_schema,
        'resource_name': resource_name_schema,
        'action_name': action_name_schema,
        'parameter_data': parameter_data_schema,
        'error_message': error_message_schema,
    }


class ConfigUpdateDetails(object):
    # all schemas
    path_schema = properties.Schema(
        properties.Schema.STRING,
        _("API path"),
        required=False,
    )
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    resource_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Config type of the updated resource"),
        required=False,
    )
    resource_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the created resource"),
        required=False,
    )
    request_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request data if request failed"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("Error message if request failed"),
        required=False,
    )
    new_resource_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("New updated data of the resource"),
        required=False,
    )
    old_resource_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Old & overwritten data of the resource"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'path',
        'user',
        'status',
        'resource_type',
        'resource_name',
        'request_data',
        'error_message',
        'new_resource_data',
        'old_resource_data',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'path': path_schema,
        'user': user_schema,
        'status': status_schema,
        'resource_type': resource_type_schema,
        'resource_name': resource_name_schema,
        'request_data': request_data_schema,
        'error_message': error_message_schema,
        'new_resource_data': new_resource_data_schema,
        'old_resource_data': old_resource_data_schema,
    }


class ConfigDeleteDetails(object):
    # all schemas
    path_schema = properties.Schema(
        properties.Schema.STRING,
        _("API path"),
        required=False,
    )
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    resource_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Config type of the deleted resource"),
        required=False,
    )
    resource_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the deleted resource"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("Error message if request failed"),
        required=False,
    )
    resource_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Deleted data of the resource"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'path',
        'user',
        'status',
        'resource_type',
        'resource_name',
        'error_message',
        'resource_data',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'path': path_schema,
        'user': user_schema,
        'status': status_schema,
        'resource_type': resource_type_schema,
        'resource_name': resource_name_schema,
        'error_message': error_message_schema,
        'resource_data': resource_data_schema,
    }


class ConfigCreateDetails(object):
    # all schemas
    path_schema = properties.Schema(
        properties.Schema.STRING,
        _("API path"),
        required=False,
    )
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    resource_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Config type of the created resource"),
        required=False,
    )
    resource_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the created resource"),
        required=False,
    )
    request_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request data if request failed"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("Error message if request failed"),
        required=False,
    )
    resource_data_schema = properties.Schema(
        properties.Schema.STRING,
        _("Data of the created resource"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'path',
        'user',
        'status',
        'resource_type',
        'resource_name',
        'request_data',
        'error_message',
        'resource_data',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'path': path_schema,
        'user': user_schema,
        'status': status_schema,
        'resource_type': resource_type_schema,
        'resource_name': resource_name_schema,
        'request_data': request_data_schema,
        'error_message': error_message_schema,
        'resource_data': resource_data_schema,
    }


class ConfigUserLogout(object):
    # all schemas
    user_schema = properties.Schema(
        properties.Schema.STRING,
        _("Request user"),
        required=False,
    )
    status_schema = properties.Schema(
        properties.Schema.STRING,
        _("Status"),
        required=False,
    )
    client_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("client ip"),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _("error message if logging out failed"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'user',
        'status',
        'client_ip',
        'error_message',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'user': user_schema,
        'status': status_schema,
        'client_ip': client_ip_schema,
        'error_message': error_message_schema,
    }
