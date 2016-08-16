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
from controller_properties import *


class CC_AgentProperties(object):
    # all schemas
    poll_duration_target_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Discovery poll target duration; a scale factor of 1+ is computed with the actual discovery (actual/target) and used to tweak slow and fast poll intervals"),
        required=False,
        update_allowed=True,
    )
    poll_slow_target_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Slow poll interval"),
        required=False,
        update_allowed=True,
    )
    poll_fast_target_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Fast poll interval"),
        required=False,
        update_allowed=True,
    )
    async_retries_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum polls to check for async jobs to finish"),
        required=False,
        update_allowed=True,
    )
    async_retries_delay_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Delay between each async job status poll check"),
        required=False,
        update_allowed=True,
    )
    vnic_retries_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum polls to check for vnics to be attached to VM"),
        required=False,
        update_allowed=True,
    )
    vnic_retries_delay_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Delay between each vnic status poll check"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'poll_duration_target',
        'poll_slow_target',
        'poll_fast_target',
        'async_retries',
        'async_retries_delay',
        'vnic_retries',
        'vnic_retries_delay',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'poll_duration_target': poll_duration_target_schema,
        'poll_slow_target': poll_slow_target_schema,
        'poll_fast_target': poll_fast_target_schema,
        'async_retries': async_retries_schema,
        'async_retries_delay': async_retries_delay_schema,
        'vnic_retries': vnic_retries_schema,
        'vnic_retries_delay': vnic_retries_delay_schema,
    }




class Hypervisor_Properties(object):
    # all schemas
    htype_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['DEFAULT', 'VMWARE_VSAN', 'VMWARE_ESX', 'KVM']),
        ],
    )
    max_nics_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_ips_per_nic_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'htype',
        'max_nics',
        'max_ips_per_nic',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'htype': htype_schema,
        'max_nics': max_nics_schema,
        'max_ips_per_nic': max_ips_per_nic_schema,
    }




class CC_Properties(object):
    # all schemas
    rpc_poll_interval_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    rpc_queue_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'rpc_poll_interval',
        'rpc_queue_size',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rpc_poll_interval': rpc_poll_interval_schema,
        'rpc_queue_size': rpc_queue_size_schema,
    }




class CloudMeta(object):
    # all schemas
    key_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    value_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'key',
        'value',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'key': key_schema,
        'value': value_schema,
    }




class CloudFlavor(object):
    # all schemas
    id_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    ram_mb_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    disk_gb_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    vcpus_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    public_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_nics_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    max_ips_per_nic_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=False,
        update_allowed=True,
    )
    enhanced_nw_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    meta_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CloudMeta.properties_schema,
        required=True,
        update_allowed=False,
    )
    meta_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=meta_item_schema,
        required=False,
        update_allowed=True,
    )
    cost_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'id',
        'name',
        'ram_mb',
        'disk_gb',
        'vcpus',
        'public',
        'max_nics',
        'max_ips_per_nic',
        'enhanced_nw',
        'meta',
        'cost',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'id': id_schema,
        'name': name_schema,
        'ram_mb': ram_mb_schema,
        'disk_gb': disk_gb_schema,
        'vcpus': vcpus_schema,
        'public': public_schema,
        'max_nics': max_nics_schema,
        'max_ips_per_nic': max_ips_per_nic_schema,
        'enhanced_nw': enhanced_nw_schema,
        'meta': meta_schema,
        'cost': cost_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'meta': getattr(CloudMeta, 'field_references', {}),
    }



class CloudInfo(object):
    # all schemas
    vtype_schema = properties.Schema(
        properties.Schema.STRING,
        _("Cloud type"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['CLOUD_VCENTER', 'CLOUD_DOCKER_UCP', 'CLOUD_APIC', 'CLOUD_OPENSTACK', 'CLOUD_MESOS', 'CLOUD_RANCHER', 'CLOUD_VCA', 'CLOUD_AWS', 'CLOUD_OSHIFT_K8S', 'CLOUD_LINUXSERVER', 'CLOUD_NONE']),
        ],
    )
    htypes_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['DEFAULT', 'VMWARE_VSAN', 'VMWARE_ESX', 'KVM']),
        ],
    )
    htypes_schema = properties.Schema(
        properties.Schema.LIST,
        _("Supported hypervisors"),
        schema=htypes_item_schema,
        required=False,
        update_allowed=True,
    )
    flavor_regex_filter_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )
    flavor_props_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CloudFlavor.properties_schema,
        required=True,
        update_allowed=False,
    )
    flavor_props_schema = properties.Schema(
        properties.Schema.LIST,
        _("Flavor properties specific to this cloud type"),
        schema=flavor_props_item_schema,
        required=False,
        update_allowed=True,
    )
    cca_props_schema = properties.Schema(
        properties.Schema.MAP,
        _("CloudConnectorAgent properties specific to this cloud type"),
        schema=CC_AgentProperties.properties_schema,
        required=False,
        update_allowed=True,
    )
    controller_props_schema = properties.Schema(
        properties.Schema.MAP,
        _("Controller properties specific to this cloud type"),
        schema=ControllerProperties.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'vtype',
        'htypes',
        'flavor_regex_filter',
        'flavor_props',
        'cca_props',
        'controller_props',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'vtype': vtype_schema,
        'htypes': htypes_schema,
        'flavor_regex_filter': flavor_regex_filter_schema,
        'flavor_props': flavor_props_schema,
        'cca_props': cca_props_schema,
        'controller_props': controller_props_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'flavor_props': getattr(CloudFlavor, 'field_references', {}),
        'cca_props': getattr(CC_AgentProperties, 'field_references', {}),
        'controller_props': getattr(ControllerProperties, 'field_references', {}),
    }



class CloudProperties(AviResource):
    resource_name = "cloudproperties"
    # all schemas
    cc_vtypes_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
        constraints=[
            constraints.AllowedValues(['CLOUD_VCENTER', 'CLOUD_DOCKER_UCP', 'CLOUD_APIC', 'CLOUD_OPENSTACK', 'CLOUD_MESOS', 'CLOUD_RANCHER', 'CLOUD_VCA', 'CLOUD_AWS', 'CLOUD_OSHIFT_K8S', 'CLOUD_LINUXSERVER', 'CLOUD_NONE']),
        ],
    )
    cc_vtypes_schema = properties.Schema(
        properties.Schema.LIST,
        _("Cloud types supported by CloudConnector"),
        schema=cc_vtypes_item_schema,
        required=False,
        update_allowed=True,
    )
    hyp_props_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=Hypervisor_Properties.properties_schema,
        required=True,
        update_allowed=False,
    )
    hyp_props_schema = properties.Schema(
        properties.Schema.LIST,
        _("Hypervisor properties"),
        schema=hyp_props_item_schema,
        required=False,
        update_allowed=True,
    )
    cc_props_schema = properties.Schema(
        properties.Schema.MAP,
        _("CloudConnector properties"),
        schema=CC_Properties.properties_schema,
        required=False,
        update_allowed=True,
    )
    info_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CloudInfo.properties_schema,
        required=True,
        update_allowed=False,
    )
    info_schema = properties.Schema(
        properties.Schema.LIST,
        _("Properties specific to a cloud type"),
        schema=info_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'cc_vtypes',
        'hyp_props',
        'cc_props',
        'info',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'cc_vtypes': cc_vtypes_schema,
        'hyp_props': hyp_props_schema,
        'cc_props': cc_props_schema,
        'info': info_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'info': getattr(CloudInfo, 'field_references', {}),
        'hyp_props': getattr(Hypervisor_Properties, 'field_references', {}),
        'cc_props': getattr(CC_Properties, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::CloudProperties': CloudProperties,
    }

