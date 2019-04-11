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


class AvailableProviderOperation(Model):
    """Class represents provider operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or Sets Name of the operations
    :type name: str
    :param display: Gets or sets Display information
     Contains the localized display information for this particular
     operation/action
    :type display:
     ~azure.mgmt.hybriddatamanager.models.AvailableProviderOperationDisplay
    :param origin: Gets or sets Origin
     The intended executor of the operation; governs the display of the
     operation in the RBAC UX and the audit logs UX.
     Default value is “user,system”
    :type origin: str
    :param properties: Gets or sets Properties
     Reserved for future use
    :type properties: object
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'AvailableProviderOperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(self, *, name: str, display=None, origin: str=None, properties=None, **kwargs) -> None:
        super(AvailableProviderOperation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin
        self.properties = properties
