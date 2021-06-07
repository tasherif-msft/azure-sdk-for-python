# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessPolicyEntry
    from ._models_py3 import Attributes
    from ._models_py3 import CheckNameAvailabilityResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import DeletedVault
    from ._models_py3 import DeletedVaultListResult
    from ._models_py3 import DeletedVaultProperties
    from ._models_py3 import DimensionProperties
    from ._models_py3 import Error
    from ._models_py3 import IPRule
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagedHsm
    from ._models_py3 import ManagedHsmError
    from ._models_py3 import ManagedHsmListResult
    from ._models_py3 import ManagedHsmProperties
    from ._models_py3 import ManagedHsmResource
    from ._models_py3 import ManagedHsmSku
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NetworkRuleSet
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import Permissions
    from ._models_py3 import PrivateEndpoint
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionItem
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionState
    from ._models_py3 import Resource
    from ._models_py3 import ResourceListResult
    from ._models_py3 import Secret
    from ._models_py3 import SecretAttributes
    from ._models_py3 import SecretCreateOrUpdateParameters
    from ._models_py3 import SecretListResult
    from ._models_py3 import SecretPatchParameters
    from ._models_py3 import SecretPatchProperties
    from ._models_py3 import SecretProperties
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Sku
    from ._models_py3 import SystemData
    from ._models_py3 import Vault
    from ._models_py3 import VaultAccessPolicyParameters
    from ._models_py3 import VaultAccessPolicyProperties
    from ._models_py3 import VaultCheckNameAvailabilityParameters
    from ._models_py3 import VaultCreateOrUpdateParameters
    from ._models_py3 import VaultListResult
    from ._models_py3 import VaultPatchParameters
    from ._models_py3 import VaultPatchProperties
    from ._models_py3 import VaultProperties
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import AccessPolicyEntry  # type: ignore
    from ._models import Attributes  # type: ignore
    from ._models import CheckNameAvailabilityResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import DeletedVault  # type: ignore
    from ._models import DeletedVaultListResult  # type: ignore
    from ._models import DeletedVaultProperties  # type: ignore
    from ._models import DimensionProperties  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import IPRule  # type: ignore
    from ._models import LogSpecification  # type: ignore
    from ._models import ManagedHsm  # type: ignore
    from ._models import ManagedHsmError  # type: ignore
    from ._models import ManagedHsmListResult  # type: ignore
    from ._models import ManagedHsmProperties  # type: ignore
    from ._models import ManagedHsmResource  # type: ignore
    from ._models import ManagedHsmSku  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import NetworkRuleSet  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import Permissions  # type: ignore
    from ._models import PrivateEndpoint  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionItem  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionState  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceListResult  # type: ignore
    from ._models import Secret  # type: ignore
    from ._models import SecretAttributes  # type: ignore
    from ._models import SecretCreateOrUpdateParameters  # type: ignore
    from ._models import SecretListResult  # type: ignore
    from ._models import SecretPatchParameters  # type: ignore
    from ._models import SecretPatchProperties  # type: ignore
    from ._models import SecretProperties  # type: ignore
    from ._models import ServiceSpecification  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Vault  # type: ignore
    from ._models import VaultAccessPolicyParameters  # type: ignore
    from ._models import VaultAccessPolicyProperties  # type: ignore
    from ._models import VaultCheckNameAvailabilityParameters  # type: ignore
    from ._models import VaultCreateOrUpdateParameters  # type: ignore
    from ._models import VaultListResult  # type: ignore
    from ._models import VaultPatchParameters  # type: ignore
    from ._models import VaultPatchProperties  # type: ignore
    from ._models import VaultProperties  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore

from ._key_vault_management_client_enums import (
    AccessPolicyUpdateKind,
    ActionsRequired,
    CertificatePermissions,
    CreateMode,
    IdentityType,
    KeyPermissions,
    ManagedHsmSkuFamily,
    ManagedHsmSkuName,
    NetworkRuleAction,
    NetworkRuleBypassOptions,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    Reason,
    SecretPermissions,
    SkuFamily,
    SkuName,
    StoragePermissions,
    VaultProvisioningState,
)

__all__ = [
    'AccessPolicyEntry',
    'Attributes',
    'CheckNameAvailabilityResult',
    'CloudErrorBody',
    'DeletedVault',
    'DeletedVaultListResult',
    'DeletedVaultProperties',
    'DimensionProperties',
    'Error',
    'IPRule',
    'LogSpecification',
    'ManagedHsm',
    'ManagedHsmError',
    'ManagedHsmListResult',
    'ManagedHsmProperties',
    'ManagedHsmResource',
    'ManagedHsmSku',
    'MetricSpecification',
    'NetworkRuleSet',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Permissions',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionItem',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'Resource',
    'ResourceListResult',
    'Secret',
    'SecretAttributes',
    'SecretCreateOrUpdateParameters',
    'SecretListResult',
    'SecretPatchParameters',
    'SecretPatchProperties',
    'SecretProperties',
    'ServiceSpecification',
    'Sku',
    'SystemData',
    'Vault',
    'VaultAccessPolicyParameters',
    'VaultAccessPolicyProperties',
    'VaultCheckNameAvailabilityParameters',
    'VaultCreateOrUpdateParameters',
    'VaultListResult',
    'VaultPatchParameters',
    'VaultPatchProperties',
    'VaultProperties',
    'VirtualNetworkRule',
    'AccessPolicyUpdateKind',
    'ActionsRequired',
    'CertificatePermissions',
    'CreateMode',
    'IdentityType',
    'KeyPermissions',
    'ManagedHsmSkuFamily',
    'ManagedHsmSkuName',
    'NetworkRuleAction',
    'NetworkRuleBypassOptions',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'Reason',
    'SecretPermissions',
    'SkuFamily',
    'SkuName',
    'StoragePermissions',
    'VaultProvisioningState',
]
