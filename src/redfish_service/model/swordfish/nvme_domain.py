from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DomainContents(RedfishModel):
    controllers: list[IdRef] | None = None
    controllers_odata_count: int | None = Field(
        serialization_alias="Controllers@odata.count", default=None
    )
    namespaces: list[IdRef] | None = None
    namespaces_odata_count: int | None = Field(
        serialization_alias="Namespaces@odata.count", default=None
    )


class Links(RedfishModel):
    associated_domains: list[IdRef] | None = None
    associated_domains_odata_count: int | None = Field(
        serialization_alias="AssociatedDomains@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class NvmeDomain(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#NVMeDomain.v1_2_0.NVMeDomain"
    )
    ana_group_id: float | None = Field(serialization_alias="ANAGroupId", default=None)
    actions: Actions | None = None
    available_firmware_images: list[IdRef] | None = None
    available_firmware_images_odata_count: int | None = Field(
        serialization_alias="AvailableFirmwareImages@odata.count", default=None
    )
    description: str | None = None
    domain_contents: DomainContents | None = None
    domain_members: list[IdRef] | None = None
    domain_members_odata_count: int | None = Field(
        serialization_alias="DomainMembers@odata.count", default=None
    )
    firmware_images: list[IdRef] | None = None
    firmware_images_odata_count: int | None = Field(
        serialization_alias="FirmwareImages@odata.count", default=None
    )
    id: str
    links: Links | None = None
    max_namespaces_supported_per_controller: float | None = None
    maximum_capacity_per_endurance_group_bytes: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    total_domain_capacity_bytes: int | None = None
    unallocated_domain_capacity_bytes: int | None = None


class NvmeDomainOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#NVMeDomain.v1_2_0.NVMeDomain"
    )
    ana_group_id: float | None = Field(serialization_alias="ANAGroupId", default=None)
    actions: Actions | None = None
    available_firmware_images: list[IdRef] | None = None
    available_firmware_images_odata_count: int | None = Field(
        serialization_alias="AvailableFirmwareImages@odata.count", default=None
    )
    description: str | None = None
    domain_contents: DomainContents | None = None
    domain_members: list[IdRef] | None = None
    domain_members_odata_count: int | None = Field(
        serialization_alias="DomainMembers@odata.count", default=None
    )
    firmware_images: list[IdRef] | None = None
    firmware_images_odata_count: int | None = Field(
        serialization_alias="FirmwareImages@odata.count", default=None
    )
    id: str | None = None
    links: Links | None = None
    max_namespaces_supported_per_controller: float | None = None
    maximum_capacity_per_endurance_group_bytes: int | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    total_domain_capacity_bytes: int | None = None
    unallocated_domain_capacity_bytes: int | None = None


class NvmeDomainOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    available_firmware_images: list[IdRef] | None = None
    domain_contents: DomainContents | None = None
    domain_members: list[IdRef] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
