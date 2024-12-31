from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class Certificate(RedfishResource):
    actions: Actions | None = None
    certificate_string: str | None = None
    certificate_type: str | None = None
    certificate_usage_types: list[str] | None = None
    description: str | None = None
    fingerprint: str | None = None
    fingerprint_hash_algorithm: str | None = None
    issuer: Identifier | None = None
    key_usage: list[str] | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    spdm: Spdm | None = None
    serial_number: str | None = None
    signature_algorithm: str | None = None
    subject: Identifier | None = None
    uefi_signature_owner: str | None = None
    valid_not_after: str | None = None
    valid_not_before: str | None = None


class CertificateType(StrEnum):
    PEM = "PEM"
    PEMCHAIN = "PEMchain"
    PKCS7 = "PKCS7"


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
    CRLSIGNING = "CRLSigning"
    ENCIPHER_ONLY = "EncipherOnly"
    DECIPHER_ONLY = "DecipherOnly"
    SERVER_AUTHENTICATION = "ServerAuthentication"
    CLIENT_AUTHENTICATION = "ClientAuthentication"
    CODE_SIGNING = "CodeSigning"
    EMAIL_PROTECTION = "EmailProtection"
    TIMESTAMPING = "Timestamping"
    OCSPSIGNING = "OCSPSigning"


class Links(RedfishModel):
    issuer: str | None = None
    oem: dict[str, Any] | None = None
    subjects: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class Rekey(RedfishModel):
    target: str | None = None
    title: str | None = None


class Renew(RedfishModel):
    target: str | None = None
    title: str | None = None


class Spdm(RedfishModel):
    slot_id: str | None = None
