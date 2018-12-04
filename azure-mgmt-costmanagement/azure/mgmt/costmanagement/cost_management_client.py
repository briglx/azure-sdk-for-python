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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
import uuid
from .operations.report_config_operations import ReportConfigOperations
from .operations.billing_account_dimensions_operations import BillingAccountDimensionsOperations
from .operations.subscription_dimensions_operations import SubscriptionDimensionsOperations
from .operations.resource_group_dimensions_operations import ResourceGroupDimensionsOperations
from .operations.operations import Operations
from . import models


class CostManagementClientConfiguration(AzureConfiguration):
    """Configuration for CostManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(CostManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-costmanagement/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class CostManagementClient(SDKClient):
    """CostManagementClient

    :ivar config: Configuration for client.
    :vartype config: CostManagementClientConfiguration

    :ivar report_config: ReportConfig operations
    :vartype report_config: azure.mgmt.costmanagement.operations.ReportConfigOperations
    :ivar billing_account_dimensions: BillingAccountDimensions operations
    :vartype billing_account_dimensions: azure.mgmt.costmanagement.operations.BillingAccountDimensionsOperations
    :ivar subscription_dimensions: SubscriptionDimensions operations
    :vartype subscription_dimensions: azure.mgmt.costmanagement.operations.SubscriptionDimensionsOperations
    :ivar resource_group_dimensions: ResourceGroupDimensions operations
    :vartype resource_group_dimensions: azure.mgmt.costmanagement.operations.ResourceGroupDimensionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.costmanagement.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = CostManagementClientConfiguration(credentials, subscription_id, base_url)
        super(CostManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-05-31'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.report_config = ReportConfigOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_account_dimensions = BillingAccountDimensionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.subscription_dimensions = SubscriptionDimensionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_group_dimensions = ResourceGroupDimensionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)

    def query_subscription(
            self, parameters, custom_headers=None, raw=False, **operation_config):
        """Lists the usage data for subscriptionId.

        :param parameters: Parameters supplied to the CreateOrUpdate Report
         Config operation.
        :type parameters:
         ~azure.mgmt.costmanagement.models.ReportConfigDefinition
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Query
        :rtype:
         ~azure.mgmt.costmanagement.models.QueryPaged[~azure.mgmt.costmanagement.models.Query]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.query_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct body
            body_content = self._serialize.body(parameters, 'ReportConfigDefinition')

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters, body_content)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.QueryPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.QueryPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    query_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Query'}

    def query_resource_group(
            self, resource_group_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Lists the usage data for subscriptionId and resource group.

        :param resource_group_name: Azure Resource Group Name.
        :type resource_group_name: str
        :param parameters: Parameters supplied to the CreateOrUpdate Report
         Config operation.
        :type parameters:
         ~azure.mgmt.costmanagement.models.ReportConfigDefinition
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Query
        :rtype:
         ~azure.mgmt.costmanagement.models.QueryPaged[~azure.mgmt.costmanagement.models.Query]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.query_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct body
            body_content = self._serialize.body(parameters, 'ReportConfigDefinition')

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters, body_content)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.QueryPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.QueryPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    query_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Query'}

    def query_billing_account(
            self, billing_account_id, parameters, custom_headers=None, raw=False, **operation_config):
        """Lists the usage data for billing account.

        :param billing_account_id: BillingAccount ID
        :type billing_account_id: str
        :param parameters: Parameters supplied to the CreateOrUpdate Report
         Config operation.
        :type parameters:
         ~azure.mgmt.costmanagement.models.ReportConfigDefinition
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Query
        :rtype:
         ~azure.mgmt.costmanagement.models.QueryPaged[~azure.mgmt.costmanagement.models.Query]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.costmanagement.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.query_billing_account.metadata['url']
                path_format_arguments = {
                    'billingAccountId': self._serialize.url("billing_account_id", billing_account_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct body
            body_content = self._serialize.body(parameters, 'ReportConfigDefinition')

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters, body_content)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.QueryPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.QueryPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    query_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Query'}