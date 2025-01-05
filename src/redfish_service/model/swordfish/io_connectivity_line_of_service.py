from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..protocol import Protocol


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoConnectivityLineOfService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type",
        default="#IOConnectivityLineOfService.v1_2_1.IOConnectivityLineOfService",
    )
    access_protocols: list[Protocol] | None = None
    actions: Actions | None = None
    description: str | None = None
    id: str
    max_bytes_per_second: int | None = None
    max_iops: int | None = Field(alias="MaxIOPS", default=None)
    name: str
    oem: dict[str, Any] | None = None
