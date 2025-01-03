from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Identifier, IndicatorLed, Location, Status
from .software_inventory import MeasurementBlock
from .swordfish.volume import OperationType


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Drive.Reset", default=None)
    revert_to_original_factory_state: RevertToOriginalFactoryState | None = Field(
        alias="#Drive.RevertToOriginalFactoryState", default=None
    )
    secure_erase: SecureErase | None = Field(alias="#Drive.SecureErase", default=None)
    oem: dict[str, Any] | None = None


class ConfigLockOptions(StrEnum):
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    LOCKDOWN_UNSUPPORTED = "LockdownUnsupported"
    COMMAND_UNSUPPORTED = "CommandUnsupported"


class ConfigurationLock(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    PARTIAL = "Partial"


class Drive(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    block_security_id_enabled: bool | None = Field(alias="BlockSecurityIDEnabled", default=None)
    block_size_bytes: int | None = None
    capable_speed_gbs: float | None = None
    capacity_bytes: int | None = None
    certificates: IdRef | None = None
    configuration_lock: ConfigurationLock | None = None
    description: str | None = None
    drive_form_factor: FormFactor | None = None
    encryption_ability: EncryptionAbility | None = None
    encryption_status: EncryptionStatus | None = None
    environment_metrics: IdRef | None = None
    failure_predicted: bool | None = None
    firmware_version: str | None = None
    hotspare_replacement_mode: HotspareReplacementModeType | None = None
    hotspare_type: HotspareType | None = None
    id: str
    identifiers: list[Identifier] | None = None
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    links: Links | None = None
    location: list[Location] | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    media_type: MediaType | None = None
    metrics: IdRef | None = None
    model: str | None = None
    multipath: bool | None = None
    nvme: Nvme | None = Field(alias="NVMe", default=None)
    name: str
    negotiated_speed_gbs: float | None = None
    oem: dict[str, Any] | None = None
    operations: list[Operations] | None = None
    part_number: str | None = None
    physical_location: Location | None = None
    predicted_media_life_left_percent: float | None = None
    protocol: Protocol | None = None
    ready_to_remove: bool | None = None
    revision: str | None = None
    rotation_speed_rpm: float | None = Field(alias="RotationSpeedRPM", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    slot_capable_protocols: list[Protocol] | None = None
    slot_form_factor: FormFactor | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    status_indicator: StatusIndicator | None = None
    target_configuration_lock_level: TargetConfigurationLockLevel | None = None
    write_cache_enabled: bool | None = None


class EncryptionAbility(StrEnum):
    NONE = "None"
    SELF_ENCRYPTING_DRIVE = "SelfEncryptingDrive"
    OTHER = "Other"


class EncryptionStatus(StrEnum):
    UNECRYPTED = "Unecrypted"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    FOREIGN = "Foreign"
    UNENCRYPTED = "Unencrypted"


class FormFactor(StrEnum):
    DRIVE3_5 = "Drive3_5"
    DRIVE2_5 = "Drive2_5"
    EDSFF = "EDSFF"
    EDSF_F_1_U_LONG = "EDSFF_1U_Long"
    EDSF_F_1_U_SHORT = "EDSFF_1U_Short"
    EDSF_F_E3_SHORT = "EDSFF_E3_Short"
    EDSF_F_E3_LONG = "EDSFF_E3_Long"
    M2 = "M2"
    M2_2230 = "M2_2230"
    M2_2242 = "M2_2242"
    M2_2260 = "M2_2260"
    M2_2280 = "M2_2280"
    M2_22110 = "M2_22110"
    U2 = "U2"
    PCIE_SLOT_FULL_LENGTH = "PCIeSlotFullLength"
    PCIE_SLOT_LOW_PROFILE = "PCIeSlotLowProfile"
    PCIE_HALF_LENGTH = "PCIeHalfLength"
    OEM = "OEM"


class HotspareReplacementModeType(StrEnum):
    REVERTIBLE = "Revertible"
    NON_REVERTIBLE = "NonRevertible"


class HotspareType(StrEnum):
    NONE = "None"
    GLOBAL = "Global"
    CHASSIS = "Chassis"
    DEDICATED = "Dedicated"


class Links(RedfishModel):
    active_software_image: IdRef | None = None
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        alias="SoftwareImages@odata.count", default=None
    )
    storage: IdRef | None = None
    storage_pools: list[IdRef] | None = None
    storage_pools_odata_count: int | None = Field(alias="StoragePools@odata.count", default=None)
    volumes: list[IdRef] | None = None
    volumes_odata_count: int | None = Field(alias="Volumes@odata.count", default=None)


class MediaType(StrEnum):
    HDD = "HDD"
    SSD = "SSD"
    SMR = "SMR"


class Nvme(RedfishModel):
    configuration_lock_state: NvmeConfigurationLockState | None = None


class NvmeConfigurationLockState(RedfishModel):
    firmware_commit: ConfigLockOptions | None = None
    firmware_image_download: ConfigLockOptions | None = None
    lockdown: ConfigLockOptions | None = None
    security_send: ConfigLockOptions | None = None
    vpd_write: ConfigLockOptions | None = Field(alias="VPDWrite", default=None)


class Operations(RedfishModel):
    associated_task: IdRef | None = None
    operation: OperationType | None = None
    operation_name: str | None = None
    percentage_complete: int | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class RevertToOriginalFactoryState(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecureErase(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StatusIndicator(StrEnum):
    OK = "OK"
    FAIL = "Fail"
    REBUILD = "Rebuild"
    PREDICTIVE_FAILURE_ANALYSIS = "PredictiveFailureAnalysis"
    HOTSPARE = "Hotspare"
    IN_A_CRITICAL_ARRAY = "InACriticalArray"
    IN_A_FAILED_ARRAY = "InAFailedArray"


class TargetConfigurationLockLevel(StrEnum):
    BASELINE = "Baseline"
