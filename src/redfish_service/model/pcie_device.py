from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CxlDevice(RedfishModel):
    capable_protocol_versions: list[CxlProtocolVersion] | None = None
    current_protocol_version: CxlProtocolVersion | None = None
    device_type: CxlDeviceType | None = None
    dynamic_capacity: CxlDynamicCapacity | None = None
    egress_port_congestion_support: bool | None = None
    max_number_logical_devices: int | None = None
    temporary_throughput_reduction_enabled: bool | None = None
    temporary_throughput_reduction_supported: bool | None = None
    throughput_reduction_support: bool | None = None
    timestamp: str | None = None


class CxlDeviceType(StrEnum):
    TYPE1 = "Type1"
    TYPE2 = "Type2"
    TYPE3 = "Type3"


class CxlDynamicCapacity(RedfishModel):
    add_capacity_policies_supported: list[CxlDynamicCapacityPolicies] | None = None
    max_dynamic_capacity_regions: int | None = None
    max_hosts: int | None = None
    memory_block_sizes_supported: list[CxlRegionBlockSizes] | None = None
    release_capacity_policies_supported: list[CxlDynamicCapacityPolicies] | None = None
    sanitization_on_release_support: list[CxlRegionSanitization] | None = None
    total_dynamic_capacity_mib: int | None = Field(
        serialization_alias="TotalDynamicCapacityMiB", default=None
    )


class CxlDynamicCapacityPolicies(StrEnum):
    FREE = "Free"
    CONTIGUOUS = "Contiguous"
    PRESCRIPTIVE = "Prescriptive"
    TAG_BASED = "TagBased"


class CxlProtocolVersion(StrEnum):
    CX_L1_1 = "CXL1_1"
    CX_L2_0 = "CXL2_0"
    CX_L3_0 = "CXL3_0"
    CX_L3_1 = "CXL3_1"
    CX_L3_2 = "CXL3_2"


class CxlRegionBlockSizes(RedfishModel):
    block_size_mib: list[int] | None = Field(serialization_alias="BlockSizeMiB", default=None)
    region_number: int | None = None


class CxlRegionSanitization(RedfishModel):
    region_number: int | None = None
    sanitization_on_release_supported: bool | None = None


class DeviceType(StrEnum):
    SINGLE_FUNCTION = "SingleFunction"
    MULTI_FUNCTION = "MultiFunction"
    SIMULATED = "Simulated"
    RETIMER = "Retimer"


class LaneSplittingType(StrEnum):
    NONE = "None"
    BRIDGED = "Bridged"
    BIFURCATED = "Bifurcated"


class Links(RedfishModel):
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(
        serialization_alias="Chassis@odata.count", default=None
    )
    connected_pcie_ports: list[IdRef] | None = Field(
        serialization_alias="ConnectedPCIePorts", default=None
    )
    connected_pcie_ports_odata_count: int | None = Field(
        serialization_alias="ConnectedPCIePorts@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(
        serialization_alias="PCIeFunctions@odata.count", default=None
    )
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(
        serialization_alias="Processors@odata.count", default=None
    )
    switch: IdRef | None = None


class PcieDevice(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PCIeDevice.v1_21_0.PCIeDevice"
    )
    actions: Actions | None = None
    assembly: IdRef | None = None
    asset_tag: str | None = None
    cxl_device: CxlDevice | None = Field(serialization_alias="CXLDevice", default=None)
    cxl_logical_devices: IdRef | None = Field(
        serialization_alias="CXLLogicalDevices", default=None
    )
    description: str | None = None
    device_type: DeviceType | None = None
    environment_metrics: IdRef | None = None
    firmware_version: str | None = None
    id: str
    links: Links | None = None
    location_indicator_active: bool | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    pcie_functions: IdRef | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)
    part_number: str | None = None
    ready_to_remove: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    slot: Slot | None = None
    spare_part_number: str | None = None
    staged_version: str | None = None
    status: Status | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)


class PcieDeviceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    asset_tag: str | None = None
    cxl_device: CxlDevice | None = Field(serialization_alias="CXLDevice", default=None)
    links: Links | None = None
    location_indicator_active: bool | None = None
    oem: dict[str, Any] | None = None
    pcie_interface: PcieInterface | None = Field(serialization_alias="PCIeInterface", default=None)
    ready_to_remove: bool | None = None
    slot: Slot | None = None
    status: Status | None = None


class PcieErrors(RedfishModel):
    bad_dllp_count: int | None = Field(serialization_alias="BadDLLPCount", default=None)
    bad_tlp_count: int | None = Field(serialization_alias="BadTLPCount", default=None)
    correctable_error_count: int | None = None
    fatal_error_count: int | None = None
    flow_control_timeout_errors: int | None = None
    l0_to_recovery_count: int | None = None
    nak_received_count: int | None = Field(serialization_alias="NAKReceivedCount", default=None)
    nak_sent_count: int | None = Field(serialization_alias="NAKSentCount", default=None)
    non_fatal_error_count: int | None = None
    replay_count: int | None = None
    replay_rollover_count: int | None = None
    unsupported_request_count: int | None = None


class PcieInterface(RedfishModel):
    lanes_in_use: int | None = None
    max_lanes: int | None = None
    max_pcie_type: PcieTypes | None = Field(serialization_alias="MaxPCIeType", default=None)
    oem: dict[str, Any] | None = None
    pcie_type: PcieTypes | None = Field(serialization_alias="PCIeType", default=None)


class PcieMetrics(RedfishModel):
    completion_credit_exhaustion_drops: int | None = None
    np_credit_exhaustion_drops: int | None = Field(
        serialization_alias="NPCreditExhaustionDrops", default=None
    )
    outbound_completion_tlp_bytes: int | None = Field(
        serialization_alias="OutboundCompletionTLPBytes", default=None
    )
    outbound_completion_tlp_count: int | None = Field(
        serialization_alias="OutboundCompletionTLPCount", default=None
    )
    outbound_read_tlp_bytes: int | None = Field(
        serialization_alias="OutboundReadTLPBytes", default=None
    )
    outbound_read_tlp_count: int | None = Field(
        serialization_alias="OutboundReadTLPCount", default=None
    )
    outbound_write_tlp_bytes: int | None = Field(
        serialization_alias="OutboundWriteTLPBytes", default=None
    )
    outbound_write_tlp_count: int | None = Field(
        serialization_alias="OutboundWriteTLPCount", default=None
    )
    tag_unavailability_drops: int | None = None


class PcieTypes(StrEnum):
    GEN1 = "Gen1"
    GEN2 = "Gen2"
    GEN3 = "Gen3"
    GEN4 = "Gen4"
    GEN5 = "Gen5"
    GEN6 = "Gen6"


class Slot(RedfishModel):
    hot_pluggable: bool | None = None
    lane_splitting: LaneSplittingType | None = None
    lanes: int | None = None
    location: Location | None = None
    pcie_type: PcieTypes | None = Field(serialization_alias="PCIeType", default=None)
    slot_type: SlotType | None = None


class SlotType(StrEnum):
    FULL_LENGTH = "FullLength"
    HALF_LENGTH = "HalfLength"
    LOW_PROFILE = "LowProfile"
    MINI = "Mini"
    M2 = "M2"
    OEM = "OEM"
    OCP3_SMALL = "OCP3Small"
    OCP3_LARGE = "OCP3Large"
    U2 = "U2"
    EDSFF = "EDSFF"
