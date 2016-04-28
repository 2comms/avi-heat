# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *
from vs_runtime import *
from vs import *


class VsInitialPlacementEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    rpc_status_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'rpc_status',
        'error_message',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'rpc_status': rpc_status_schema,
        'error_message': error_message_schema,
    }


class VsScaleOutEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    rpc_status_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )
    scale_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ScaleStatus.properties_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'rpc_status',
        'error_message',
        'scale_status',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'rpc_status': rpc_status_schema,
        'error_message': error_message_schema,
        'scale_status': scale_status_schema,
    }


class VsScaleInEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    rpc_status_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )
    scale_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ScaleStatus.properties_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'rpc_status',
        'error_message',
        'scale_status',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'rpc_status': rpc_status_schema,
        'error_message': error_message_schema,
        'scale_status': scale_status_schema,
    }


class VsErrorEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    rpc_status_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'rpc_status',
        'error_message',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'rpc_status': rpc_status_schema,
        'error_message': error_message_schema,
    }


class VsFsmEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    vs_rt_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceRuntime.properties_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'vs_rt',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'vs_rt': vs_rt_schema,
    }


class VsMigrateEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    rpc_status_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
    )
    error_message_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )
    scale_status_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ScaleStatus.properties_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'rpc_status',
        'error_message',
        'scale_status',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'rpc_status': rpc_status_schema,
        'error_message': error_message_schema,
        'scale_status': scale_status_schema,
    }


class VsPoolNwFilterEventDetails(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    filter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    network_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'filter',
        'network',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'filter': filter_schema,
        'network': network_schema,
    }


class VsAwaitingSeEventDetails(object):
    # all schemas
    vs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    se_requested_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VirtualServiceResource.properties_schema,
        required=False,
    )
    se_assigned_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VsSeAssigned.properties_schema,
        required=True,
    )
    se_assigned_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=se_assigned_item_schema,
        required=False,
    )
    awaitingse_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
    )

    # properties list
    PROPERTIES = (
        'vs_uuid',
        'se_requested',
        'se_assigned',
        'awaitingse_timeout',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vs_uuid': vs_uuid_schema,
        'se_requested': se_requested_schema,
        'se_assigned': se_assigned_schema,
        'awaitingse_timeout': awaitingse_timeout_schema,
    }
