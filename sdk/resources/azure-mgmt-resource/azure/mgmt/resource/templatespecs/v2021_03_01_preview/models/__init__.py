# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureResourceBase
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import LinkedTemplateArtifact
    from ._models_py3 import SystemData
    from ._models_py3 import TemplateSpec
    from ._models_py3 import TemplateSpecUpdateModel
    from ._models_py3 import TemplateSpecVersion
    from ._models_py3 import TemplateSpecVersionInfo
    from ._models_py3 import TemplateSpecVersionUpdateModel
    from ._models_py3 import TemplateSpecVersionsListResult
    from ._models_py3 import TemplateSpecsError
    from ._models_py3 import TemplateSpecsListResult
except (SyntaxError, ImportError):
    from ._models import AzureResourceBase  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import LinkedTemplateArtifact  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TemplateSpec  # type: ignore
    from ._models import TemplateSpecUpdateModel  # type: ignore
    from ._models import TemplateSpecVersion  # type: ignore
    from ._models import TemplateSpecVersionInfo  # type: ignore
    from ._models import TemplateSpecVersionUpdateModel  # type: ignore
    from ._models import TemplateSpecVersionsListResult  # type: ignore
    from ._models import TemplateSpecsError  # type: ignore
    from ._models import TemplateSpecsListResult  # type: ignore

from ._template_specs_client_enums import (
    CreatedByType,
    TemplateSpecExpandKind,
)

__all__ = [
    'AzureResourceBase',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'LinkedTemplateArtifact',
    'SystemData',
    'TemplateSpec',
    'TemplateSpecUpdateModel',
    'TemplateSpecVersion',
    'TemplateSpecVersionInfo',
    'TemplateSpecVersionUpdateModel',
    'TemplateSpecVersionsListResult',
    'TemplateSpecsError',
    'TemplateSpecsListResult',
    'CreatedByType',
    'TemplateSpecExpandKind',
]
