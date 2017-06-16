# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class ControllerProperties(AviResource):
    resource_name = "controllerproperties"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    dummy_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    unresponsive_se_reboot_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    crashed_se_reboot_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 900)"),
        required=False,
        update_allowed=True,
    )
    se_offline_del_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 172000)"),
        required=False,
        update_allowed=True,
    )
    vs_se_create_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 1500)"),
        required=False,
        update_allowed=True,
    )
    vs_se_vnic_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    vs_se_bootup_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    se_vnic_cooldown_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 120)"),
        required=False,
        update_allowed=True,
    )
    vs_se_vnic_ip_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 120)"),
        required=False,
        update_allowed=True,
    )
    fatal_error_lease_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 120)"),
        required=False,
        update_allowed=True,
    )
    upgrade_lease_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 360)"),
        required=False,
        update_allowed=True,
    )
    query_host_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 180)"),
        required=False,
        update_allowed=True,
    )
    vnic_op_fail_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 180)"),
        required=False,
        update_allowed=True,
    )
    dns_refresh_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    se_create_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 900)"),
        required=False,
        update_allowed=True,
    )
    max_dead_se_in_grp_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Default: 1)"),
        required=False,
        update_allowed=True,
    )
    dead_se_detection_timer_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 360)"),
        required=False,
        update_allowed=True,
    )
    api_idle_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 15)"),
        required=False,
        update_allowed=True,
    )
    allow_unauthenticated_nodes_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(" (Default: False)"),
        required=False,
        update_allowed=True,
    )
    cluster_ip_gratuitous_arp_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    vs_key_rotate_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    secure_channel_controller_token_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    secure_channel_se_token_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    max_seq_vnic_failures_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Default: 3)"),
        required=False,
        update_allowed=True,
    )
    vs_awaiting_se_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    vs_apic_scaleout_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to wait for the scaled out SE to become ready before marking the scaleout done, applies to APIC configuration only (Units: SEC) (Default: 360)"),
        required=False,
        update_allowed=True,
    )
    secure_channel_cleanup_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    attach_ip_retry_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 360)"),
        required=False,
        update_allowed=True,
    )
    attach_ip_retry_limit_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    persistence_key_rotate_period_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: MIN) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    allow_unauthenticated_apis_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Allow unauthenticated access for special APIs (Default: False)"),
        required=False,
        update_allowed=True,
    )
    warmstart_se_reconnect_wait_time_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    vs_se_ping_fail_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(" (Units: SEC) (Default: 60)"),
        required=False,
        update_allowed=True,
    )
    se_failover_attempt_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Interval between attempting failovers to an SE (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    max_pcap_per_tenant_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of pcap files stored per tenant (Default: 4)"),
        required=False,
        update_allowed=True,
    )
    ssl_certificate_expiry_warning_days_item_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Number of days for SSL Certificate expiry warning (Units: DAYS)"),
        required=True,
        update_allowed=False,
    )
    ssl_certificate_expiry_warning_days_schema = properties.Schema(
        properties.Schema.LIST,
        _("Number of days for SSL Certificate expiry warning"),
        schema=ssl_certificate_expiry_warning_days_item_schema,
        required=False,
        update_allowed=True,
    )
    seupgrade_fabric_pool_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Pool size used for all fabric commands during se upgrade. (Default: 20)"),
        required=False,
        update_allowed=True,
    )
    seupgrade_segroup_min_dead_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time to wait before marking segroup upgrade as stuck. (Units: SEC) (Default: 360)"),
        required=False,
        update_allowed=True,
    )
    allow_ip_forwarding_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1)  (Default: False)"),
        required=False,
        update_allowed=True,
    )
    appviewx_compat_mode_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("(Introduced in: 17.1.1) Export configuration in appviewx compatibility mode (Default: False)"),
        required=False,
        update_allowed=True,
    )
    upgrade_dns_ttl_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("(Introduced in: 17.1.1) Time to account for DNS TTL during upgrade. This is in addition to vs_scalein_timeout_for_upgrade in se_group. (Units: SEC) (Default: 5)"),
        required=False,
        update_allowed=True,
    )
    portal_token_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.2) Token used for uploading tech-support to portal"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'avi_version',
        'dummy',
        'unresponsive_se_reboot',
        'crashed_se_reboot',
        'se_offline_del',
        'vs_se_create_fail',
        'vs_se_vnic_fail',
        'vs_se_bootup_fail',
        'se_vnic_cooldown',
        'vs_se_vnic_ip_fail',
        'fatal_error_lease_time',
        'upgrade_lease_time',
        'query_host_fail',
        'vnic_op_fail_time',
        'dns_refresh_period',
        'se_create_timeout',
        'max_dead_se_in_grp',
        'dead_se_detection_timer',
        'api_idle_timeout',
        'allow_unauthenticated_nodes',
        'cluster_ip_gratuitous_arp_period',
        'vs_key_rotate_period',
        'secure_channel_controller_token_timeout',
        'secure_channel_se_token_timeout',
        'max_seq_vnic_failures',
        'vs_awaiting_se_timeout',
        'vs_apic_scaleout_timeout',
        'secure_channel_cleanup_timeout',
        'attach_ip_retry_interval',
        'attach_ip_retry_limit',
        'persistence_key_rotate_period',
        'allow_unauthenticated_apis',
        'warmstart_se_reconnect_wait_time',
        'vs_se_ping_fail',
        'se_failover_attempt_interval',
        'max_pcap_per_tenant',
        'ssl_certificate_expiry_warning_days',
        'seupgrade_fabric_pool_size',
        'seupgrade_segroup_min_dead_timeout',
        'allow_ip_forwarding',
        'appviewx_compat_mode',
        'upgrade_dns_ttl',
        'portal_token',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'dummy': dummy_schema,
        'unresponsive_se_reboot': unresponsive_se_reboot_schema,
        'crashed_se_reboot': crashed_se_reboot_schema,
        'se_offline_del': se_offline_del_schema,
        'vs_se_create_fail': vs_se_create_fail_schema,
        'vs_se_vnic_fail': vs_se_vnic_fail_schema,
        'vs_se_bootup_fail': vs_se_bootup_fail_schema,
        'se_vnic_cooldown': se_vnic_cooldown_schema,
        'vs_se_vnic_ip_fail': vs_se_vnic_ip_fail_schema,
        'fatal_error_lease_time': fatal_error_lease_time_schema,
        'upgrade_lease_time': upgrade_lease_time_schema,
        'query_host_fail': query_host_fail_schema,
        'vnic_op_fail_time': vnic_op_fail_time_schema,
        'dns_refresh_period': dns_refresh_period_schema,
        'se_create_timeout': se_create_timeout_schema,
        'max_dead_se_in_grp': max_dead_se_in_grp_schema,
        'dead_se_detection_timer': dead_se_detection_timer_schema,
        'api_idle_timeout': api_idle_timeout_schema,
        'allow_unauthenticated_nodes': allow_unauthenticated_nodes_schema,
        'cluster_ip_gratuitous_arp_period': cluster_ip_gratuitous_arp_period_schema,
        'vs_key_rotate_period': vs_key_rotate_period_schema,
        'secure_channel_controller_token_timeout': secure_channel_controller_token_timeout_schema,
        'secure_channel_se_token_timeout': secure_channel_se_token_timeout_schema,
        'max_seq_vnic_failures': max_seq_vnic_failures_schema,
        'vs_awaiting_se_timeout': vs_awaiting_se_timeout_schema,
        'vs_apic_scaleout_timeout': vs_apic_scaleout_timeout_schema,
        'secure_channel_cleanup_timeout': secure_channel_cleanup_timeout_schema,
        'attach_ip_retry_interval': attach_ip_retry_interval_schema,
        'attach_ip_retry_limit': attach_ip_retry_limit_schema,
        'persistence_key_rotate_period': persistence_key_rotate_period_schema,
        'allow_unauthenticated_apis': allow_unauthenticated_apis_schema,
        'warmstart_se_reconnect_wait_time': warmstart_se_reconnect_wait_time_schema,
        'vs_se_ping_fail': vs_se_ping_fail_schema,
        'se_failover_attempt_interval': se_failover_attempt_interval_schema,
        'max_pcap_per_tenant': max_pcap_per_tenant_schema,
        'ssl_certificate_expiry_warning_days': ssl_certificate_expiry_warning_days_schema,
        'seupgrade_fabric_pool_size': seupgrade_fabric_pool_size_schema,
        'seupgrade_segroup_min_dead_timeout': seupgrade_segroup_min_dead_timeout_schema,
        'allow_ip_forwarding': allow_ip_forwarding_schema,
        'appviewx_compat_mode': appviewx_compat_mode_schema,
        'upgrade_dns_ttl': upgrade_dns_ttl_schema,
        'portal_token': portal_token_schema,
    }




def resource_mapping():
    return {
        'Avi::LBaaS::ControllerProperties': ControllerProperties,
    }

