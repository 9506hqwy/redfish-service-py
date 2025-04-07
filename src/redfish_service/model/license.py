from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AuthorizationScope(StrEnum):
    DEVICE = "Device"
    CAPACITY = "Capacity"
    SERVICE = "Service"


class ContactInfo(RedfishModel):
    contact_name: str | None = None
    email_address: str | None = None
    phone_number: str | None = None


class License(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#License.v1_1_4.License")
    actions: Actions | None = None
    authorization_scope: AuthorizationScope | None = None
    contact: ContactInfo | None = None
    description: str | None = None
    download_uri: str | None = Field(serialization_alias="DownloadURI", default=None)
    entitlement_id: str | None = None
    expiration_date: str | None = None
    grace_period_days: int | None = None
    id: str
    install_date: str | None = None
    license_info_uri: str | None = Field(serialization_alias="LicenseInfoURI", default=None)
    license_origin: LicenseOrigin | None = None
    license_string: str | None = None
    license_type: LicenseType | None = None
    links: Links | None = None
    manufacturer: str | None = None
    max_authorized_devices: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    remaining_duration: str | None = None
    remaining_use_count: int | None = None
    removable: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None


class LicenseOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#License.v1_1_4.License"
    )
    actions: Actions | None = None
    authorization_scope: AuthorizationScope | None = None
    contact: ContactInfo | None = None
    description: str | None = None
    download_uri: str | None = Field(serialization_alias="DownloadURI", default=None)
    entitlement_id: str | None = None
    expiration_date: str | None = None
    grace_period_days: int | None = None
    id: str | None = None
    install_date: str | None = None
    license_info_uri: str | None = Field(serialization_alias="LicenseInfoURI", default=None)
    license_origin: LicenseOrigin | None = None
    license_string: str | None = None
    license_type: LicenseType | None = None
    links: Links | None = None
    manufacturer: str | None = None
    max_authorized_devices: int | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    remaining_duration: str | None = None
    remaining_use_count: int | None = None
    removable: bool | None = None
    sku: str | None = Field(serialization_alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None


class LicenseOrigin(StrEnum):
    BUILT_IN = "BuiltIn"
    INSTALLED = "Installed"


class LicenseType(StrEnum):
    PRODUCTION = "Production"
    PROTOTYPE = "Prototype"
    TRIAL = "Trial"


class Links(RedfishModel):
    authorized_devices: list[IdRef] | None = None
    authorized_devices_odata_count: int | None = Field(
        serialization_alias="AuthorizedDevices@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    target_services: list[IdRef] | None = None
    target_services_odata_count: int | None = Field(
        serialization_alias="TargetServices@odata.count", default=None
    )
