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


class TCPProxyProfile(object):
    # all schemas
    automatic_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Dynamically pick the relevant parameters for connections. (Default: True)"),
        required=False,
        update_allowed=True,
    )
    idle_connection_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Controls the behavior of idle connections. (Default: KEEP_ALIVE)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['KEEP_ALIVE', 'CLOSE_IDLE']),
        ],
    )
    idle_connection_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The duration for keepalive probes or session idle timeout. Max value is 3600 seconds, min is 60.  Set to 0 to allow infinite idle time. (Units: SEC) (Default: 600)"),
        required=False,
        update_allowed=True,
    )
    ignore_time_wait_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("A new SYN is accepted from the same 4-tuple even if there is already a connection in TIME_WAIT state.  This is equivalent of setting Time Wait Delay to 0 (Default: False)"),
        required=False,
        update_allowed=True,
    )
    time_wait_delay_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The time (in millisec) to wait before closing a connection in the TIME_WAIT state. (Units: MILLISECONDS) (Default: 2000)"),
        required=False,
        update_allowed=True,
    )
    max_retransmissions_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of attempts at retransmit before closing the connection. (Default: 8)"),
        required=False,
        update_allowed=True,
    )
    max_syn_retransmissions_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The maximum number of attempts at retransmitting a SYN packet before giving up. (Default: 8)"),
        required=False,
        update_allowed=True,
    )
    receive_window_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Size of the receive window. (Units: KB) (Default: 64)"),
        required=False,
        update_allowed=True,
    )
    use_interface_mtu_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Use the interface MTU to calculate the TCP max segment size. (Default: True)"),
        required=False,
        update_allowed=True,
    )
    max_segment_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum TCP segment size. (Units: BYTES)"),
        required=False,
        update_allowed=True,
    )
    nagles_algorithm_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Consolidates small data packets to send clients fewer but larger packets.  Adversely affects real time protocols such as telnet or SSH. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    ip_dscp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Controls the value of the Differentiated Services Code Point field inserted in the IP header.  This has two options:  Set to a specific value, or Pass Through, which uses the incoming DSCP value. (Default: 0)"),
        required=False,
        update_allowed=True,
    )
    cc_algo_schema = properties.Schema(
        properties.Schema.STRING,
        _("Controls the congestion control algorithm we use. (Default: CC_ALGO_NEW_RENO)"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['CC_ALGO_NEW_RENO', 'CC_ALGO_HTCP', 'CC_ALGO_CUBIC']),
        ],
    )
    aggressive_congestion_avoidance_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Controls the our congestion window to send, normally it's 1 mss, If this option is turned on, we use 10 msses (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'automatic',
        'idle_connection_type',
        'idle_connection_timeout',
        'ignore_time_wait',
        'time_wait_delay',
        'max_retransmissions',
        'max_syn_retransmissions',
        'receive_window',
        'use_interface_mtu',
        'max_segment_size',
        'nagles_algorithm',
        'ip_dscp',
        'cc_algo',
        'aggressive_congestion_avoidance',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'automatic': automatic_schema,
        'idle_connection_type': idle_connection_type_schema,
        'idle_connection_timeout': idle_connection_timeout_schema,
        'ignore_time_wait': ignore_time_wait_schema,
        'time_wait_delay': time_wait_delay_schema,
        'max_retransmissions': max_retransmissions_schema,
        'max_syn_retransmissions': max_syn_retransmissions_schema,
        'receive_window': receive_window_schema,
        'use_interface_mtu': use_interface_mtu_schema,
        'max_segment_size': max_segment_size_schema,
        'nagles_algorithm': nagles_algorithm_schema,
        'ip_dscp': ip_dscp_schema,
        'cc_algo': cc_algo_schema,
        'aggressive_congestion_avoidance': aggressive_congestion_avoidance_schema,
    }




class UDPFastPathProfile(object):
    # all schemas
    session_idle_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The amount of time (in sec) for which a flow needs to be idle before it is deleted. (Units: SEC) (Default: 10)"),
        required=False,
        update_allowed=True,
    )
    per_pkt_loadbalance_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When enabled, every UDP packet is considered a new transaction and may be load balanced to a different server.  When disabled, packets from the same client source IP and port are sent to the same server. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    snat_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When disabled, Source NAT will not be performed for all client UDP packets (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'session_idle_timeout',
        'per_pkt_loadbalance',
        'snat',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'session_idle_timeout': session_idle_timeout_schema,
        'per_pkt_loadbalance': per_pkt_loadbalance_schema,
        'snat': snat_schema,
    }




class TCPFastPathProfile(object):
    # all schemas
    session_idle_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The amount of time (in sec) for which a connection needs to be idle before it is eligible to be deleted. (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    enable_syn_protection_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("When enabled, Avi will complete the 3-way handshake with the client before forwarding any packets to the server.  This will protect the server from SYN flood and half open SYN connections. (Default: False)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'session_idle_timeout',
        'enable_syn_protection',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'session_idle_timeout': session_idle_timeout_schema,
        'enable_syn_protection': enable_syn_protection_schema,
    }




class NetworkProfileUnion(object):
    # all schemas
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Configure one of either proxy or fast path profiles. (Default: PROTOCOL_TYPE_TCP_PROXY)"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PROTOCOL_TYPE_TCP_FAST_PATH', 'PROTOCOL_TYPE_TCP_PROXY', 'PROTOCOL_TYPE_UDP_FAST_PATH']),
        ],
    )
    tcp_proxy_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TCPProxyProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    tcp_fast_path_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TCPFastPathProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    udp_fast_path_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=UDPFastPathProfile.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'type',
        'tcp_proxy_profile',
        'tcp_fast_path_profile',
        'udp_fast_path_profile',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'type': type_schema,
        'tcp_proxy_profile': tcp_proxy_profile_schema,
        'tcp_fast_path_profile': tcp_fast_path_profile_schema,
        'udp_fast_path_profile': udp_fast_path_profile_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'tcp_proxy_profile': getattr(TCPProxyProfile, 'field_references', {}),
        'tcp_fast_path_profile': getattr(TCPFastPathProfile, 'field_references', {}),
        'udp_fast_path_profile': getattr(UDPFastPathProfile, 'field_references', {}),
    }



class NetworkProfile(AviResource):
    resource_name = "networkprofile"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the network profile."),
        required=True,
        update_allowed=True,
    )
    profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=NetworkProfileUnion.properties_schema,
        required=True,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'name',
        'profile',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'profile': profile_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'profile': getattr(NetworkProfileUnion, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::NetworkProfile': NetworkProfile,
    }

