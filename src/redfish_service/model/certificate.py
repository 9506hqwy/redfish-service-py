from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef


class Actions(RedfishModel):
    rekey: Rekey | None = Field(serialization_alias="#Certificate.Rekey", default=None)
    renew: Renew | None = Field(serialization_alias="#Certificate.Renew", default=None)
    oem: dict[str, Any] | None = None


class Certificate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Certificate.v1_9_0.Certificate"
    )
    actions: Actions | None = None
    certificate_string: str | None = None
    certificate_type: CertificateType | None = None
    certificate_usage_types: list[CertificateUsageType] | None = None
    description: str | None = None
    fingerprint: str | None = None
    fingerprint_hash_algorithm: str | None = None
    id: str
    issuer: Identifier | None = None
    key_usage: list[KeyUsage] | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    spdm: Spdm | None = Field(serialization_alias="SPDM", default=None)
    serial_number: str | None = None
    signature_algorithm: str | None = None
    subject: Identifier | None = None
    uefi_signature_owner: str | None = None
    valid_not_after: str | None = None
    valid_not_before: str | None = None


class CertificateOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Certificate.v1_9_0.Certificate"
    )
    actions: Actions | None = None
    certificate_string: str | None = None
    certificate_type: CertificateType | None = None
    certificate_usage_types: list[CertificateUsageType] | None = None
    description: str | None = None
    fingerprint: str | None = None
    fingerprint_hash_algorithm: str | None = None
    id: str | None = None
    issuer: Identifier | None = None
    key_usage: list[KeyUsage] | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    spdm: Spdm | None = Field(serialization_alias="SPDM", default=None)
    serial_number: str | None = None
    signature_algorithm: str | None = None
    subject: Identifier | None = None
    uefi_signature_owner: str | None = None
    valid_not_after: str | None = None
    valid_not_before: str | None = None


class CertificateOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    issuer: Identifier | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    spdm: Spdm | None = Field(serialization_alias="SPDM", default=None)
    subject: Identifier | None = None


class CertificateType(StrEnum):
    PEM = "PEM"
    PE_MCHAIN = "PEMchain"
    PKCS7 = "PKCS7"


class CertificateUsageType(StrEnum):
    USER = "User"
    WEB = "Web"
    SSH = "SSH"
    DEVICE = "Device"
    PLATFORM = "Platform"
    BIOS = "BIOS"
    I_DEV_ID = "IDevID"
    L_DEV_ID = "LDevID"
    IAK = "IAK"
    LAK = "LAK"
    EK = "EK"


class Identifier(RedfishModel):
    additional_common_names: list[str] | None = None
    additional_organizational_units: list[str] | None = None
    alternative_names: list[str] | None = None
    city: str | None = None
    common_name: str | None = None
    country: str | None = None
    display_string: str | None = None
    domain_components: list[str] | None = None
    email: str | None = None
    organization: str | None = None
    organizational_unit: str | None = None
    state: str | None = None


class KeyUsage(StrEnum):
    DIGITAL_SIGNATURE = "DigitalSignature"
    NON_REPUDIATION = "NonRepudiation"
    KEY_ENCIPHERMENT = "KeyEncipherment"
    DATA_ENCIPHERMENT = "DataEncipherment"
    KEY_AGREEMENT = "KeyAgreement"
    KEY_CERT_SIGN = "KeyCertSign"
    CRL_SIGNING = "CRLSigning"
    ENCIPHER_ONLY = "EncipherOnly"
    DECIPHER_ONLY = "DecipherOnly"
    SERVER_AUTHENTICATION = "ServerAuthentication"
    CLIENT_AUTHENTICATION = "ClientAuthentication"
    CODE_SIGNING = "CodeSigning"
    EMAIL_PROTECTION = "EmailProtection"
    TIMESTAMPING = "Timestamping"
    OCSP_SIGNING = "OCSPSigning"


class Links(RedfishModel):
    issuer: IdRef | None = None
    oem: dict[str, Any] | None = None
    subjects: list[IdRef] | None = None
    subjects_odata_count: int | None = Field(
        serialization_alias="Subjects@odata.count", default=None
    )


class Rekey(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class RekeyRequest(RedfishModel):
    challenge_password: str | None = None
    key_bit_length: int | None = None
    key_curve_id: str | None = None
    key_pair_algorithm: str | None = None


class Renew(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class RenewRequest(RedfishModel):
    challenge_password: str | None = None


class Spdm(RedfishModel):
    slot_id: int | None = None
