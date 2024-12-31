from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class BootOption(RedfishResource):
    actions: Actions | None = None
    alias: str | None = None
    boot_option_enabled: str | None = None
    boot_option_reference: str
    description: str | None = None
    display_name: str | None = None
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    uefi_device_path: str | None = None


class OemActions(RedfishResource):
    pass
