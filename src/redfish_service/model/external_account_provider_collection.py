from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class ExternalAccountProviderCollection(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type",
        default="#ExternalAccountProviderCollection.ExternalAccountProviderCollection",
    )
    description: str | None = None
    members: list[IdRef]
    members_odata_count: int = Field(alias="Members@odata.count")
    members_odata_next_link: str | None = Field(alias="Members@odata.nextLink", default=None)
    name: str
    oem: dict[str, Any] | None = None
