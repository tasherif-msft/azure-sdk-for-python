# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates Insights service is not able to process the incoming request. The reason is provided in the error message.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class LiveTokenResponse(msrest.serialization.Model):
    """The response to a live token query.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar live_token: JWT token for accessing live metrics stream data.
    :vartype live_token: str
    """

    _validation = {
        'live_token': {'readonly': True},
    }

    _attribute_map = {
        'live_token': {'key': 'liveToken', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LiveTokenResponse, self).__init__(**kwargs)
        self.live_token = None


class OperationInfo(msrest.serialization.Model):
    """Information about an operation.

    :param provider: Name of the provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the operation.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationInfo, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationLive(msrest.serialization.Model):
    """Represents an operation returned by the GetOperations request.

    :param name: Name of the operation.
    :type name: str
    :param display: Display name of the operation.
    :type display: ~azure.mgmt.applicationinsights.v2020_06_02_preview.models.OperationInfo
    :param origin: Origin of the operation.
    :type origin: str
    :param properties: Properties of the operation.
    :type properties: object
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationLive, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)


class OperationsListResult(msrest.serialization.Model):
    """Result of the List Operations operation.

    :param value: A collection of operations.
    :type value: list[~azure.mgmt.applicationinsights.v2020_06_02_preview.models.OperationLive]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationLive]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
