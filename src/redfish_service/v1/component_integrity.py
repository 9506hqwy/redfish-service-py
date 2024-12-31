from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class ComponentIntegrity(RedfishResource):
    actions: Actions | None = None
    component_integrity_enabled: bool | None = None
    component_integrity_type: ComponentIntegrityType
    component_integrity_type_version: str
    description: str | None = None
    last_updated: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    spdm: Spdminfo | None = None
    status: Status | None = None
    tpm: Tpminfo | None = None
    target_component_uri: str


class ComponentIntegrityType(StrEnum):
    SPDM = "SPDM"
    TPM = "TPM"
    TCM = "TCM"
    TPCM = "TPCM"
    OEM = "OEM"


class Links(RedfishResource):
    components_protected: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass


class SpdmgetSignedMeasurements(RedfishResource):
    target: str | None = None
    title: str | None = None


class Spdminfo(RedfishResource):
    component_communication: str | None = None
    identity_authentication: str | None = None
    measurement_set: str | None = None
    requester: IdRef


class TpmgetSignedMeasurements(RedfishResource):
    target: str | None = None
    title: str | None = None


class Tpminfo(RedfishResource):
    component_communication: str | None = None
    identity_authentication: str | None = None
    measurement_set: str | None = None
    nonce_size_bytes_maximum: str | None = None
