# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *


class Application(AviResource):
    resource_name = "application"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    virtualservice_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
    )
    virtualservice_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=virtualservice_uuids_item_schema,
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
        'virtualservice_uuids',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'virtualservice_uuids': virtualservice_uuids_schema,
        'description': description_schema,
    }


def resource_mapping():
    return {
        'Avi::Application': Application,
    }

