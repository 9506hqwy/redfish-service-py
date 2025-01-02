from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    generate_csr: GenerateCsr | None = Field(alias="#CertificateService.GenerateCSR", default=None)
    replace_certificate: ReplaceCertificate | None = Field(
        alias="#CertificateService.ReplaceCertificate", default=None
    )
    oem: dict[str, Any] | None = None


class CertificateService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    certificate_locations: IdRef | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None


class GenerateCsr(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ReplaceCertificate(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)
