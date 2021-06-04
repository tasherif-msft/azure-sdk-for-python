# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AgentPool
    from ._models_py3 import AgentPoolListResult
    from ._models_py3 import AgentPoolQueueStatus
    from ._models_py3 import AgentPoolUpdateParameters
    from ._models_py3 import AgentProperties
    from ._models_py3 import Argument
    from ._models_py3 import AuthInfo
    from ._models_py3 import AuthInfoUpdateParameters
    from ._models_py3 import BaseImageDependency
    from ._models_py3 import BaseImageTrigger
    from ._models_py3 import BaseImageTriggerUpdateParameters
    from ._models_py3 import Credentials
    from ._models_py3 import CustomRegistryCredentials
    from ._models_py3 import DockerBuildRequest
    from ._models_py3 import DockerBuildStep
    from ._models_py3 import DockerBuildStepUpdateParameters
    from ._models_py3 import EncodedTaskRunRequest
    from ._models_py3 import EncodedTaskStep
    from ._models_py3 import EncodedTaskStepUpdateParameters
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ErrorResponseBody
    from ._models_py3 import FileTaskRunRequest
    from ._models_py3 import FileTaskStep
    from ._models_py3 import FileTaskStepUpdateParameters
    from ._models_py3 import IdentityProperties
    from ._models_py3 import ImageDescriptor
    from ._models_py3 import ImageUpdateTrigger
    from ._models_py3 import InnerErrorDescription
    from ._models_py3 import OverrideTaskStepProperties
    from ._models_py3 import PlatformProperties
    from ._models_py3 import PlatformUpdateParameters
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import Run
    from ._models_py3 import RunFilter
    from ._models_py3 import RunGetLogResult
    from ._models_py3 import RunListResult
    from ._models_py3 import RunRequest
    from ._models_py3 import RunUpdateParameters
    from ._models_py3 import SecretObject
    from ._models_py3 import SetValue
    from ._models_py3 import SourceProperties
    from ._models_py3 import SourceRegistryCredentials
    from ._models_py3 import SourceTrigger
    from ._models_py3 import SourceTriggerDescriptor
    from ._models_py3 import SourceTriggerUpdateParameters
    from ._models_py3 import SourceUpdateParameters
    from ._models_py3 import SourceUploadDefinition
    from ._models_py3 import SystemData
    from ._models_py3 import Task
    from ._models_py3 import TaskListResult
    from ._models_py3 import TaskRun
    from ._models_py3 import TaskRunListResult
    from ._models_py3 import TaskRunRequest
    from ._models_py3 import TaskRunUpdateParameters
    from ._models_py3 import TaskStepProperties
    from ._models_py3 import TaskStepUpdateParameters
    from ._models_py3 import TaskUpdateParameters
    from ._models_py3 import TimerTrigger
    from ._models_py3 import TimerTriggerDescriptor
    from ._models_py3 import TimerTriggerUpdateParameters
    from ._models_py3 import TriggerProperties
    from ._models_py3 import TriggerUpdateParameters
    from ._models_py3 import UserIdentityProperties
except (SyntaxError, ImportError):
    from ._models import AgentPool  # type: ignore
    from ._models import AgentPoolListResult  # type: ignore
    from ._models import AgentPoolQueueStatus  # type: ignore
    from ._models import AgentPoolUpdateParameters  # type: ignore
    from ._models import AgentProperties  # type: ignore
    from ._models import Argument  # type: ignore
    from ._models import AuthInfo  # type: ignore
    from ._models import AuthInfoUpdateParameters  # type: ignore
    from ._models import BaseImageDependency  # type: ignore
    from ._models import BaseImageTrigger  # type: ignore
    from ._models import BaseImageTriggerUpdateParameters  # type: ignore
    from ._models import Credentials  # type: ignore
    from ._models import CustomRegistryCredentials  # type: ignore
    from ._models import DockerBuildRequest  # type: ignore
    from ._models import DockerBuildStep  # type: ignore
    from ._models import DockerBuildStepUpdateParameters  # type: ignore
    from ._models import EncodedTaskRunRequest  # type: ignore
    from ._models import EncodedTaskStep  # type: ignore
    from ._models import EncodedTaskStepUpdateParameters  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ErrorResponseBody  # type: ignore
    from ._models import FileTaskRunRequest  # type: ignore
    from ._models import FileTaskStep  # type: ignore
    from ._models import FileTaskStepUpdateParameters  # type: ignore
    from ._models import IdentityProperties  # type: ignore
    from ._models import ImageDescriptor  # type: ignore
    from ._models import ImageUpdateTrigger  # type: ignore
    from ._models import InnerErrorDescription  # type: ignore
    from ._models import OverrideTaskStepProperties  # type: ignore
    from ._models import PlatformProperties  # type: ignore
    from ._models import PlatformUpdateParameters  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Run  # type: ignore
    from ._models import RunFilter  # type: ignore
    from ._models import RunGetLogResult  # type: ignore
    from ._models import RunListResult  # type: ignore
    from ._models import RunRequest  # type: ignore
    from ._models import RunUpdateParameters  # type: ignore
    from ._models import SecretObject  # type: ignore
    from ._models import SetValue  # type: ignore
    from ._models import SourceProperties  # type: ignore
    from ._models import SourceRegistryCredentials  # type: ignore
    from ._models import SourceTrigger  # type: ignore
    from ._models import SourceTriggerDescriptor  # type: ignore
    from ._models import SourceTriggerUpdateParameters  # type: ignore
    from ._models import SourceUpdateParameters  # type: ignore
    from ._models import SourceUploadDefinition  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Task  # type: ignore
    from ._models import TaskListResult  # type: ignore
    from ._models import TaskRun  # type: ignore
    from ._models import TaskRunListResult  # type: ignore
    from ._models import TaskRunRequest  # type: ignore
    from ._models import TaskRunUpdateParameters  # type: ignore
    from ._models import TaskStepProperties  # type: ignore
    from ._models import TaskStepUpdateParameters  # type: ignore
    from ._models import TaskUpdateParameters  # type: ignore
    from ._models import TimerTrigger  # type: ignore
    from ._models import TimerTriggerDescriptor  # type: ignore
    from ._models import TimerTriggerUpdateParameters  # type: ignore
    from ._models import TriggerProperties  # type: ignore
    from ._models import TriggerUpdateParameters  # type: ignore
    from ._models import UserIdentityProperties  # type: ignore

from ._container_registry_management_client_enums import (
    Architecture,
    BaseImageDependencyType,
    BaseImageTriggerType,
    CreatedByType,
    LastModifiedByType,
    OS,
    ProvisioningState,
    ResourceIdentityType,
    RunStatus,
    RunType,
    SecretObjectType,
    SourceControlType,
    SourceRegistryLoginMode,
    SourceTriggerEvent,
    StepType,
    TaskStatus,
    TokenType,
    TriggerStatus,
    UpdateTriggerPayloadType,
    Variant,
)

__all__ = [
    'AgentPool',
    'AgentPoolListResult',
    'AgentPoolQueueStatus',
    'AgentPoolUpdateParameters',
    'AgentProperties',
    'Argument',
    'AuthInfo',
    'AuthInfoUpdateParameters',
    'BaseImageDependency',
    'BaseImageTrigger',
    'BaseImageTriggerUpdateParameters',
    'Credentials',
    'CustomRegistryCredentials',
    'DockerBuildRequest',
    'DockerBuildStep',
    'DockerBuildStepUpdateParameters',
    'EncodedTaskRunRequest',
    'EncodedTaskStep',
    'EncodedTaskStepUpdateParameters',
    'ErrorResponse',
    'ErrorResponseBody',
    'FileTaskRunRequest',
    'FileTaskStep',
    'FileTaskStepUpdateParameters',
    'IdentityProperties',
    'ImageDescriptor',
    'ImageUpdateTrigger',
    'InnerErrorDescription',
    'OverrideTaskStepProperties',
    'PlatformProperties',
    'PlatformUpdateParameters',
    'ProxyResource',
    'Resource',
    'Run',
    'RunFilter',
    'RunGetLogResult',
    'RunListResult',
    'RunRequest',
    'RunUpdateParameters',
    'SecretObject',
    'SetValue',
    'SourceProperties',
    'SourceRegistryCredentials',
    'SourceTrigger',
    'SourceTriggerDescriptor',
    'SourceTriggerUpdateParameters',
    'SourceUpdateParameters',
    'SourceUploadDefinition',
    'SystemData',
    'Task',
    'TaskListResult',
    'TaskRun',
    'TaskRunListResult',
    'TaskRunRequest',
    'TaskRunUpdateParameters',
    'TaskStepProperties',
    'TaskStepUpdateParameters',
    'TaskUpdateParameters',
    'TimerTrigger',
    'TimerTriggerDescriptor',
    'TimerTriggerUpdateParameters',
    'TriggerProperties',
    'TriggerUpdateParameters',
    'UserIdentityProperties',
    'Architecture',
    'BaseImageDependencyType',
    'BaseImageTriggerType',
    'CreatedByType',
    'LastModifiedByType',
    'OS',
    'ProvisioningState',
    'ResourceIdentityType',
    'RunStatus',
    'RunType',
    'SecretObjectType',
    'SourceControlType',
    'SourceRegistryLoginMode',
    'SourceTriggerEvent',
    'StepType',
    'TaskStatus',
    'TokenType',
    'TriggerStatus',
    'UpdateTriggerPayloadType',
    'Variant',
]
