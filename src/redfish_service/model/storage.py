from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .pcie_device import PcieInterface
from .protocol import Protocol
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock
from .swordfish.volume import RaidType


class Actions(RedfishModel):
    import_foreign_drives: ImportForeignDrives | None = Field(
        serialization_alias="#Storage.ImportForeignDrives", default=None
    )
    rekey_external_key: RekeyExternalKey | None = Field(
        serialization_alias="#Storage.RekeyExternalKey", default=None
    )
    reset_to_defaults: ResetToDefaults | None = Field(
        serialization_alias="#Storage.ResetToDefaults", default=None
    )
    set_controller_password: SetControllerPassword | None = Field(
        serialization_alias="#Storage.SetControllerPassword", default=None
    )
    set_encryption_key: SetEncryptionKey | None = Field(
        serialization_alias="#Storage.SetEncryptionKey", default=None
    )
    oem: dict[str, Any] | None = None


class AutoVolumeCreate(StrEnum):
    DISABLED = "Disabled"
    NON_RAID = "NonRAID"
    RAID0 = "RAID0"
    RAID1 = "RAID1"


class CacheSummary(RedfishModel):
    persistent_cache_size_mib: int | None = Field(
        serialization_alias="PersistentCacheSizeMiB", default=None
    )
    status: Status | None = None
    total_cache_size_mib: int | None = Field(serialization_alias="TotalCacheSizeMiB", default=None)


class ConfigLockOptions(StrEnum):
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    LOCKDOWN_UNSUPPORTED = "LockdownUnsupported"
    COMMAND_UNSUPPORTED = "CommandUnsupported"


class ConfigurationLock(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    PARTIAL = "Partial"


class EncryptionMode(StrEnum):
    DISABLED = "Disabled"
    USE_EXTERNAL_KEY = "UseExternalKey"
    USE_LOCAL_KEY = "UseLocalKey"
    PASSWORD_ONLY = "PasswordOnly"  # noqa: S105
    PASSWORD_WITH_EXTERNAL_KEY = "PasswordWithExternalKey"  # noqa: S105
    PASSWORD_WITH_LOCAL_KEY = "PasswordWithLocalKey"  # noqa: S105


class HotspareActivationPolicy(StrEnum):
    ON_DRIVE_FAILURE = "OnDriveFailure"
    ON_DRIVE_PREDICTED_FAILURE = "OnDrivePredictedFailure"
    OEM = "OEM"


class ImportForeignDrives(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ImportForeignDrivesRequest(RedfishModel):
    controller_password: str | None = None
    drive_encryption_key: str
    drive_encryption_key_identifier: str | None = None


class Links(RedfishModel):
    block_security_id_unsupported_drives: list[IdRef] | None = Field(
        serialization_alias="BlockSecurityIDUnsupportedDrives", default=None
    )
    block_security_id_unsupported_drives_odata_count: int | None = Field(
        serialization_alias="BlockSecurityIDUnsupportedDrives@odata.count", default=None
    )
    block_security_id_update_unsuccessful_drives: list[IdRef] | None = Field(
        serialization_alias="BlockSecurityIDUpdateUnsuccessfulDrives", default=None
    )
    block_security_id_update_unsuccessful_drives_odata_count: int | None = Field(
        serialization_alias="BlockSecurityIDUpdateUnsuccessfulDrives@odata.count", default=None
    )
    enclosures: list[IdRef] | None = None
    enclosures_odata_count: int | None = Field(
        serialization_alias="Enclosures@odata.count", default=None
    )
    hosting_storage_systems: list[IdRef] | None = None
    hosting_storage_systems_odata_count: int | None = Field(
        serialization_alias="HostingStorageSystems@odata.count", default=None
    )
    nvme_of_discovery_subsystems: list[IdRef] | None = Field(
        serialization_alias="NVMeoFDiscoverySubsystems", default=None
    )
    nvme_of_discovery_subsystems_odata_count: int | None = Field(
        serialization_alias="NVMeoFDiscoverySubsystems@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    simple_storage: IdRef | None = None
    storage_services: list[IdRef] | None = None
    storage_services_odata_count: int | None = Field(
        serialization_alias="StorageServices@odata.count", default=None
    )


class NvmeConfigurationLockState(RedfishModel):
    firmware_commit: ConfigLockOptions | None = None
    firmware_image_download: ConfigLockOptions | None = None
    lockdown: ConfigLockOptions | None = None
    security_send: ConfigLockOptions | None = None
    vpd_write: ConfigLockOptions | None = Field(serialization_alias="VPDWrite", default=None)


class NvmeSubsystemProperties(RedfishModel):
    configuration_lock_state: NvmeConfigurationLockState | None = None
    max_namespaces_supported: float | None = None
    shared_namespace_controller_attachment_supported: bool | None = None


class Rates(RedfishModel):
    consistency_check_rate_percent: int | None = None
    rebuild_rate_percent: int | None = None
    transformation_rate_percent: int | None = None


class RekeyExternalKey(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetToDefaults(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetToDefaultsRequest(RedfishModel):
    reset_type: ResetToDefaultsType


class ResetToDefaultsType(StrEnum):
    RESET_ALL = "ResetAll"
    PRESERVE_VOLUMES = "PreserveVolumes"


class SetControllerPassword(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetControllerPasswordRequest(RedfishModel):
    current_password: str | None = None
    new_password: str
    security_key: str | None = None


class SetEncryptionKey(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetEncryptionKeyRequest(RedfishModel):
    current_encryption_key: str | None = None
    encryption_key: str
    encryption_key_identifier: str | None = None


class Storage(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Storage.v1_19_0.Storage")
    actions: Actions | None = None
    auto_volume_create: AutoVolumeCreate | None = None
    block_security_id_policy: bool | None = Field(
        serialization_alias="BlockSecurityIDPolicy", default=None
    )
    configuration_lock: ConfigurationLock | None = None
    connections: IdRef | None = None
    consistency_groups: IdRef | None = None
    controllers: IdRef | None = None
    description: str | None = None
    drives: list[IdRef] | None = None
    drives_odata_count: int | None = Field(serialization_alias="Drives@odata.count", default=None)
    encryption_mode: EncryptionMode | None = None
    endpoint_groups: IdRef | None = None
    file_systems: IdRef | None = None
    hotspare_activation_policy: HotspareActivationPolicy | None = None
    id: str
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    local_encryption_key_identifier: str | None = None
    metrics: IdRef | None = None
    nvme_subsystem_properties: NvmeSubsystemProperties | None = Field(
        serialization_alias="NVMeSubsystemProperties", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    redundancy_odata_count: int | None = Field(
        serialization_alias="Redundancy@odata.count", default=None
    )
    status: Status | None = None
    storage_controllers: list[StorageController] | None = None
    storage_controllers_odata_count: int | None = Field(
        serialization_alias="StorageControllers@odata.count", default=None
    )
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    target_configuration_lock_level: TargetConfigurationLockLevel | None = None
    volumes: IdRef | None = None


class StorageOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    auto_volume_create: AutoVolumeCreate | None = None
    block_security_id_policy: bool | None = Field(
        serialization_alias="BlockSecurityIDPolicy", default=None
    )
    configuration_lock: ConfigurationLock | None = None
    encryption_mode: EncryptionMode | None = None
    hotspare_activation_policy: HotspareActivationPolicy | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    nvme_subsystem_properties: NvmeSubsystemProperties | None = Field(
        serialization_alias="NVMeSubsystemProperties", default=None
    )
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    status: Status | None = None
    target_configuration_lock_level: TargetConfigurationLockLevel | None = None


class StorageController(RedfishModel):
    odata_id: str = Field(serialization_alias="@odata.id")
    actions: StorageControllerActions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cache_summary: CacheSummary | None = None
    certificates: IdRef | None = None
    controller_rates: Rates | None = None
    firmware_version: str | None = None
    identifiers: list[Identifier] | None = None
    links: StorageControllerLinks | None = None
    location: Location | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    member_id: str
    model: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)
    part_number: str | None = None
    ports: IdRef | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    speed_gbps: float | None = None
    status: Status | None = None
    supported_controller_protocols: list[Protocol] | None = None
    supported_device_protocols: list[Protocol] | None = None
    supported_raid_types: list[RaidType] | None = Field(
        serialization_alias="SupportedRAIDTypes", default=None
    )


class StorageControllerActions(RedfishModel):
    oem: dict[str, Any] | None = None


class StorageControllerLinks(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(
        serialization_alias="PCIeFunctions@odata.count", default=None
    )
    storage_services: list[IdRef] | None = None
    storage_services_odata_count: int | None = Field(
        serialization_alias="StorageServices@odata.count", default=None
    )


class TargetConfigurationLockLevel(StrEnum):
    BASELINE = "Baseline"
