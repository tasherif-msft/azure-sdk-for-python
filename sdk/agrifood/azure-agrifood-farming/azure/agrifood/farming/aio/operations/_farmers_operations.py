# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FarmersOperations:
    """FarmersOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.agrifood.farming.models
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

    def list(
        self,
        ids: Optional[List[str]] = None,
        names: Optional[List[str]] = None,
        property_filters: Optional[List[str]] = None,
        statuses: Optional[List[str]] = None,
        min_created_date_time: Optional[datetime.datetime] = None,
        max_created_date_time: Optional[datetime.datetime] = None,
        min_last_modified_date_time: Optional[datetime.datetime] = None,
        max_last_modified_date_time: Optional[datetime.datetime] = None,
        max_page_size: Optional[int] = 50,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.FarmerListResponse"]:
        """Returns a paginated list of farmer resources.

        :param ids: Ids of the resource.
        :type ids: list[str]
        :param names: Names of the resource.
        :type names: list[str]
        :param property_filters: Filters on key-value pairs within the Properties object.
         eg. "{testKey} eq {testValue}".
        :type property_filters: list[str]
        :param statuses: Statuses of the resource.
        :type statuses: list[str]
        :param min_created_date_time: Minimum creation date of resource (inclusive).
        :type min_created_date_time: ~datetime.datetime
        :param max_created_date_time: Maximum creation date of resource (inclusive).
        :type max_created_date_time: ~datetime.datetime
        :param min_last_modified_date_time: Minimum last modified date of resource (inclusive).
        :type min_last_modified_date_time: ~datetime.datetime
        :param max_last_modified_date_time: Maximum last modified date of resource (inclusive).
        :type max_last_modified_date_time: ~datetime.datetime
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50.
        :type max_page_size: int
        :param skip_token: Skip token for getting next set of results.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FarmerListResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.agrifood.farming.models.FarmerListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FarmerListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if ids is not None:
                    query_parameters['ids'] = [self._serialize.query("ids", q, 'str') if q is not None else '' for q in ids]
                if names is not None:
                    query_parameters['names'] = [self._serialize.query("names", q, 'str') if q is not None else '' for q in names]
                if property_filters is not None:
                    query_parameters['propertyFilters'] = [self._serialize.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
                if statuses is not None:
                    query_parameters['statuses'] = [self._serialize.query("statuses", q, 'str') if q is not None else '' for q in statuses]
                if min_created_date_time is not None:
                    query_parameters['minCreatedDateTime'] = self._serialize.query("min_created_date_time", min_created_date_time, 'iso-8601')
                if max_created_date_time is not None:
                    query_parameters['maxCreatedDateTime'] = self._serialize.query("max_created_date_time", max_created_date_time, 'iso-8601')
                if min_last_modified_date_time is not None:
                    query_parameters['minLastModifiedDateTime'] = self._serialize.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
                if max_last_modified_date_time is not None:
                    query_parameters['maxLastModifiedDateTime'] = self._serialize.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
                if max_page_size is not None:
                    query_parameters['$maxPageSize'] = self._serialize.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('FarmerListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/farmers'}  # type: ignore

    async def get(
        self,
        farmer_id: str,
        **kwargs: Any
    ) -> "_models.Farmer":
        """Gets a specified farmer resource.

        :param farmer_id: ID of the associated farmer.
        :type farmer_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Farmer, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.Farmer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Farmer"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Farmer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/farmers/{farmerId}'}  # type: ignore

    async def create_or_update(
        self,
        farmer_id: str,
        farmer: Optional["_models.Farmer"] = None,
        **kwargs: Any
    ) -> "_models.Farmer":
        """Creates or updates a farmer resource.

        :param farmer_id: ID of the farmer resource.
        :type farmer_id: str
        :param farmer: Farmer resource payload to create or update.
        :type farmer: ~azure.agrifood.farming.models.Farmer
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Farmer, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.Farmer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Farmer"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        content_type = kwargs.pop("content_type", "application/merge-patch+json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
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
        if farmer is not None:
            body_content = self._serialize.body(farmer, 'Farmer')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('Farmer', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Farmer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/farmers/{farmerId}'}  # type: ignore

    async def delete(
        self,
        farmer_id: str,
        **kwargs: Any
    ) -> None:
        """Deletes a specified farmer resource.

        :param farmer_id: ID of farmer to be deleted.
        :type farmer_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
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

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/farmers/{farmerId}'}  # type: ignore

    async def get_cascade_delete_job_details(
        self,
        job_id: str,
        **kwargs: Any
    ) -> "_models.CascadeDeleteJob":
        """Get a cascade delete job for specified farmer.

        :param job_id: ID of the job.
        :type job_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CascadeDeleteJob, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.CascadeDeleteJob
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CascadeDeleteJob"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_cascade_delete_job_details.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'jobId': self._serialize.url("job_id", job_id, 'str'),
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CascadeDeleteJob', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_cascade_delete_job_details.metadata = {'url': '/farmers/cascade-delete/{jobId}'}  # type: ignore

    async def _create_cascade_delete_job_initial(
        self,
        job_id: str,
        farmer_id: str,
        **kwargs: Any
    ) -> "_models.CascadeDeleteJob":
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CascadeDeleteJob"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self._create_cascade_delete_job_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'jobId': self._serialize.url("job_id", job_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['farmerId'] = self._serialize.query("farmer_id", farmer_id, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('CascadeDeleteJob', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_cascade_delete_job_initial.metadata = {'url': '/farmers/cascade-delete/{jobId}'}  # type: ignore

    async def begin_create_cascade_delete_job(
        self,
        job_id: str,
        farmer_id: str,
        **kwargs: Any
    ) -> AsyncLROPoller["_models.CascadeDeleteJob"]:
        """Create a cascade delete job for specified farmer.

        :param job_id: Job ID supplied by end user.
        :type job_id: str
        :param farmer_id: ID of the farmer to be deleted.
        :type farmer_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling.
         Pass in False for this operation to not poll, or pass in your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CascadeDeleteJob or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.agrifood.farming.models.CascadeDeleteJob]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CascadeDeleteJob"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_cascade_delete_job_initial(
                job_id=job_id,
                farmer_id=farmer_id,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('CascadeDeleteJob', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'jobId': self._serialize.url("job_id", job_id, 'str'),
        }

        if polling is True: polling_method = AsyncLROBasePolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
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
    begin_create_cascade_delete_job.metadata = {'url': '/farmers/cascade-delete/{jobId}'}  # type: ignore
