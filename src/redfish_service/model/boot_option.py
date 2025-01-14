from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .computer_system import BootSource
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BootOption(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#BootOption.v1_0_6.BootOption"
    )
    actions: Actions | None = None
    alias: BootSource | None = None
    boot_option_enabled: bool | None = None
    boot_option_reference: str | None = None
    description: str | None = None
    display_name: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(
        serialization_alias="RelatedItem@odata.count", default=None
    )
    uefi_device_path: str | None = None


class BootOptionOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#BootOption.v1_0_6.BootOption"
    )
    actions: Actions | None = None
    alias: BootSource | None = None
    boot_option_enabled: bool | None = None
    boot_option_reference: str | None = None
    description: str | None = None
    display_name: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(
        serialization_alias="RelatedItem@odata.count", default=None
    )
    uefi_device_path: str | None = None


class BootOptionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    boot_option_enabled: bool | None = None
    oem: dict[str, Any] | None = None
