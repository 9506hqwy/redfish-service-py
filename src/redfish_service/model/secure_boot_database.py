from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    reset_keys: ResetKeys | None = Field(
        serialization_alias="#SecureBootDatabase.ResetKeys", default=None
    )
    oem: dict[str, Any] | None = None


class ResetKeys(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetKeysRequest(RedfishModel):
    reset_keys_type: ResetKeysType


class ResetKeysType(StrEnum):
    RESET_ALL_KEYS_TO_DEFAULT = "ResetAllKeysToDefault"
    DELETE_ALL_KEYS = "DeleteAllKeys"


class SecureBootDatabase(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SecureBootDatabase.v1_0_3.SecureBootDatabase"
    )
    actions: Actions | None = None
    certificates: IdRef | None = None
    database_id: str | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    signatures: IdRef | None = None
