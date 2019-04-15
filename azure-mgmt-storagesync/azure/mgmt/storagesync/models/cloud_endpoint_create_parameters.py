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

from .proxy_resource import ProxyResource


class CloudEndpointCreateParameters(ProxyResource):
    """The parameters used when creating a cloud endpoint.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param storage_account_resource_id: Storage Account Resource Id
    :type storage_account_resource_id: str
    :param azure_file_share_name: Azure file share name
    :type azure_file_share_name: str
    :param storage_account_tenant_id: Storage Account Tenant Id
    :type storage_account_tenant_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'storage_account_resource_id': {'key': 'properties.storageAccountResourceId', 'type': 'str'},
        'azure_file_share_name': {'key': 'properties.azureFileShareName', 'type': 'str'},
        'storage_account_tenant_id': {'key': 'properties.storageAccountTenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CloudEndpointCreateParameters, self).__init__(**kwargs)
        self.storage_account_resource_id = kwargs.get('storage_account_resource_id', None)
        self.azure_file_share_name = kwargs.get('azure_file_share_name', None)
        self.storage_account_tenant_id = kwargs.get('storage_account_tenant_id', None)
