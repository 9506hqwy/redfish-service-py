from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CertificateService(RedfishResource):
    actions: Actions | None = None
    certificate_locations: IdRef | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None


class GenerateCsr(RedfishModel):
    target: str | None = None
    title: str | None = None


class ReplaceCertificate(RedfishModel):
    target: str | None = None
    title: str | None = None
