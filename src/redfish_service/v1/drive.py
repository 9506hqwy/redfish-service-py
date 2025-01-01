from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Identifier, Location, Status
from .software_inventory import MeasurementBlock


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Drive.Reset", default=None)
    revert_to_original_factory_state: RevertToOriginalFactoryState | None = Field(
        alias="#Drive.RevertToOriginalFactoryState", default=None
    )
    secure_erase: SecureErase | None = Field(alias="#Drive.SecureErase", default=None)
    oem: dict[str, Any] | None = None


class Drive(RedfishResource):
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    block_security_idenabled: str | None = Field(alias="BlockSecurityIDEnabled", default=None)
    block_size_bytes: str | None = None
    capable_speed_gbs: str | None = None
    capacity_bytes: str | None = None
    certificates: IdRef | None = None
    configuration_lock: str | None = None
    description: str | None = None
    drive_form_factor: str | None = None
    encryption_ability: str | None = None
    encryption_status: str | None = None
    environment_metrics: IdRef | None = None
    failure_predicted: str | None = None
    firmware_version: str | None = None
    hotspare_replacement_mode: str | None = None
    hotspare_type: str | None = None
    identifiers: list[Identifier] | None = None
    indicator_led: str | None = Field(alias="IndicatorLED", default=None)
    links: Links | None = None
    location: list[Location] | None = None
    location_indicator_active: str | None = None
    manufacturer: str | None = None
    measurements: list[MeasurementBlock] | None = None
    media_type: str | None = None
    metrics: str | None = None
    model: str | None = None
    multipath: str | None = None
    nvme: str | None = Field(alias="NVMe", default=None)
    negotiated_speed_gbs: str | None = None
    oem: dict[str, Any] | None = None
    operations: list[Operations] | None = None
    part_number: str | None = None
    physical_location: Location | None = None
    predicted_media_life_left_percent: str | None = None
    protocol: str | None = None
    ready_to_remove: str | None = None
    revision: str | None = None
    rotation_speed_rpm: str | None = Field(alias="RotationSpeedRPM", default=None)
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    slot_capable_protocols: list[str] | None = None
    slot_form_factor: str | None = None
    spare_part_number: str | None = None
    status: Status | None = None
    status_indicator: str | None = None
    target_configuration_lock_level: str | None = None
    write_cache_enabled: str | None = None


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


class Operations(RedfishModel):
    associated_task: IdRef | None = None
    operation: str | None = None
    operation_name: str | None = None
    percentage_complete: str | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class RevertToOriginalFactoryState(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecureErase(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
