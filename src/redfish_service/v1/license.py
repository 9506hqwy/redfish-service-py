from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ContactInfo(RedfishModel):
    contact_name: str | None = None
    email_address: str | None = None
    phone_number: str | None = None


class License(RedfishResource):
    actions: Actions | None = None
    authorization_scope: str | None = None
    contact: ContactInfo | None = None
    description: str | None = None
    download_uri: str | None = None
    entitlement_id: str | None = None
    expiration_date: str | None = None
    grace_period_days: str | None = None
    install_date: str | None = None
    license_info_uri: str | None = None
    license_origin: str | None = None
    license_string: str | None = None
    license_type: str | None = None
    links: Links | None = None
    manufacturer: str | None = None
    max_authorized_devices: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    remaining_duration: str | None = None
    remaining_use_count: str | None = None
    removable: str | None = None
    sku: str | None = None
    serial_number: str | None = None
    status: Status | None = None


class Links(RedfishModel):
    authorized_devices: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    target_services: list[IdRef] | None = None
