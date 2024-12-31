from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class StorageServiceMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    iostatistics: Iostatistics | None = None
    oem: dict[str, Any] | None = None
