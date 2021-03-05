# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
import six
from azure.core.pipeline import PipelineRequest
from azure.core.pipeline.policies import SansIOHTTPPolicy
from .._base_handler import ServiceBusSharedKeyCredential


class ServiceBusSharedKeyCredentialPolicy(SansIOHTTPPolicy):
    """A policy that put token generated by ServiceBusSharedKeyCredential into HTTP request header

    :param str endpoint:
    :param ServiceBusSharedKeyCredential credential:
    :param str name:
    """

    def __init__(self, endpoint, credential, name):
        # type: (str, ServiceBusSharedKeyCredential, str) -> None
        super(ServiceBusSharedKeyCredentialPolicy, self).__init__()
        self._credential = credential
        self._endpoint = endpoint
        if not name:
            raise ValueError("name can not be None or empty")
        if not isinstance(name, six.string_types):
            raise TypeError("name must be a string.")
        self._name = name
        self._token_expiry_on = 0
        self._token = None

    def _update_token(self):
        if (
            self._token_expiry_on + 60 <= time.time()
        ):  # Update token if it's expiring in 60 seconds
            access_token, self._token_expiry_on = self._credential.get_token(
                self._endpoint
            )
            self._token = access_token.decode("utf-8")

    def on_request(self, request):
        # type: (PipelineRequest) -> None
        """Adds an Authorization header to request and sends request to next policy.

        :param request: The pipeline request object
        :type request: ~azure.core.pipeline.PipelineRequest
        """
        self._update_token()
        request.http_request.headers[self._name] = self._token
