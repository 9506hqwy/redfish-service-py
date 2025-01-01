from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    reset_keys: ResetKeys | None = Field(alias="#SecureBootDatabase.ResetKeys", default=None)
    oem: dict[str, Any] | None = None


class ResetKeys(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SecureBootDatabase(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    database_id: str | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    signatures: IdRef | None = None
