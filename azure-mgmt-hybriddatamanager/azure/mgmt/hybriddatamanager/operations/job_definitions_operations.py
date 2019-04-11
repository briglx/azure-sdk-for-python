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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class JobDefinitionsOperations(object):
    """JobDefinitionsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API Version. Constant value: "2016-06-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-06-01"

        self.config = config

    def list_by_data_service(
            self, data_service_name, resource_group_name, data_manager_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """This method gets all the job definitions of the given data service
        name.

        :param data_service_name: The data service type of interest.
        :type data_service_name: str
        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param filter: OData Filter options
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of JobDefinition
        :rtype:
         ~azure.mgmt.hybriddatamanager.models.JobDefinitionPaged[~azure.mgmt.hybriddatamanager.models.JobDefinition]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_data_service.metadata['url']
                path_format_arguments = {
                    'dataServiceName': self._serialize.url("data_service_name", data_service_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.JobDefinitionPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.JobDefinitionPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_data_service.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions'}

    def get(
            self, data_service_name, job_definition_name, resource_group_name, data_manager_name, custom_headers=None, raw=False, **operation_config):
        """This method gets job definition object by name.

        :param data_service_name: The data service name of the job definition
        :type data_service_name: str
        :param job_definition_name: The job definition name that is being
         queried.
        :type job_definition_name: str
        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: JobDefinition or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.hybriddatamanager.models.JobDefinition or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'dataServiceName': self._serialize.url("data_service_name", data_service_name, 'str'),
            'jobDefinitionName': self._serialize.url("job_definition_name", job_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('JobDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}'}


    def _create_or_update_initial(
            self, data_service_name, job_definition_name, job_definition, resource_group_name, data_manager_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'dataServiceName': self._serialize.url("data_service_name", data_service_name, 'str'),
            'jobDefinitionName': self._serialize.url("job_definition_name", job_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        body_content = self._serialize.body(job_definition, 'JobDefinition')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('JobDefinition', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, data_service_name, job_definition_name, job_definition, resource_group_name, data_manager_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates or updates a job definition.

        :param data_service_name: The data service type of the job definition.
        :type data_service_name: str
        :param job_definition_name: The job definition name to be created or
         updated.
        :type job_definition_name: str
        :param job_definition: Job Definition object to be created or updated.
        :type job_definition:
         ~azure.mgmt.hybriddatamanager.models.JobDefinition
        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns JobDefinition or
         ClientRawResponse<JobDefinition> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~azure.mgmt.hybriddatamanager.models.JobDefinition]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~azure.mgmt.hybriddatamanager.models.JobDefinition]]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = self._create_or_update_initial(
            data_service_name=data_service_name,
            job_definition_name=job_definition_name,
            job_definition=job_definition,
            resource_group_name=resource_group_name,
            data_manager_name=data_manager_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('JobDefinition', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}'}


    def _delete_initial(
            self, data_service_name, job_definition_name, resource_group_name, data_manager_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'dataServiceName': self._serialize.url("data_service_name", data_service_name, 'str'),
            'jobDefinitionName': self._serialize.url("job_definition_name", job_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, data_service_name, job_definition_name, resource_group_name, data_manager_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """This method deletes the given job definition.

        :param data_service_name: The data service type of the job definition.
        :type data_service_name: str
        :param job_definition_name: The job definition name to be deleted.
        :type job_definition_name: str
        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = self._delete_initial(
            data_service_name=data_service_name,
            job_definition_name=job_definition_name,
            resource_group_name=resource_group_name,
            data_manager_name=data_manager_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}'}


    def _run_initial(
            self, data_service_name, job_definition_name, run_parameters, resource_group_name, data_manager_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.run.metadata['url']
        path_format_arguments = {
            'dataServiceName': self._serialize.url("data_service_name", data_service_name, 'str'),
            'jobDefinitionName': self._serialize.url("job_definition_name", job_definition_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(run_parameters, 'RunParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def run(
            self, data_service_name, job_definition_name, run_parameters, resource_group_name, data_manager_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """This method runs a job instance of the given job definition.

        :param data_service_name: The data service type of the job definition.
        :type data_service_name: str
        :param job_definition_name: Name of the job definition.
        :type job_definition_name: str
        :param run_parameters: Run time parameters for the job definition.
        :type run_parameters:
         ~azure.mgmt.hybriddatamanager.models.RunParameters
        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = self._run_initial(
            data_service_name=data_service_name,
            job_definition_name=job_definition_name,
            run_parameters=run_parameters,
            resource_group_name=resource_group_name,
            data_manager_name=data_manager_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    run.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/run'}

    def list_by_data_manager(
            self, resource_group_name, data_manager_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """This method gets all the job definitions of the given data manager
        resource.

        :param resource_group_name: The Resource Group Name
        :type resource_group_name: str
        :param data_manager_name: The name of the DataManager Resource within
         the specified resource group. DataManager names must be between 3 and
         24 characters in length and use any alphanumeric and underscore only
        :type data_manager_name: str
        :param filter: OData Filter options
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of JobDefinition
        :rtype:
         ~azure.mgmt.hybriddatamanager.models.JobDefinitionPaged[~azure.mgmt.hybriddatamanager.models.JobDefinition]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_data_manager.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'dataManagerName': self._serialize.url("data_manager_name", data_manager_name, 'str', max_length=24, min_length=3, pattern=r'^[-\w\.]+$')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.JobDefinitionPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.JobDefinitionPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_data_manager.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/jobDefinitions'}
