from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class CoolantConnectorCollection(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#CoolantConnectorCollection.CoolantConnectorCollection",
    )
    description: str | None = None
    members: list[IdRef]
    members_odata_count: int = Field(serialization_alias="Members@odata.count")
    members_odata_next_link: str | None = Field(
        serialization_alias="Members@odata.nextLink", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
