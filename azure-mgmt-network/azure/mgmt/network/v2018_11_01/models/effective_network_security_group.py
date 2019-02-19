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


class EffectiveNetworkSecurityGroup(Model):
    """Effective network security group.

    :param network_security_group: The ID of network security group that is
     applied.
    :type network_security_group:
     ~azure.mgmt.network.v2018_11_01.models.SubResource
    :param association: Associated resources.
    :type association:
     ~azure.mgmt.network.v2018_11_01.models.EffectiveNetworkSecurityGroupAssociation
    :param effective_security_rules: A collection of effective security rules.
    :type effective_security_rules:
     list[~azure.mgmt.network.v2018_11_01.models.EffectiveNetworkSecurityRule]
    :param tag_map: Mapping of tags to list of IP Addresses included within
     the tag.
    :type tag_map: dict[str, list[str]]
    """

    _attribute_map = {
        'network_security_group': {'key': 'networkSecurityGroup', 'type': 'SubResource'},
        'association': {'key': 'association', 'type': 'EffectiveNetworkSecurityGroupAssociation'},
        'effective_security_rules': {'key': 'effectiveSecurityRules', 'type': '[EffectiveNetworkSecurityRule]'},
        'tag_map': {'key': 'tagMap', 'type': '{[str]}'},
    }

    def __init__(self, **kwargs):
        super(EffectiveNetworkSecurityGroup, self).__init__(**kwargs)
        self.network_security_group = kwargs.get('network_security_group', None)
        self.association = kwargs.get('association', None)
        self.effective_security_rules = kwargs.get('effective_security_rules', None)
        self.tag_map = kwargs.get('tag_map', None)
