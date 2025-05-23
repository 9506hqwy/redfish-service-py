from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef


class Actions(RedfishModel):
    reset_keys: ResetKeys | None = Field(serialization_alias="#SecureBoot.ResetKeys", default=None)
    oem: dict[str, Any] | None = None


class ResetKeys(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetKeysRequest(RedfishModel):
    reset_keys_type: ResetKeysType


class ResetKeysType(StrEnum):
    RESET_ALL_KEYS_TO_DEFAULT = "ResetAllKeysToDefault"
    DELETE_ALL_KEYS = "DeleteAllKeys"
    DELETE_PK = "DeletePK"


class SecureBoot(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SecureBoot.v1_1_2.SecureBoot"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    secure_boot_current_boot: SecureBootCurrentBootType | None = None
    secure_boot_databases: IdRef | None = None
    secure_boot_enable: bool | None = None
    secure_boot_mode: SecureBootModeType | None = None


class SecureBootOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    secure_boot_enable: bool | None = None


class SecureBootCurrentBootType(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SecureBootModeType(StrEnum):
    SETUP_MODE = "SetupMode"
    USER_MODE = "UserMode"
    AUDIT_MODE = "AuditMode"
    DEPLOYED_MODE = "DeployedMode"
