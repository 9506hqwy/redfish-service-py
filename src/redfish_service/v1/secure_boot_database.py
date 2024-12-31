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


class SecureBootDatabase(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    database_id: str | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    signatures: IdRef | None = None
