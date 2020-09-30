# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class DeploymentMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode that is used to deploy resources. This value can be either Incremental or Complete. In
    Incremental mode, resources are deployed without deleting existing resources that are not
    included in the template. In Complete mode, resources are deployed and existing resources in
    the resource group that are not included in the template are deleted. Be careful when using
    Complete mode as you may unintentionally delete resources.
    """

    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"

class OnErrorDeploymentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The deployment on error behavior type. Possible values are LastSuccessful and
    SpecificDeployment.
    """

    LAST_SUCCESSFUL = "LastSuccessful"
    SPECIFIC_DEPLOYMENT = "SpecificDeployment"

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The identity type.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"
