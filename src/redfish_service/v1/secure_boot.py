from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ResetKeys(RedfishModel):
    target: str | None = None
    title: str | None = None


class SecureBoot(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    secure_boot_current_boot: str | None = None
    secure_boot_databases: IdRef | None = None
    secure_boot_enable: str | None = None
    secure_boot_mode: str | None = None
