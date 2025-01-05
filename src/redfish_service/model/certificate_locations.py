from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CertificateLocations(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#CertificateLocations.v1_0_4.CertificateLocations"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    certificates: list[IdRef] | None = None
    certificates_odata_count: int | None = Field(alias="Certificates@odata.count", default=None)
    oem: dict[str, Any] | None = None
