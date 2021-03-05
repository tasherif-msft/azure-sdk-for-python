# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ServiceOperations(object):
    """ServiceOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.storage.fileshare.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def set_properties(
        self,
        storage_service_properties,  # type: "_models.StorageServiceProperties"
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Sets properties for a storage account's File service endpoint, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties.
        :type storage_service_properties: ~azure.storage.fileshare.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-
         File-Service-Operations?redirectedfrom=MSDN">Setting Timeouts for File Service
         Operations.</a>`.
        :type timeout: int
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
        restype = "service"
        comp = "properties"
        content_type = kwargs.pop("content_type", "application/xml")
        accept = "application/xml"

        # Construct URL
        url = self.set_properties.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(storage_service_properties, 'StorageServiceProperties', is_xml=True)
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    set_properties.metadata = {'url': '/'}  # type: ignore

    def get_properties(
        self,
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.StorageServiceProperties"
        """Gets the properties of a storage account's File service, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-
         File-Service-Operations?redirectedfrom=MSDN">Setting Timeouts for File Service
         Operations.</a>`.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties, or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.StorageServiceProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StorageServiceProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        restype = "service"
        comp = "properties"
        accept = "application/xml"

        # Construct URL
        url = self.get_properties.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['restype'] = self._serialize.query("restype", restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        deserialized = self._deserialize('StorageServiceProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_properties.metadata = {'url': '/'}  # type: ignore

    def list_shares_segment(
        self,
        prefix=None,  # type: Optional[str]
        marker=None,  # type: Optional[str]
        maxresults=None,  # type: Optional[int]
        include=None,  # type: Optional[List[Union[str, "_models.ListSharesIncludeType"]]]
        timeout=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ListSharesResponse"
        """The List Shares Segment operation returns a list of the shares and share snapshots under the
        specified account.

        :param prefix: Filters the results to return only entries whose name begins with the specified
         prefix.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list to be returned with the
         next list operation. The operation returns a marker value within the response body if the list
         returned was not complete. The marker value may then be used in a subsequent call to request
         the next set of list items. The marker value is opaque to the client.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return. If the request does not
         specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000
         items.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response.
        :type include: list[str or ~azure.storage.fileshare.models.ListSharesIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-
         File-Service-Operations?redirectedfrom=MSDN">Setting Timeouts for File Service
         Operations.</a>`.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSharesResponse, or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListSharesResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ListSharesResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        comp = "list"
        accept = "application/xml"

        # Construct URL
        url = self.list_shares_segment.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')
        if prefix is not None:
            query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
        if marker is not None:
            query_parameters['marker'] = self._serialize.query("marker", marker, 'str')
        if maxresults is not None:
            query_parameters['maxresults'] = self._serialize.query("maxresults", maxresults, 'int', minimum=1)
        if include is not None:
            query_parameters['include'] = self._serialize.query("include", include, '[str]', div=',')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.StorageError, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        response_headers['x-ms-version']=self._deserialize('str', response.headers.get('x-ms-version'))
        deserialized = self._deserialize('ListSharesResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    list_shares_segment.metadata = {'url': '/'}  # type: ignore
