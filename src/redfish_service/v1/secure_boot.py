from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    reset_keys: ResetKeys | None = Field(alias="#SecureBoot.ResetKeys", default=None)
    oem: dict[str, Any] | None = None


class ResetKeys(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecureBoot(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    secure_boot_current_boot: str | None = None
    secure_boot_databases: IdRef | None = None
    secure_boot_enable: str | None = None
    secure_boot_mode: str | None = None
