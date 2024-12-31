from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class SpdmalgorithmSet(RedfishResource):
    aead: list[str] | None = None
    base_asym: list[str] | None = None
    base_hash: list[str] | None = None


class SpdmparameterSet(RedfishResource):
    algorithms: SpdmalgorithmSet | None = None
    versions: list[str] | None = None


class Spdmpolicy(RedfishResource):
    allow_extended_algorithms: str | None = None
    allowed: SpdmparameterSet | None = None
    denied: SpdmparameterSet | None = None
    enabled: str | None = None
    revoked_certificates: IdRef | None = None
    secure_session_enabled: str | None = None
    trusted_certificates: IdRef | None = None
    verify_certificate: str | None = None


class SecurityPolicy(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    override_parent_manager: bool | None = None
    spdm: Spdmpolicy | None = None
    status: Status | None = None
    tls: Tlscommunication | None = None


class TlsalgorithmSet(RedfishResource):
    cipher_suites: list[str] | None = None
    signature_algorithms: list[str] | None = None


class Tlscommunication(RedfishResource):
    client: Tlspolicy | None = None
    server: Tlspolicy | None = None


class TlsparameterSet(RedfishResource):
    algorithms: TlsalgorithmSet | None = None
    versions: list[str] | None = None


class Tlspolicy(RedfishResource):
    allowed: TlsparameterSet | None = None
    denied: TlsparameterSet | None = None
    revoked_certificates: IdRef | None = None
    trusted_certificates: IdRef | None = None
    verify_certificate: str | None = None
