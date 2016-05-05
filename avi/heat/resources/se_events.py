# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *
from pool import *
from application_persistence_profile import *
from health_monitor_runtime import *
from log_common import *


class SeThreshEventDetails(object):
    # all schemas
    thresh_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    curr_value_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'thresh',
        'curr_value',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'thresh': thresh_schema,
        'curr_value': curr_value_schema,
    }




class SePersistenceEventDetails(object):
    # all schemas
    pool_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of pool whose persistence table limits were reached"),
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of persistence"),
        required=False,
        update_allowed=True,
    )
    entries_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Current number of entries in the client ip persistence table"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool',
        'type',
        'entries',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool': pool_schema,
        'type': type_schema,
        'entries': entries_schema,
    }




class SeHmEventShmDetails(object):
    # all schemas
    health_monitor_schema = properties.Schema(
        properties.Schema.STRING,
        _("Health Monitor name"),
        required=True,
        update_allowed=True,
    )
    average_response_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Average health monitor response time from server in milli-seconds"),
        required=False,
        update_allowed=True,
    )
    resp_string_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'health_monitor',
        'average_response_time',
        'resp_string',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'health_monitor': health_monitor_schema,
        'average_response_time': average_response_time_schema,
        'resp_string': resp_string_schema,
    }




class SeDupipEventDetails(object):
    # all schemas
    vnic_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic name"),
        required=False,
        update_allowed=True,
    )
    vnic_ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic IP"),
        required=False,
        update_allowed=True,
    )
    remote_mac_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mac Address"),
        required=False,
        update_allowed=True,
    )
    local_mac_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mac Address"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vnic_name',
        'vnic_ip',
        'remote_mac',
        'local_mac',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vnic_name': vnic_name_schema,
        'vnic_ip': vnic_ip_schema,
        'remote_mac': remote_mac_schema,
        'local_mac': local_mac_schema,
    }




class SePoolLbEventDetails(object):
    # all schemas
    pool_schema = properties.Schema(
        properties.Schema.STRING,
        _("Pool name"),
        required=False,
        update_allowed=True,
    )
    reason_schema = properties.Schema(
        properties.Schema.STRING,
        _("Reason for Load balancing failure"),
        required=False,
        update_allowed=True,
    )
    failure_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("Reason code for load balancing failure"),
        required=False,
        update_allowed=True,
    )
    virtual_service_schema = properties.Schema(
        properties.Schema.STRING,
        _("Virtual Service name"),
        required=False,
        update_allowed=True,
    )
    src_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of event generator"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool',
        'reason',
        'failure_code',
        'virtual_service',
        'src_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool': pool_schema,
        'reason': reason_schema,
        'failure_code': failure_code_schema,
        'virtual_service': virtual_service_schema,
        'src_uuid': src_uuid_schema,
    }




class SeIpRemovedEventDetails(object):
    # all schemas
    se_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the SE responsible for this event"),
        required=False,
        update_allowed=True,
    )
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic name"),
        required=False,
        update_allowed=True,
    )
    linux_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic linux name"),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("IP added"),
        required=False,
        update_allowed=True,
    )
    mask_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Mask "),
        required=False,
        update_allowed=True,
    )
    mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("DCHP or Static"),
        required=False,
        update_allowed=True,
    )
    ns_schema = properties.Schema(
        properties.Schema.STRING,
        _("Namespace"),
        required=False,
        update_allowed=True,
    )
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network UUID"),
        required=False,
        update_allowed=True,
    )
    mac_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mac Address"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_uuid',
        'if_name',
        'linux_name',
        'ip',
        'mask',
        'mode',
        'ns',
        'network_uuid',
        'mac',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_uuid': se_uuid_schema,
        'if_name': if_name_schema,
        'linux_name': linux_name_schema,
        'ip': ip_schema,
        'mask': mask_schema,
        'mode': mode_schema,
        'ns': ns_schema,
        'network_uuid': network_uuid_schema,
        'mac': mac_schema,
    }




class SeIpAddedEventDetails(object):
    # all schemas
    se_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the SE responsible for this event"),
        required=False,
        update_allowed=True,
    )
    if_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic name"),
        required=False,
        update_allowed=True,
    )
    linux_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic linux name"),
        required=False,
        update_allowed=True,
    )
    ip_schema = properties.Schema(
        properties.Schema.STRING,
        _("IP added"),
        required=False,
        update_allowed=True,
    )
    mask_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Mask "),
        required=False,
        update_allowed=True,
    )
    mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("DCHP or Static"),
        required=False,
        update_allowed=True,
    )
    ns_schema = properties.Schema(
        properties.Schema.STRING,
        _("Namespace"),
        required=False,
        update_allowed=True,
    )
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network UUID"),
        required=False,
        update_allowed=True,
    )
    mac_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mac Address"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_uuid',
        'if_name',
        'linux_name',
        'ip',
        'mask',
        'mode',
        'ns',
        'network_uuid',
        'mac',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_uuid': se_uuid_schema,
        'if_name': if_name_schema,
        'linux_name': linux_name_schema,
        'ip': ip_schema,
        'mask': mask_schema,
        'mode': mode_schema,
        'ns': ns_schema,
        'network_uuid': network_uuid_schema,
        'mac': mac_schema,
    }




class SeHmEventServerDetails(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP address of server"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Port override form the pool port. If server port is not specified, the pool port is used."),
        required=False,
        update_allowed=True,
    )
    hostname_schema = properties.Schema(
        properties.Schema.STRING,
        _("Host name or VM name or DNS name for the server"),
        required=False,
        update_allowed=True,
    )
    failure_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("Healthmonitor Failure code"),
        required=False,
        update_allowed=True,
    )
    app_info_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AppInfo.properties_schema,
        required=True,
        update_allowed=False,
    )
    app_info_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=app_info_item_schema,
        required=False,
        update_allowed=True,
    )
    shm_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SeHmEventShmDetails.properties_schema,
        required=True,
        update_allowed=False,
    )
    shm_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=shm_item_schema,
        required=False,
        update_allowed=True,
    )
    ssl_error_code_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip',
        'port',
        'hostname',
        'failure_code',
        'app_info',
        'shm',
        'ssl_error_code',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'port': port_schema,
        'hostname': hostname_schema,
        'failure_code': failure_code_schema,
        'app_info': app_info_schema,
        'shm': shm_schema,
        'ssl_error_code': ssl_error_code_schema,
    }




class SeHBEventDetails(object):
    # all schemas
    se_uuid1_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the SE responsible for this event"),
        required=False,
        update_allowed=True,
    )
    se_uuid2_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of a SE in the SE-Group which failed to respond"),
        required=False,
        update_allowed=True,
    )
    hb_type_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("HB Request/Response not received"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_uuid1',
        'se_uuid2',
        'hb_type',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_uuid1': se_uuid1_schema,
        'se_uuid2': se_uuid2_schema,
        'hb_type': hb_type_schema,
    }




class SeHmEventVsDetails(object):
    # all schemas
    virtual_service_schema = properties.Schema(
        properties.Schema.STRING,
        _("Virtual Service name"),
        required=False,
        update_allowed=True,
    )
    reason_schema = properties.Schema(
        properties.Schema.STRING,
        _("Reason for Virtual Service Down"),
        required=False,
        update_allowed=True,
    )
    se_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Service Engine name"),
        required=False,
        update_allowed=True,
    )
    ha_reason_schema = properties.Schema(
        properties.Schema.STRING,
        _("HA Compromised reason"),
        required=False,
        update_allowed=True,
    )
    src_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the event generator"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'virtual_service',
        'reason',
        'se_name',
        'ha_reason',
        'src_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'virtual_service': virtual_service_schema,
        'reason': reason_schema,
        'se_name': se_name_schema,
        'ha_reason': ha_reason_schema,
        'src_uuid': src_uuid_schema,
    }




class SeIpfailureEventDetails(object):
    # all schemas
    se_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the SE responsible for this event"),
        required=False,
        update_allowed=True,
    )
    vnic_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Vnic name"),
        required=False,
        update_allowed=True,
    )
    network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Network UUID"),
        required=False,
        update_allowed=True,
    )
    mac_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mac Address"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'se_uuid',
        'vnic_name',
        'network_uuid',
        'mac',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'se_uuid': se_uuid_schema,
        'vnic_name': vnic_name_schema,
        'network_uuid': network_uuid_schema,
        'mac': mac_schema,
    }




class SeHmEventPoolDetails(object):
    # all schemas
    pool_schema = properties.Schema(
        properties.Schema.STRING,
        _("Pool name"),
        required=False,
        update_allowed=True,
    )
    server_schema = properties.Schema(
        properties.Schema.MAP,
        _("Server details"),
        schema=SeHmEventServerDetails.properties_schema,
        required=False,
        update_allowed=True,
    )
    virtual_service_schema = properties.Schema(
        properties.Schema.STRING,
        _("Virtual service name"),
        required=False,
        update_allowed=True,
    )
    se_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Service Engine"),
        required=False,
        update_allowed=True,
    )
    ha_reason_schema = properties.Schema(
        properties.Schema.STRING,
        _("HA Compromised reason"),
        required=False,
        update_allowed=True,
    )
    percent_servers_up_schema = properties.Schema(
        properties.Schema.STRING,
        _("Percentage of servers up"),
        required=False,
        update_allowed=True,
    )
    src_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the event generator"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'pool',
        'server',
        'virtual_service',
        'se_name',
        'ha_reason',
        'percent_servers_up',
        'src_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'pool': pool_schema,
        'server': server_schema,
        'virtual_service': virtual_service_schema,
        'se_name': se_name_schema,
        'ha_reason': ha_reason_schema,
        'percent_servers_up': percent_servers_up_schema,
        'src_uuid': src_uuid_schema,
    }


