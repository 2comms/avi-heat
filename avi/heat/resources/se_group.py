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
from vi_mgr_common import *
from dos import *
from analytics_policy import *


class CustomTag(object):
    # all schemas
    tag_key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    tag_val_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'tag_key',
        'tag_val',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'tag_key': tag_key_schema,
        'tag_val': tag_val_schema,
    }




class VcenterClusters(object):
    # all schemas
    cluster_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    cluster_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=cluster_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    include_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cluster_uuids',
        'include',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cluster_uuids': cluster_uuids_schema,
        'include': include_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'cluster_uuids': 'vimgrclusterruntime',
    }



class VcenterHosts(object):
    # all schemas
    host_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    host_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=host_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    include_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'host_uuids',
        'include',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'host_uuids': host_uuids_schema,
        'include': include_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'host_uuids': 'vimgrhostruntime',
    }



class IptableRule(object):
    # all schemas
    src_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=False,
        update_allowed=True,
    )
    dst_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=False,
        update_allowed=True,
    )
    src_port_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=PortRange.properties_schema,
        required=False,
        update_allowed=True,
    )
    dst_port_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=PortRange.properties_schema,
        required=False,
        update_allowed=True,
    )
    proto_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PROTO_TCP', 'PROTO_UDP', 'PROTO_ICMP', 'PROTO_ALL']),
        ],
    )
    input_interface_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    output_interface_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    action_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['MASQUERADE', 'DROP', 'DNAT', 'ACCEPT', 'REJECT']),
        ],
    )
    dnat_ip_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=False,
        update_allowed=True,
    )
    tag_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'src_ip',
        'dst_ip',
        'src_port',
        'dst_port',
        'proto',
        'input_interface',
        'output_interface',
        'action',
        'dnat_ip',
        'tag',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'src_ip': src_ip_schema,
        'dst_ip': dst_ip_schema,
        'src_port': src_port_schema,
        'dst_port': dst_port_schema,
        'proto': proto_schema,
        'input_interface': input_interface_schema,
        'output_interface': output_interface_schema,
        'action': action_schema,
        'dnat_ip': dnat_ip_schema,
        'tag': tag_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'src_ip': getattr(IpAddrPrefix, 'field_references', {}),
        'dst_ip': getattr(IpAddrPrefix, 'field_references', {}),
        'src_port': getattr(PortRange, 'field_references', {}),
        'dst_port': getattr(PortRange, 'field_references', {}),
        'dnat_ip': getattr(IpAddr, 'field_references', {}),
    }



class IptableRuleSet(object):
    # all schemas
    table_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    chain_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IptableRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'table',
        'chain',
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'table': table_schema,
        'chain': chain_schema,
        'rules': rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'rules': getattr(IptableRule, 'field_references', {}),
    }



class ServiceEngineGroup(AviResource):
    resource_name = "serviceenginegroup"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_vs_per_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of Virtual Services that can be placed on a single Service Engine."),
        required=False,
        update_allowed=True,
    )
    min_scaleout_per_vs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Minimum number of active Service Engines for the Virtual Service."),
        required=False,
        update_allowed=True,
    )
    max_scaleout_per_vs_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of active Service Engines for the Virtual Service."),
        required=False,
        update_allowed=True,
    )
    max_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of Services Engines in this group."),
        required=False,
        update_allowed=True,
    )
    vcpus_per_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of vcpus for each of the Service Engine virtual machines."),
        required=False,
        update_allowed=True,
    )
    memory_per_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Amount of memory for each of the Service Engine virtual machines."),
        required=False,
        update_allowed=True,
    )
    disk_per_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Amount of disk space for each of the Service Engine virtual machines."),
        required=False,
        update_allowed=True,
    )
    max_cpu_usage_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("When CPU utilization exceeds this maximum threshold, Virtual Services hosted on this Service Engine may be rebalanced to other Service Engines to lighten the load. A new Service Engine may be created as part of this process."),
        required=False,
        update_allowed=True,
    )
    min_cpu_usage_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("When CPU utilization falls below the minimum threshold, Virtual Services hosted on this Service Engine may be consolidated onto other underutilized Service Engines.  After consolidation, unused Service Engines may then be eligible for deletion. When CPU utilization exceeds the maximum threshold, Virtual Services hosted on this Service Engine may be migrated to other Service Engines to lighten the load. A new Service Engine may be created as part of this process."),
        required=False,
        update_allowed=True,
    )
    se_deprovision_delay_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Duration to preserve unused Service Engine virtual machines before deleting them. If traffic to a Virtual Service were to spike up abruptly, this Service Engine would still be available to be utilized again rather than creating a new Service Engine."),
        required=False,
        update_allowed=True,
    )
    auto_rebalance_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("If 'Auto Rebalance' is selected, Virtual Services will be automatically migrated when the load on Service Engines falls below the minimum threshold or goes above the maximum threshold. Otherwise, an Alert is generated instead of automatically performing the migration."),
        required=False,
        update_allowed=True,
    )
    se_name_prefix_schema = properties.Schema(
        properties.Schema.STRING,
        _("Prefix to use for virtual machine name of Service Engines."),
        required=False,
        update_allowed=True,
    )
    vs_host_redundancy_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Ensure primary and secondary Service Engines are deployed on different physical hosts."),
        required=False,
        update_allowed=True,
    )
    vcenter_folder_schema = properties.Schema(
        properties.Schema.STRING,
        _("Folder to place all the Service Engine virtual machines in vCenter."),
        required=False,
        update_allowed=True,
    )
    vcenter_datastores_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VcenterDatastore.properties_schema,
        required=True,
        update_allowed=False,
    )
    vcenter_datastores_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=vcenter_datastores_item_schema,
        required=False,
        update_allowed=True,
    )
    vcenter_datastores_include_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcenter_datastore_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['VCENTER_DATASTORE_ANY', 'VCENTER_DATASTORE_LOCAL', 'VCENTER_DATASTORE_SHARED']),
        ],
    )
    vcenter_clusters_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VcenterClusters.properties_schema,
        required=False,
        update_allowed=True,
    )
    vcenter_hosts_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=VcenterHosts.properties_schema,
        required=False,
        update_allowed=True,
    )
    openstack_availability_zone_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    cpu_reserve_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    mem_reserve_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    mgmt_network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Management network to use for Avi Service Engines You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    mgmt_subnet_schema = properties.Schema(
        properties.Schema.MAP,
        _("Management subnet to use for Avi Service Engines"),
        schema=IpAddrPrefix.properties_schema,
        required=False,
        update_allowed=True,
    )
    ha_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("High Availability mode for all the Virtual Services using this Service Engine group."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['HA_MODE_SHARED_PAIR', 'HA_MODE_LEGACY_ACTIVE_STANDBY', 'HA_MODE_SHARED']),
        ],
    )
    algo_schema = properties.Schema(
        properties.Schema.STRING,
        _("If 'compact' placement algorithm is used, Virtual Services are placed on existing Service Engines until they all have the maximum number of Virtual Services. Otherwise, Virtual Services are distributed to as many Service Engines as possible."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PLACEMENT_ALGO_PACKED', 'PLACEMENT_ALGO_DISTRIBUTED']),
        ],
    )
    buffer_se_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Excess Service Engine capacity provisioned for HA failover"),
        required=False,
        update_allowed=True,
    )
    active_standby_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Service Engines in active/standby mode for HA failover"),
        required=False,
        update_allowed=True,
    )
    placement_mode_schema = properties.Schema(
        properties.Schema.STRING,
        _("If placement mode is 'Auto', Virtual Services are automatically placed on Service Engines. If 'Manual' placement mode is selected, user must specify the Service Engine where the Virtual Service should be placed."),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['PLACEMENT_MODE_AUTO', 'PLACEMENT_MODE_MANUAL']),
        ],
    )
    openstack_mgmt_network_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Management network name"),
        required=False,
        update_allowed=True,
    )
    openstack_mgmt_network_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Management network UUID"),
        required=False,
        update_allowed=True,
    )
    instance_flavor_schema = properties.Schema(
        properties.Schema.STRING,
        _("Instance/Flavor type for SE instance"),
        required=False,
        update_allowed=True,
    )
    hypervisor_schema = properties.Schema(
        properties.Schema.STRING,
        _("Override default hypervisor"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEFAULT', 'VMWARE_VSAN', 'VMWARE_ESX', 'KVM']),
        ],
    )
    se_dos_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DosThresholdProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    auto_rebalance_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Frequency of rebalance, if 'Auto rebalance' is enabled"),
        required=False,
        update_allowed=True,
    )
    aggressive_failure_detection_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable aggressive failover configuration for ha."),
        required=False,
        update_allowed=True,
    )
    realtime_se_metrics_schema = properties.Schema(
        properties.Schema.MAP,
        _("Enable or disable real time SE metrics"),
        schema=MetricsRealTimeUpdate.properties_schema,
        required=False,
        update_allowed=True,
    )
    vs_scaleout_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to wait for the scaled out SE to become ready before marking the scaleout done"),
        required=False,
        update_allowed=True,
    )
    vs_scalein_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to wait for the scaled in SE to drain existing flows before marking the scalein done"),
        required=False,
        update_allowed=True,
    )
    hardwaresecuritymodulegroup_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    connection_memory_percentage_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Percentage of memory for connection state. This will come at the expense of memory used for HTTP in-memory cache."),
        required=False,
        update_allowed=True,
    )
    extra_config_multiplier_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Multiplier for extra config to support large VS/Pool config."),
        required=False,
        update_allowed=True,
    )
    vs_scalein_timeout_for_upgrade_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("During SE upgrade, Time to wait for the scaled-in SE to drain existing flows before marking the scalein done"),
        required=False,
        update_allowed=True,
    )
    host_attribute_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Key of a Key,Value pair identifying a set of hosts. Currently used to separate North-South and East-West ServiceEngine sizing requirements, specifically in Container ecosystems, where ServiceEngines on East-West traffic nodes are typically smaller than those on North-South traffic nodes."),
        required=False,
        update_allowed=True,
    )
    host_attribute_value_schema = properties.Schema(
        properties.Schema.STRING,
        _("Value of a Key,Value pair identifying a set of hosts. Currently used to separate North-South and East-West ServiceEngine sizing requirements, specifically in Container ecosystems, where ServiceEngines on East-West traffic nodes are typically smaller than those on North-South traffic nodes."),
        required=False,
        update_allowed=True,
    )
    log_disksz_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum disk capacity (in MB) to be allocated to an SE. This is exclusively used for debug and log data."),
        required=False,
        update_allowed=True,
    )
    os_reserved_memory_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Amount of extra memory to be reserved for use by the Operating System on a Service Engine."),
        required=False,
        update_allowed=True,
    )
    floating_intf_ip_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    floating_intf_ip_schema = properties.Schema(
        properties.Schema.LIST,
        _("If ServiceEngineGroup is configured for Legacy 1+1 Active Standby HA Mode, Floating IP's will be advertised only by the Active SE in the Pair. Virtual Services in this group must be disabled/enabled for any changes to the Floating IP's to take effect. If manual load distribution among the Active Standby ServiceEngines is enabled, Floating IP's provided here will be advertised only by the Active ServiceEngine hosting all the VirtualServices tagged with Active Standby SE 1 Tag."),
        schema=floating_intf_ip_item_schema,
        required=False,
        update_allowed=True,
    )
    hm_on_standby_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable active health monitoring from the standby SE for all placed virtual services."),
        required=False,
        update_allowed=True,
    )
    per_app_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Per-app SE mode is designed for deploying dedicated load balancers per app (VS). In this mode, each SE is limited to a max of 2 VSs. vCPUs in per-app SEs count towards licensing usage at 25% rate."),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The interval between two ping requests sent by the gateway monitor.  If a value is not specified, requests are sent every second (1000 milliseconds)."),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_fail_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive failed gateway health checks before a gateway is marked down."),
        required=False,
        update_allowed=True,
    )
    gateway_monitor_success_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The number of consecutive successful gateway health checks before a gateway that was marked down by the gateway monitor is marked up."),
        required=False,
        update_allowed=True,
    )
    distribute_load_active_standby_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Use both the active and standby Service Engines for Virtual Service placement in the legacy active standby HA mode."),
        required=False,
        update_allowed=True,
    )
    auto_redistribute_active_standby_load_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Redistribution of virtual services from the takeover SE to the replacement SE can cause momentary traffic loss. If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to REST API."),
        required=False,
        update_allowed=True,
    )
    floating_intf_ip_se_2_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    floating_intf_ip_se_2_schema = properties.Schema(
        properties.Schema.LIST,
        _("This field is applicable only if the ServiceEngineGroup is configured for Legacy 1+1 Active Standby HA Mode, with manual load distribution among the Active Standby ServiceEngines enabled. Floating IP's provided here will be advertised only by the Active ServiceEngine hosting all the VirtualServices tagged with Active Standby SE 2 Tag."),
        schema=floating_intf_ip_se_2_item_schema,
        required=False,
        update_allowed=True,
    )
    custom_tag_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CustomTag.properties_schema,
        required=True,
        update_allowed=False,
    )
    custom_tag_schema = properties.Schema(
        properties.Schema.LIST,
        _("Custom tag will be used to create the tags for SE instance in AWS. Note this is not the same as the prefix for SE name"),
        schema=custom_tag_item_schema,
        required=False,
        update_allowed=True,
    )
    dedicated_dispatcher_core_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Dedicate the core that handles packet receive/transmit from the network to just the dispatching function. Don't use it for TCP/IP and SSL functions."),
        required=False,
        update_allowed=True,
    )
    cpu_socket_affinity_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Allocate all the CPU cores for the Service Engine Virtual Machines  on the same CPU socket. Applicable only for vCenter Cloud."),
        required=False,
        update_allowed=True,
    )
    num_flow_cores_sum_changes_to_ignore_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of changes in num flow cores sum to ignore."),
        required=False,
        update_allowed=True,
    )
    iptables_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IptableRuleSet.properties_schema,
        required=True,
        update_allowed=False,
    )
    iptables_schema = properties.Schema(
        properties.Schema.LIST,
        _("Iptable Rules"),
        schema=iptables_item_schema,
        required=False,
        update_allowed=True,
    )
    enable_routing_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable routing for this ServiceEngineGroup "),
        required=False,
        update_allowed=True,
    )
    advertise_backend_networks_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Advertise reach-ability of backend server networks via ADC through BGP for default gateway feature."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'description',
        'max_vs_per_se',
        'min_scaleout_per_vs',
        'max_scaleout_per_vs',
        'max_se',
        'vcpus_per_se',
        'memory_per_se',
        'disk_per_se',
        'max_cpu_usage',
        'min_cpu_usage',
        'se_deprovision_delay',
        'auto_rebalance',
        'se_name_prefix',
        'vs_host_redundancy',
        'vcenter_folder',
        'vcenter_datastores',
        'vcenter_datastores_include',
        'vcenter_datastore_mode',
        'vcenter_clusters',
        'vcenter_hosts',
        'openstack_availability_zone',
        'cpu_reserve',
        'mem_reserve',
        'mgmt_network_uuid',
        'mgmt_subnet',
        'ha_mode',
        'algo',
        'buffer_se',
        'active_standby',
        'placement_mode',
        'openstack_mgmt_network_name',
        'openstack_mgmt_network_uuid',
        'instance_flavor',
        'hypervisor',
        'se_dos_profile',
        'auto_rebalance_interval',
        'aggressive_failure_detection',
        'realtime_se_metrics',
        'vs_scaleout_timeout',
        'vs_scalein_timeout',
        'hardwaresecuritymodulegroup_uuid',
        'connection_memory_percentage',
        'extra_config_multiplier',
        'vs_scalein_timeout_for_upgrade',
        'host_attribute_key',
        'host_attribute_value',
        'log_disksz',
        'os_reserved_memory',
        'floating_intf_ip',
        'hm_on_standby',
        'per_app',
        'gateway_monitor_interval',
        'gateway_monitor_fail_threshold',
        'gateway_monitor_success_threshold',
        'distribute_load_active_standby',
        'auto_redistribute_active_standby_load',
        'floating_intf_ip_se_2',
        'custom_tag',
        'dedicated_dispatcher_core',
        'cpu_socket_affinity',
        'num_flow_cores_sum_changes_to_ignore',
        'iptables',
        'enable_routing',
        'advertise_backend_networks',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'description': description_schema,
        'max_vs_per_se': max_vs_per_se_schema,
        'min_scaleout_per_vs': min_scaleout_per_vs_schema,
        'max_scaleout_per_vs': max_scaleout_per_vs_schema,
        'max_se': max_se_schema,
        'vcpus_per_se': vcpus_per_se_schema,
        'memory_per_se': memory_per_se_schema,
        'disk_per_se': disk_per_se_schema,
        'max_cpu_usage': max_cpu_usage_schema,
        'min_cpu_usage': min_cpu_usage_schema,
        'se_deprovision_delay': se_deprovision_delay_schema,
        'auto_rebalance': auto_rebalance_schema,
        'se_name_prefix': se_name_prefix_schema,
        'vs_host_redundancy': vs_host_redundancy_schema,
        'vcenter_folder': vcenter_folder_schema,
        'vcenter_datastores': vcenter_datastores_schema,
        'vcenter_datastores_include': vcenter_datastores_include_schema,
        'vcenter_datastore_mode': vcenter_datastore_mode_schema,
        'vcenter_clusters': vcenter_clusters_schema,
        'vcenter_hosts': vcenter_hosts_schema,
        'openstack_availability_zone': openstack_availability_zone_schema,
        'cpu_reserve': cpu_reserve_schema,
        'mem_reserve': mem_reserve_schema,
        'mgmt_network_uuid': mgmt_network_uuid_schema,
        'mgmt_subnet': mgmt_subnet_schema,
        'ha_mode': ha_mode_schema,
        'algo': algo_schema,
        'buffer_se': buffer_se_schema,
        'active_standby': active_standby_schema,
        'placement_mode': placement_mode_schema,
        'openstack_mgmt_network_name': openstack_mgmt_network_name_schema,
        'openstack_mgmt_network_uuid': openstack_mgmt_network_uuid_schema,
        'instance_flavor': instance_flavor_schema,
        'hypervisor': hypervisor_schema,
        'se_dos_profile': se_dos_profile_schema,
        'auto_rebalance_interval': auto_rebalance_interval_schema,
        'aggressive_failure_detection': aggressive_failure_detection_schema,
        'realtime_se_metrics': realtime_se_metrics_schema,
        'vs_scaleout_timeout': vs_scaleout_timeout_schema,
        'vs_scalein_timeout': vs_scalein_timeout_schema,
        'hardwaresecuritymodulegroup_uuid': hardwaresecuritymodulegroup_uuid_schema,
        'connection_memory_percentage': connection_memory_percentage_schema,
        'extra_config_multiplier': extra_config_multiplier_schema,
        'vs_scalein_timeout_for_upgrade': vs_scalein_timeout_for_upgrade_schema,
        'host_attribute_key': host_attribute_key_schema,
        'host_attribute_value': host_attribute_value_schema,
        'log_disksz': log_disksz_schema,
        'os_reserved_memory': os_reserved_memory_schema,
        'floating_intf_ip': floating_intf_ip_schema,
        'hm_on_standby': hm_on_standby_schema,
        'per_app': per_app_schema,
        'gateway_monitor_interval': gateway_monitor_interval_schema,
        'gateway_monitor_fail_threshold': gateway_monitor_fail_threshold_schema,
        'gateway_monitor_success_threshold': gateway_monitor_success_threshold_schema,
        'distribute_load_active_standby': distribute_load_active_standby_schema,
        'auto_redistribute_active_standby_load': auto_redistribute_active_standby_load_schema,
        'floating_intf_ip_se_2': floating_intf_ip_se_2_schema,
        'custom_tag': custom_tag_schema,
        'dedicated_dispatcher_core': dedicated_dispatcher_core_schema,
        'cpu_socket_affinity': cpu_socket_affinity_schema,
        'num_flow_cores_sum_changes_to_ignore': num_flow_cores_sum_changes_to_ignore_schema,
        'iptables': iptables_schema,
        'enable_routing': enable_routing_schema,
        'advertise_backend_networks': advertise_backend_networks_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'iptables': getattr(IptableRuleSet, 'field_references', {}),
        'floating_intf_ip_se_2': getattr(IpAddr, 'field_references', {}),
        'hardwaresecuritymodulegroup_uuid': 'hardwaresecuritymodulegroup',
        'vcenter_hosts': getattr(VcenterHosts, 'field_references', {}),
        'custom_tag': getattr(CustomTag, 'field_references', {}),
        'mgmt_network_uuid': 'network',
        'vcenter_datastores': getattr(VcenterDatastore, 'field_references', {}),
        'mgmt_subnet': getattr(IpAddrPrefix, 'field_references', {}),
        'floating_intf_ip': getattr(IpAddr, 'field_references', {}),
        'vcenter_clusters': getattr(VcenterClusters, 'field_references', {}),
        'se_dos_profile': getattr(DosThresholdProfile, 'field_references', {}),
        'realtime_se_metrics': getattr(MetricsRealTimeUpdate, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::ServiceEngineGroup': ServiceEngineGroup,
    }

