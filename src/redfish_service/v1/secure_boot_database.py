from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class ResetKeys(RedfishResource):
    target: str | None = None
    title: str | None = None


class SecureBootDatabase(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    database_id: str | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    signatures: IdRef | None = None
