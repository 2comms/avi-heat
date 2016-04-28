# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from common import *
from options import *
from match import *
from action import *
from rate import *


class HTTPSecurityAction(object):
    # all schemas
    action_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of the security action to perform"),
        required=True,
    )
    status_code_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP status code to use for local response"),
        required=False,
    )
    https_port_schema = properties.Schema(
        properties.Schema.MAP,
        _("Secure SSL/TLS port to redirect the HTTP request to"),
        schema=Port.properties_schema,
        required=False,
    )
    file_schema = properties.Schema(
        properties.Schema.MAP,
        _("File to be used for generating HTTP local response"),
        schema=HTTPLocalFile.properties_schema,
        required=False,
    )
    rate_limit_schema = properties.Schema(
        properties.Schema.MAP,
        _("Rate Limit profile to be used to rate-limit the flow"),
        schema=RateProfile.properties_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'action',
        'status_code',
        'https_port',
        'file',
        'rate_limit',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'action': action_schema,
        'status_code': status_code_schema,
        'https_port': https_port_schema,
        'file': file_schema,
        'rate_limit': rate_limit_schema,
    }


class HTTPPolicies(object):
    # all schemas
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the virtual service HTTP policy collection"),
        required=True,
    )
    http_policy_set_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of the virtual service HTTP policy collection"),
        required=True,
    )

    # properties list
    PROPERTIES = (
        'index',
        'http_policy_set_uuid',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'index': index_schema,
        'http_policy_set_uuid': http_policy_set_uuid_schema,
    }


class HTTPRequestRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule"),
        required=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=MatchTarget.properties_schema,
        required=False,
    )
    redirect_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP redirect action"),
        schema=HTTPRedirectAction.properties_schema,
        required=False,
    )
    hdr_action_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPHdrAction.properties_schema,
        required=True,
    )
    hdr_action_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP header rewrite action"),
        schema=hdr_action_item_schema,
        required=False,
    )
    rewrite_url_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP request URL rewrite action"),
        schema=HTTPRewriteURLAction.properties_schema,
        required=False,
    )
    switching_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Content switching action"),
        schema=HTTPSwitchingAction.properties_schema,
        required=False,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log all HTTP headers upon rule match"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'redirect_action',
        'hdr_action',
        'rewrite_url_action',
        'switching_action',
        'log',
        'all_headers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'redirect_action': redirect_action_schema,
        'hdr_action': hdr_action_schema,
        'rewrite_url_action': rewrite_url_action_schema,
        'switching_action': switching_action_schema,
        'log': log_schema,
        'all_headers': all_headers_schema,
    }


class HTTPResponseRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule"),
        required=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=ResponseMatchTarget.properties_schema,
        required=False,
    )
    hdr_action_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPHdrAction.properties_schema,
        required=True,
    )
    hdr_action_schema = properties.Schema(
        properties.Schema.LIST,
        _("HTTP header rewrite action"),
        schema=hdr_action_item_schema,
        required=False,
    )
    loc_hdr_action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Location header rewrite action"),
        schema=HTTPRewriteLocHdrAction.properties_schema,
        required=False,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
    )
    all_headers_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log all HTTP headers upon rule match"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'hdr_action',
        'loc_hdr_action',
        'log',
        'all_headers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'hdr_action': hdr_action_schema,
        'loc_hdr_action': loc_hdr_action_schema,
        'log': log_schema,
        'all_headers': all_headers_schema,
    }


class HTTPSecurityRule(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the rule"),
        required=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Index of the rule"),
        required=True,
    )
    enable_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable or disable the rule"),
        required=True,
    )
    match_schema = properties.Schema(
        properties.Schema.MAP,
        _("Add match criteria to the rule"),
        schema=MatchTarget.properties_schema,
        required=False,
    )
    action_schema = properties.Schema(
        properties.Schema.MAP,
        _("Action to be performed upon successful matching"),
        schema=HTTPSecurityAction.properties_schema,
        required=False,
    )
    log_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Log HTTP request upon rule match"),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'enable',
        'match',
        'action',
        'log',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'enable': enable_schema,
        'match': match_schema,
        'action': action_schema,
        'log': log_schema,
    }


class HTTPRequestPolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPRequestRule.properties_schema,
        required=True,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP request policy"),
        schema=rules_item_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }


class HTTPSecurityPolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPSecurityRule.properties_schema,
        required=True,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP security policy"),
        schema=rules_item_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }


class HTTPResponsePolicy(object):
    # all schemas
    rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPResponseRule.properties_schema,
        required=True,
    )
    rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Add rules to the HTTP response policy"),
        schema=rules_item_schema,
        required=False,
    )

    # properties list
    PROPERTIES = (
        'rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'rules': rules_schema,
    }


class HTTPPolicySet(AviResource):
    resource_name = "httppolicyset"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Name of the HTTP Policy Set"),
        required=True,
    )
    http_security_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP security policy for the virtual service."),
        schema=HTTPSecurityPolicy.properties_schema,
        required=False,
    )
    http_request_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP request policy for the virtual service."),
        schema=HTTPRequestPolicy.properties_schema,
        required=False,
    )
    http_response_policy_schema = properties.Schema(
        properties.Schema.MAP,
        _("HTTP response policy for the virtual service."),
        schema=HTTPResponsePolicy.properties_schema,
        required=False,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("Creator name"),
        required=False,
    )
    cloud_config_cksum_schema = properties.Schema(
        properties.Schema.STRING,
        _("Checksum of cloud configuration for Pool. Internally set by cloud connector"),
        required=False,
    )
    is_internal_policy_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'http_security_policy',
        'http_request_policy',
        'http_response_policy',
        'created_by',
        'cloud_config_cksum',
        'is_internal_policy',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'http_security_policy': http_security_policy_schema,
        'http_request_policy': http_request_policy_schema,
        'http_response_policy': http_response_policy_schema,
        'created_by': created_by_schema,
        'cloud_config_cksum': cloud_config_cksum_schema,
        'is_internal_policy': is_internal_policy_schema,
        'description': description_schema,
    }


def resource_mapping():
    return {
        'Avi::HTTPPolicySet': HTTPPolicySet,
    }

