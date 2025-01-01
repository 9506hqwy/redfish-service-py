from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CertificateLocations(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    certificates: list[IdRef] | None = None
    certificates_odata_count: int | None = Field(alias="Certificates@odata.count", default=None)
    oem: dict[str, Any] | None = None
