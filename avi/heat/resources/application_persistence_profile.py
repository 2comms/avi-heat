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


class HdrPersistenceProfile(object):
    # all schemas
    prst_hdr_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header name for custom header persistence"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prst_hdr_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prst_hdr_name': prst_hdr_name_schema,
    }




class AppCookiePersistenceProfile(object):
    # all schemas
    prst_hdr_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Header or cookie name for application cookie persistence"),
        required=True,
        update_allowed=True,
    )
    timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The length of time after a client's connections have closed before expiring the client's persistence to a server."),
        required=False,
        update_allowed=True,
    )
    encryption_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Key to use for cookie encryption"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'prst_hdr_name',
        'timeout',
        'encryption_key',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'prst_hdr_name': prst_hdr_name_schema,
        'timeout': timeout_schema,
        'encryption_key': encryption_key_schema,
    }




class HttpCookiePersistenceProfile(object):
    # all schemas
    encryption_key_schema = properties.Schema(
        properties.Schema.STRING,
        _("Key to use for cookie encryption"),
        required=False,
        update_allowed=True,
    )
    cookie_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("HTTP cookie name for cookie persistence"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'encryption_key',
        'cookie_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'encryption_key': encryption_key_schema,
        'cookie_name': cookie_name_schema,
    }




class IPPersistenceProfile(object):
    # all schemas
    ip_persistent_timeout_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("The length of time after a client's connections have closed before expiring the client's persistence to a server."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip_persistent_timeout',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip_persistent_timeout': ip_persistent_timeout_schema,
    }




class ApplicationPersistenceProfile(AviResource):
    resource_name = "applicationpersistenceprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("A user-friendly name for the persistence profile."),
        required=True,
        update_allowed=True,
    )
    server_hm_down_recovery_schema = properties.Schema(
        properties.Schema.STRING,
        _("Specifies behavior when a persistent server has been marked down by a health monitor."),
        required=False,
        update_allowed=True,
    )
    persistence_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Method used to persist clients to the same server for a duration of time or a session."),
        required=True,
        update_allowed=True,
    )
    ip_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the Client IP Persistence profile parameters."),
        schema=IPPersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    hdr_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the custom HTTP Header Persistence profile parameters."),
        schema=HdrPersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    app_cookie_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the Application Cookie Persistence profile parameters."),
        schema=AppCookiePersistenceProfile.properties_schema,
        required=False,
        update_allowed=True,
    )
    http_cookie_persistence_profile_schema = properties.Schema(
        properties.Schema.MAP,
        _("Specifies the HTTP Cookie Persistence profile parameters."),
        schema=HttpCookiePersistenceProfile.properties_schema,
        required=False,
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
        'name',
        'server_hm_down_recovery',
        'persistence_type',
        'ip_persistence_profile',
        'hdr_persistence_profile',
        'app_cookie_persistence_profile',
        'http_cookie_persistence_profile',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'server_hm_down_recovery': server_hm_down_recovery_schema,
        'persistence_type': persistence_type_schema,
        'ip_persistence_profile': ip_persistence_profile_schema,
        'hdr_persistence_profile': hdr_persistence_profile_schema,
        'app_cookie_persistence_profile': app_cookie_persistence_profile_schema,
        'http_cookie_persistence_profile': http_cookie_persistence_profile_schema,
        'description': description_schema,
    }




def resource_mapping():
    return {
        'AviBeta16.1::ApplicationPersistenceProfile': ApplicationPersistenceProfile,
    }

