from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .certificate import KeyUsage
from .odata_v4 import IdRef


class AcmeChallengeType(StrEnum):
    HTTP01 = "Http01"
    DNS01 = "Dns01"


class AcmeConfiguration(RedfishModel):
    challenge_type: AcmeChallengeType | None = None
    eab_key: str | None = Field(serialization_alias="EABKey", default=None)
    eab_key_id: str | None = Field(serialization_alias="EABKeyId", default=None)
    email: str | None = None


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CsrParameters(RedfishModel):
    alternative_names: list[str] | None = None
    challenge_password: str | None = None
    city: str | None = None
    common_name: str | None = None
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


class CertificateEnrollment(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#CertificateEnrollment.v1_0_1.CertificateEnrollment",
    )
    acme: AcmeConfiguration | None = Field(serialization_alias="ACME", default=None)
    actions: Actions | None = None
    csr_parameters: CsrParameters | None = Field(serialization_alias="CSRParameters", default=None)
    description: str | None = None
    enabled: bool | None = None
    enrollment_state: EnrollmentState | None = None
    enrollment_type: EnrollmentProtocolType | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    renew_before_expiry_days: int | None = None
    scep: ScepConfiguration | None = Field(serialization_alias="SCEP", default=None)
    server_uri: str | None = Field(serialization_alias="ServerURI", default=None)
    verify_certificate: bool | None = None


class CertificateEnrollmentOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type",
        default="#CertificateEnrollment.v1_0_1.CertificateEnrollment",
    )
    acme: AcmeConfiguration | None = Field(serialization_alias="ACME", default=None)
    actions: Actions | None = None
    csr_parameters: CsrParameters | None = Field(serialization_alias="CSRParameters", default=None)
    description: str | None = None
    enabled: bool | None = None
    enrollment_state: EnrollmentState | None = None
    enrollment_type: EnrollmentProtocolType
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    renew_before_expiry_days: int | None = None
    scep: ScepConfiguration | None = Field(serialization_alias="SCEP", default=None)
    server_uri: str = Field(serialization_alias="ServerURI")
    verify_certificate: bool | None = None


class CertificateEnrollmentOnUpdate(RedfishModelOnUpdate):
    acme: AcmeConfiguration | None = Field(serialization_alias="ACME", default=None)
    actions: Actions | None = None
    csr_parameters: CsrParameters | None = Field(serialization_alias="CSRParameters", default=None)
    enabled: bool | None = None
    enrollment_state: EnrollmentState | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    renew_before_expiry_days: int | None = None
    scep: ScepConfiguration | None = Field(serialization_alias="SCEP", default=None)
    server_uri: str | None = Field(serialization_alias="ServerURI", default=None)
    verify_certificate: bool | None = None


class EnrollmentProtocolType(StrEnum):
    ACME = "ACME"
    SCEP = "SCEP"
    OEM = "OEM"


class EnrollmentState(RedfishModel):
    last_operation: LastOperationType | None = None
    last_operation_status: OperationStatus | None = None
    last_operation_time: str | None = None


class LastOperationType(StrEnum):
    RENEW = "Renew"
    UPDATE_ACME_EMAIL = "UpdateAcmeEmail"


class Links(RedfishModel):
    ca_certificates: list[IdRef] | None = Field(serialization_alias="CACertificates", default=None)
    ca_certificates_odata_count: int | None = Field(
        serialization_alias="CACertificates@odata.count", default=None
    )
    enrolled_certificate: IdRef | None = None
    enrolled_certificate_location: IdRef | None = None
    oem: dict[str, Any] | None = None


class OperationStatus(StrEnum):
    SUCCESS = "Success"
    FAILED = "Failed"
    IN_PROGRESS = "InProgress"
    UNKNOWN = "Unknown"


class ScepConfiguration(RedfishModel):
    challenge_password: str | None = None
