# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class LinkedServiceOperations:
    """LinkedServiceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_linked_services_by_workspace(
        self,
        **kwargs
    ) -> AsyncIterable["models.LinkedServiceListResponse"]:
        """Lists linked services.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LinkedServiceListResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.synapse.artifacts.models.LinkedServiceListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.LinkedServiceListResponse"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.get_linked_services_by_workspace.metadata['url']  # type: ignore
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('LinkedServiceListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.CloudError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_linked_services_by_workspace.metadata = {'url': '/linkedservices'}  # type: ignore

    async def create_or_update_linked_service(
        self,
        linked_service_name: str,
        properties: "models.LinkedService",
        if_match: Optional[str] = None,
        **kwargs
    ) -> "models.LinkedServiceResource":
        """Creates or updates a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param properties: Properties of linked service.
        :type properties: ~azure.synapse.artifacts.models.LinkedService
        :param if_match: ETag of the linkedService entity.  Should only be specified for update, for
         which it should match existing entity or can be * for unconditional update.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.LinkedServiceResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.LinkedServiceResource"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _linked_service = models.LinkedServiceResource(properties=properties)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update_linked_service.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_linked_service, 'LinkedServiceResource')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore

    async def get_linked_service(
        self,
        linked_service_name: str,
        if_none_match: Optional[str] = None,
        **kwargs
    ) -> Optional["models.LinkedServiceResource"]:
        """Gets a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :param if_none_match: ETag of the linked service entity. Should only be specified for get. If
         the ETag matches the existing entity tag, or if * was provided, then no content will be
         returned.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LinkedServiceResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.LinkedServiceResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.LinkedServiceResource"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.get_linked_service.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LinkedServiceResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore

    async def delete_linked_service(
        self,
        linked_service_name: str,
        **kwargs
    ) -> None:
        """Deletes a linked service.

        :param linked_service_name: The linked service name.
        :type linked_service_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.delete_linked_service.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'linkedServiceName': self._serialize.url("linked_service_name", linked_service_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_linked_service.metadata = {'url': '/linkedservices/{linkedServiceName}'}  # type: ignore