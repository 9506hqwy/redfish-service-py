from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Device(RedfishModel):
    capacity_bytes: int | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishModel):
    chassis: IdRef | None = None
    oem: dict[str, Any] | None = None
    storage: IdRef | None = None


class SimpleStorage(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#SimpleStorage.v1_3_2.SimpleStorage")
    actions: Actions | None = None
    description: str | None = None
    devices: list[Device] | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    uefi_device_path: str | None = None
