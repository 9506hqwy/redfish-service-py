from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class SpdmAlgorithmSet(RedfishModel):
    aead: list[str] | None = Field(serialization_alias="AEAD", default=None)
    base_asym: list[str] | None = None
    base_hash: list[str] | None = None


class SpdmParameterSet(RedfishModel):
    algorithms: SpdmAlgorithmSet | None = None
    versions: list[str] | None = None


class SpdmPolicy(RedfishModel):
    allow_extended_algorithms: bool | None = None
    allowed: SpdmParameterSet | None = None
    denied: SpdmParameterSet | None = None
    enabled: bool | None = None
    revoked_certificates: IdRef | None = None
    secure_session_enabled: bool | None = None
    trusted_certificates: IdRef | None = None
    verify_certificate: bool | None = None


class SecurityPolicy(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SecurityPolicy.v1_0_3.SecurityPolicy"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    override_parent_manager: bool | None = None
    spdm: SpdmPolicy | None = Field(serialization_alias="SPDM", default=None)
    status: Status | None = None
    tls: TlsCommunication | None = Field(serialization_alias="TLS", default=None)


class SecurityPolicyOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    override_parent_manager: bool | None = None
    spdm: SpdmPolicy | None = Field(serialization_alias="SPDM", default=None)
    status: Status | None = None
    tls: TlsCommunication | None = Field(serialization_alias="TLS", default=None)


class TlsAlgorithmSet(RedfishModel):
    cipher_suites: list[str] | None = None
    signature_algorithms: list[str] | None = None


class TlsCommunication(RedfishModel):
    client: TlsPolicy | None = None
    server: TlsPolicy | None = None


class TlsParameterSet(RedfishModel):
    algorithms: TlsAlgorithmSet | None = None
    versions: list[str] | None = None


class TlsPolicy(RedfishModel):
    allowed: TlsParameterSet | None = None
    denied: TlsParameterSet | None = None
    revoked_certificates: IdRef | None = None
    trusted_certificates: IdRef | None = None
    verify_certificate: bool | None = None
