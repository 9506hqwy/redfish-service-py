from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class UpdateServiceCapabilities(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#UpdateServiceCapabilities.v1_0_0.UpdateServiceCapabilities",
    )
    actions: Actions | None = None
    allowable_staging: list[str] | None = None
    allowable_targets: list[str] | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
