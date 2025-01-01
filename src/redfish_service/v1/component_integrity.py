from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    spdmget_signed_measurements: SpdmgetSignedMeasurements | None = Field(
        alias="#ComponentIntegrity.SPDMGetSignedMeasurements", default=None
    )
    tpmget_signed_measurements: TpmgetSignedMeasurements | None = Field(
        alias="#ComponentIntegrity.TPMGetSignedMeasurements", default=None
    )
    oem: dict[str, Any] | None = None


class ComponentIntegrity(RedfishResource):
    actions: Actions | None = None
    component_integrity_enabled: bool | None = None
    component_integrity_type: ComponentIntegrityType
    component_integrity_type_version: str
    description: str | None = None
    last_updated: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    spdm: Spdminfo | None = Field(alias="SPDM", default=None)
    status: Status | None = None
    tpm: Tpminfo | None = Field(alias="TPM", default=None)
    target_component_uri: str = Field(alias="TargetComponentURI")


class ComponentIntegrityType(StrEnum):
    SPDM = "SPDM"
    TPM = "TPM"
    TCM = "TCM"
    TPCM = "TPCM"
    OEM = "OEM"


class Links(RedfishModel):
    components_protected: list[IdRef] | None = None
    components_protected_odata_count: int | None = Field(
        alias="ComponentsProtected@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class SpdmgetSignedMeasurements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Spdminfo(RedfishModel):
    component_communication: str | None = None
    identity_authentication: str | None = None
    measurement_set: str | None = None
    requester: IdRef


class TpmgetSignedMeasurements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Tpminfo(RedfishModel):
    component_communication: str | None = None
    identity_authentication: str | None = None
    measurement_set: str | None = None
    nonce_size_bytes_maximum: str | None = None
