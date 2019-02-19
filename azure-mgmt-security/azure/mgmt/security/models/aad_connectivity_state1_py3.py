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


class AadConnectivityState1(Model):
    """Describes an Azure resource with kind.

    :param connectivity_state: The connectivity state of the external AAD
     solution . Possible values include: 'Discovered', 'NotLicensed',
     'Connected'
    :type connectivity_state: str or
     ~azure.mgmt.security.models.AadConnectivityState
    """

    _attribute_map = {
        'connectivity_state': {'key': 'connectivityState', 'type': 'str'},
    }

    def __init__(self, *, connectivity_state=None, **kwargs) -> None:
        super(AadConnectivityState1, self).__init__(**kwargs)
        self.connectivity_state = connectivity_state
