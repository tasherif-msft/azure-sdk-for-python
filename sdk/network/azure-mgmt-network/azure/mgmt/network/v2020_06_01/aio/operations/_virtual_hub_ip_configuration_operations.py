# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class VirtualHubIpConfigurationOperations:
    """VirtualHubIpConfigurationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2020_06_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        ip_config_name: str,
        **kwargs
    ) -> "_models.HubIpConfiguration":
        """Retrieves the details of a Virtual Hub Ip configuration.

        :param resource_group_name: The resource group name of the VirtualHub.
        :type resource_group_name: str
        :param virtual_hub_name: The name of the VirtualHub.
        :type virtual_hub_name: str
        :param ip_config_name: The name of the ipconfig.
        :type ip_config_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HubIpConfiguration, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_06_01.models.HubIpConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.HubIpConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
            'ipConfigName': self._serialize.url("ip_config_name", ip_config_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('HubIpConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations/{ipConfigName}'}  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        ip_config_name: str,
        parameters: "_models.HubIpConfiguration",
        **kwargs
    ) -> "_models.HubIpConfiguration":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.HubIpConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
            'ipConfigName': self._serialize.url("ip_config_name", ip_config_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'HubIpConfiguration')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('HubIpConfiguration', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('HubIpConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations/{ipConfigName}'}  # type: ignore

    async def begin_create_or_update(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        ip_config_name: str,
        parameters: "_models.HubIpConfiguration",
        **kwargs
    ) -> AsyncLROPoller["_models.HubIpConfiguration"]:
        """Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing
        VirtualHubIpConfiguration.

        :param resource_group_name: The resource group name of the VirtualHub.
        :type resource_group_name: str
        :param virtual_hub_name: The name of the VirtualHub.
        :type virtual_hub_name: str
        :param ip_config_name: The name of the ipconfig.
        :type ip_config_name: str
        :param parameters: Hub Ip Configuration parameters.
        :type parameters: ~azure.mgmt.network.v2020_06_01.models.HubIpConfiguration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either HubIpConfiguration or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2020_06_01.models.HubIpConfiguration]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.HubIpConfiguration"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                virtual_hub_name=virtual_hub_name,
                ip_config_name=ip_config_name,
                parameters=parameters,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('HubIpConfiguration', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
            'ipConfigName': self._serialize.url("ip_config_name", ip_config_name, 'str'),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations/{ipConfigName}'}  # type: ignore

    async def _delete_initial(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        ip_config_name: str,
        **kwargs
    ) -> None:
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        accept = "application/json"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
            'ipConfigName': self._serialize.url("ip_config_name", ip_config_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations/{ipConfigName}'}  # type: ignore

    async def begin_delete(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        ip_config_name: str,
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Deletes a VirtualHubIpConfiguration.

        :param resource_group_name: The resource group name of the VirtualHubBgpConnection.
        :type resource_group_name: str
        :param virtual_hub_name: The name of the VirtualHub.
        :type virtual_hub_name: str
        :param ip_config_name: The name of the ipconfig.
        :type ip_config_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the AsyncARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                virtual_hub_name=virtual_hub_name,
                ip_config_name=ip_config_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
            'ipConfigName': self._serialize.url("ip_config_name", ip_config_name, 'str'),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations/{ipConfigName}'}  # type: ignore

    def list(
        self,
        resource_group_name: str,
        virtual_hub_name: str,
        **kwargs
    ) -> AsyncIterable["_models.ListVirtualHubIpConfigurationResults"]:
        """Retrieves the details of all VirtualHubIpConfigurations.

        :param resource_group_name: The resource group name of the VirtualHub.
        :type resource_group_name: str
        :param virtual_hub_name: The name of the VirtualHub.
        :type virtual_hub_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ListVirtualHubIpConfigurationResults or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_06_01.models.ListVirtualHubIpConfigurationResults]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListVirtualHubIpConfigurationResults"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-06-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'virtualHubName': self._serialize.url("virtual_hub_name", virtual_hub_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ListVirtualHubIpConfigurationResults', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}/ipConfigurations'}  # type: ignore
