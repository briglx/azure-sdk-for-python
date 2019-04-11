# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AvailableProviderOperationDisplay(Model):
    """Contains the localized display information for this particular operation /
    action.
    These value will be used by several clients for
    (1) custom role definitions for RBAC;
    (2) complex query filters for the event service; and (3) audit history /
    records for management operations.

    :param provider: Gets or sets Provider
     The localized friendly form of the resource provider name – it is expected
     to also include the publisher/company responsible.
     It should use Title Casing and begin with “Microsoft” for 1st party
     services.
    :type provider: str
    :param resource: Gets or sets Resource
     The localized friendly form of the resource type related to this
     action/operation – it should match the public documentation for the
     resource provider.
     It should use Title Casing – for examples, please refer to the “name”
     section.
    :type resource: str
    :param operation: Gets or sets Operation
     The localized friendly name for the operation, as it should be shown to
     the user.
     It should be concise (to fit in drop downs) but clear (i.e.
     self-documenting). It should use Title Casing and include the
     entity/resource to which it applies.
    :type operation: str
    :param description: Gets or sets Description
     The localized friendly description for the operation, as it should be
     shown to the user.
     It should be thorough, yet concise – it will be used in tool tips and
     detailed views.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AvailableProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)
