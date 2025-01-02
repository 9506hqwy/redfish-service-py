from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.io_statistics import IoStatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class StorageServiceMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    oem: dict[str, Any] | None = None
