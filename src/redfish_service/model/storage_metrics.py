from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .swordfish.io_statistics import IoStatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class StorageMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#StorageMetrics.v1_0_0.StorageMetrics"
    )
    actions: Actions | None = None
    compression_savings_bytes: int | None = None
    deduplication_savings_bytes: int | None = None
    description: str | None = None
    io_statistics: IoStatistics | None = Field(serialization_alias="IOStatistics", default=None)
    id: str
    name: str
    oem: dict[str, Any] | None = None
    state_change_count: float | None = None
    thin_provisioning_savings_bytes: int | None = None
