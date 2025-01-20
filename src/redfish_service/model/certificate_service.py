from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .certificate import CertificateType, KeyUsage
from .odata_v4 import IdRef


class Actions(RedfishModel):
    generate_csr: GenerateCsr | None = Field(
        serialization_alias="#CertificateService.GenerateCSR", default=None
    )
    replace_certificate: ReplaceCertificate | None = Field(
        serialization_alias="#CertificateService.ReplaceCertificate", default=None
    )
    oem: dict[str, Any] | None = None


class CertificateService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#CertificateService.v1_0_6.CertificateService"
    )
    actions: Actions | None = None
    certificate_locations: IdRef | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None


class GenerateCsr(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class GenerateCsrRequest(RedfishModel):
    alternative_names: list[str] | None = None
    certificate_collection: IdRef
    challenge_password: str | None = None
    city: str | None = None
    common_name: str
    contact_person: str | None = None
    country: str | None = None
    email: str | None = None
    given_name: str | None = None
    initials: str | None = None
    key_bit_length: int | None = None
    key_curve_id: str | None = None
    key_pair_algorithm: str | None = None
    key_usage: list[KeyUsage] | None = None
    organization: str | None = None
    organizational_unit: str | None = None
    state: str | None = None
    surname: str | None = None
    unstructured_name: str | None = None


class ReplaceCertificate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ReplaceCertificateRequest(RedfishModel):
    certificate_string: str
    certificate_type: CertificateType
    certificate_uri: IdRef
