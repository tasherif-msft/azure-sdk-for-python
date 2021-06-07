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


class AccountType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of storage accessed on the storage account.
    """

    GENERAL_PURPOSE_STORAGE = "GeneralPurposeStorage"
    BLOB_STORAGE = "BlobStorage"

class AddonState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Addon Provisioning State
    """

    INVALID = "Invalid"
    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    RECONFIGURING = "Reconfiguring"
    FAILED = "Failed"
    DELETING = "Deleting"

class AddonType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Addon type.
    """

    IOT_EDGE = "IotEdge"
    ARC_FOR_KUBERNETES = "ArcForKubernetes"

class AlertSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Severity of the alert.
    """

    INFORMATIONAL = "Informational"
    WARNING = "Warning"
    CRITICAL = "Critical"

class AuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authentication type.
    """

    INVALID = "Invalid"
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"

class AzureContainerDataFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Storage format used for the file represented by the share.
    """

    BLOCK_BLOB = "BlockBlob"
    PAGE_BLOB = "PageBlob"
    AZURE_FILE = "AzureFile"

class ClientPermissionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of access to be allowed for the client.
    """

    NO_ACCESS = "NoAccess"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class ContainerStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current status of the container.
    """

    OK = "OK"
    OFFLINE = "Offline"
    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    NEEDS_ATTENTION = "NeedsAttention"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DataBoxEdgeDeviceKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The etag for the devices.
    """

    AZURE_DATA_BOX_GATEWAY = "AzureDataBoxGateway"
    AZURE_STACK_EDGE = "AzureStackEdge"
    AZURE_STACK_HUB = "AzureStackHub"
    AZURE_MODULAR_DATA_CENTRE = "AzureModularDataCentre"

class DataBoxEdgeDeviceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the Data Box Edge/Gateway device.
    """

    READY_TO_SETUP = "ReadyToSetup"
    ONLINE = "Online"
    OFFLINE = "Offline"
    NEEDS_ATTENTION = "NeedsAttention"
    DISCONNECTED = "Disconnected"
    PARTIALLY_DISCONNECTED = "PartiallyDisconnected"
    MAINTENANCE = "Maintenance"

class DataPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Data policy of the share.
    """

    CLOUD = "Cloud"
    LOCAL = "Local"

class DayOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class DeviceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the Data Box Edge/Gateway device.
    """

    DATA_BOX_EDGE_DEVICE = "DataBoxEdgeDevice"

class DownloadPhase(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The download phase.
    """

    UNKNOWN = "Unknown"
    INITIALIZING = "Initializing"
    DOWNLOADING = "Downloading"
    VERIFYING = "Verifying"

class EncryptionAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The algorithm used to encrypt "Value".
    """

    NONE = "None"
    AES256 = "AES256"
    RSAES_PKCS1_V1_5 = "RSAES_PKCS1_v_1_5"

class HostPlatformType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Platform where the runtime is hosted.
    """

    KUBERNETES_CLUSTER = "KubernetesCluster"
    LINUX_VM = "LinuxVM"

class InstallRebootBehavior(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates if updates are available and at least one of the updates needs a reboot.
    """

    NEVER_REBOOTS = "NeverReboots"
    REQUIRES_REBOOT = "RequiresReboot"
    REQUEST_REBOOT = "RequestReboot"

class JobStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the job.
    """

    INVALID = "Invalid"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PAUSED = "Paused"
    SCHEDULED = "Scheduled"

class JobType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the job.
    """

    INVALID = "Invalid"
    SCAN_FOR_UPDATES = "ScanForUpdates"
    DOWNLOAD_UPDATES = "DownloadUpdates"
    INSTALL_UPDATES = "InstallUpdates"
    REFRESH_SHARE = "RefreshShare"
    REFRESH_CONTAINER = "RefreshContainer"
    BACKUP = "Backup"
    RESTORE = "Restore"
    TRIGGER_SUPPORT_PACKAGE = "TriggerSupportPackage"

class KubernetesNodeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Node type - Master/Worker
    """

    INVALID = "Invalid"
    MASTER = "Master"
    WORKER = "Worker"

class KubernetesState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of Kubernetes deployment
    """

    INVALID = "Invalid"
    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    RECONFIGURING = "Reconfiguring"
    FAILED = "Failed"
    DELETING = "Deleting"

class MetricAggregationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Metric aggregation type.
    """

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
    COUNT = "Count"

class MetricCategory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Metric category.
    """

    CAPACITY = "Capacity"
    TRANSACTION = "Transaction"

class MetricUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Metric units.
    """

    NOT_SPECIFIED = "NotSpecified"
    PERCENT = "Percent"
    COUNT = "Count"
    SECONDS = "Seconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    BYTES_PER_SECOND = "BytesPerSecond"
    COUNT_PER_SECOND = "CountPerSecond"

class MonitoringStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current monitoring status of the share.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class MountType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Mounting type.
    """

    VOLUME = "Volume"
    HOST_PATH = "HostPath"

class MsiIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Identity type
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"

class NetworkAdapterDHCPStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Value indicating whether this adapter has DHCP enabled.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class NetworkAdapterRDMAStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Value indicating whether this adapter is RDMA capable.
    """

    INCAPABLE = "Incapable"
    CAPABLE = "Capable"

class NetworkAdapterStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Value indicating whether this adapter is valid.
    """

    INACTIVE = "Inactive"
    ACTIVE = "Active"

class NetworkGroup(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The network group.
    """

    NONE = "None"
    NON_RDMA = "NonRDMA"
    RDMA = "RDMA"

class NodeStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current status of the individual node
    """

    UNKNOWN = "Unknown"
    UP = "Up"
    DOWN = "Down"
    REBOOTING = "Rebooting"
    SHUTTING_DOWN = "ShuttingDown"

class OrderState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the order as per the allowed status types.
    """

    UNTRACKED = "Untracked"
    AWAITING_FULFILMENT = "AwaitingFulfilment"
    AWAITING_PREPARATION = "AwaitingPreparation"
    AWAITING_SHIPMENT = "AwaitingShipment"
    SHIPPED = "Shipped"
    ARRIVING = "Arriving"
    DELIVERED = "Delivered"
    REPLACEMENT_REQUESTED = "ReplacementRequested"
    LOST_DEVICE = "LostDevice"
    DECLINED = "Declined"
    RETURN_INITIATED = "ReturnInitiated"
    AWAITING_RETURN_SHIPMENT = "AwaitingReturnShipment"
    SHIPPED_BACK = "ShippedBack"
    COLLECTED_AT_MICROSOFT = "CollectedAtMicrosoft"
    AWAITING_PICKUP = "AwaitingPickup"
    PICKUP_COMPLETED = "PickupCompleted"
    AWAITING_DROP = "AwaitingDrop"

class PlatformType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Host OS supported by the Arc addon.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class PosixComplianceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If provisioned storage is posix compliant.
    """

    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ResourceMoveStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Denotes whether move operation is in progress
    """

    NONE = "None"
    RESOURCE_MOVE_IN_PROGRESS = "ResourceMoveInProgress"
    RESOURCE_MOVE_FAILED = "ResourceMoveFailed"

class RoleStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Local Edge Management Status
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class RoleTypes(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    IOT = "IOT"
    ASA = "ASA"
    FUNCTIONS = "Functions"
    COGNITIVE = "Cognitive"
    MEC = "MEC"
    CLOUD_EDGE_MANAGEMENT = "CloudEdgeManagement"
    KUBERNETES = "Kubernetes"

class ShareAccessProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Access protocol to be used by the share.
    """

    SMB = "SMB"
    NFS = "NFS"

class ShareAccessType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of access to be allowed on the share for this user.
    """

    CHANGE = "Change"
    READ = "Read"
    CUSTOM = "Custom"

class ShareStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current status of the share.
    """

    OFFLINE = "Offline"
    UNKNOWN = "Unknown"
    OK = "OK"
    UPDATING = "Updating"
    NEEDS_ATTENTION = "NeedsAttention"

class ShipmentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_APPLICABLE = "NotApplicable"
    SHIPPED_TO_CUSTOMER = "ShippedToCustomer"
    SELF_PICKUP = "SelfPickup"

class SkuAvailability(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Links to the next set of results
    """

    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Sku name.
    """

    GATEWAY = "Gateway"
    EDGE = "Edge"
    TEA1_NODE = "TEA_1Node"
    TEA1_NODE_UPS = "TEA_1Node_UPS"
    TEA1_NODE_HEATER = "TEA_1Node_Heater"
    TEA1_NODE_UPS_HEATER = "TEA_1Node_UPS_Heater"
    TEA4_NODE_HEATER = "TEA_4Node_Heater"
    TEA4_NODE_UPS_HEATER = "TEA_4Node_UPS_Heater"
    TMA = "TMA"
    TDC = "TDC"
    TCA_SMALL = "TCA_Small"
    GPU = "GPU"
    TCA_LARGE = "TCA_Large"
    EDGE_P_BASE = "EdgeP_Base"
    EDGE_P_HIGH = "EdgeP_High"
    EDGE_PR_BASE = "EdgePR_Base"
    EDGE_PR_BASE_UPS = "EdgePR_Base_UPS"
    EDGE_MR_MINI = "EdgeMR_Mini"
    RCA_SMALL = "RCA_Small"
    RCA_LARGE = "RCA_Large"
    RDC = "RDC"

class SkuSignupOption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sku can be signed up by customer or not.
    """

    NONE = "None"
    AVAILABLE = "Available"

class SkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Sku tier.
    """

    STANDARD = "Standard"

class SkuVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Availability of the Sku as preview/stable.
    """

    STABLE = "Stable"
    PREVIEW = "Preview"

class SSLStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Signifies whether SSL needs to be enabled or not.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class StorageAccountStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current status of the storage account
    """

    OK = "OK"
    OFFLINE = "Offline"
    UNKNOWN = "Unknown"
    UPDATING = "Updating"
    NEEDS_ATTENTION = "NeedsAttention"

class SubscriptionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    REGISTERED = "Registered"
    WARNED = "Warned"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"
    UNREGISTERED = "Unregistered"

class TimeGrain(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    PT1_M = "PT1M"
    PT5_M = "PT5M"
    PT15_M = "PT15M"
    PT30_M = "PT30M"
    PT1_H = "PT1H"
    PT6_H = "PT6H"
    PT12_H = "PT12H"
    PT1_D = "PT1D"

class TriggerEventType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Trigger Kind.
    """

    FILE_EVENT = "FileEvent"
    PERIODIC_TIMER_EVENT = "PeriodicTimerEvent"

class UpdateOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current update operation.
    """

    NONE = "None"
    SCAN = "Scan"
    DOWNLOAD = "Download"
    INSTALL = "Install"

class UpdateOperationStage(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Current stage of the update operation.
    """

    UNKNOWN = "Unknown"
    INITIAL = "Initial"
    SCAN_STARTED = "ScanStarted"
    SCAN_COMPLETE = "ScanComplete"
    SCAN_FAILED = "ScanFailed"
    DOWNLOAD_STARTED = "DownloadStarted"
    DOWNLOAD_COMPLETE = "DownloadComplete"
    DOWNLOAD_FAILED = "DownloadFailed"
    INSTALL_STARTED = "InstallStarted"
    INSTALL_COMPLETE = "InstallComplete"
    INSTALL_FAILED = "InstallFailed"
    REBOOT_INITIATED = "RebootInitiated"
    SUCCESS = "Success"
    FAILURE = "Failure"
    RESCAN_STARTED = "RescanStarted"
    RESCAN_COMPLETE = "RescanComplete"
    RESCAN_FAILED = "RescanFailed"

class UserType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the user.
    """

    SHARE = "Share"
    LOCAL_MANAGEMENT = "LocalManagement"
    ARM = "ARM"
