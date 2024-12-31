from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class StorageServiceMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    iostatistics: Iostatistics | None = None
    oem: dict[str, Any] | None = None
