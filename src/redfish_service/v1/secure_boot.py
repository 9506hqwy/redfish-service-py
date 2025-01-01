from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
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
    secure_boot_current_boot: SecureBootCurrentBootType | None = None
    secure_boot_databases: IdRef | None = None
    secure_boot_enable: bool | None = None
    secure_boot_mode: SecureBootModeType | None = None


class SecureBootCurrentBootType(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecureBootModeType(StrEnum):
    SETUP_MODE = "SetupMode"
    USER_MODE = "UserMode"
    AUDIT_MODE = "AuditMode"
    DEPLOYED_MODE = "DeployedMode"
