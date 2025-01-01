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


class DmtfmeasurementTypes(StrEnum):
    IMMUTABLE_ROM = "ImmutableROM"
    MUTABLE_FIRMWARE = "MutableFirmware"
    HARDWARE_CONFIGURATION = "HardwareConfiguration"
    FIRMWARE_CONFIGURATION = "FirmwareConfiguration"
    MUTABLE_FIRMWARE_VERSION = "MutableFirmwareVersion"
    MUTABLE_FIRMWARE_SECURITY_VERSION_NUMBER = "MutableFirmwareSecurityVersionNumber"
    MEASUREMENT_MANIFEST = "MeasurementManifest"


class Links(RedfishModel):
    components_protected: list[IdRef] | None = None
    components_protected_odata_count: int | None = Field(
        alias="ComponentsProtected@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MeasurementSpecification(StrEnum):
    DMTF = "DMTF"


class SpdmgetSignedMeasurements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Spdmcommunication(RedfishModel):
    sessions: list[SingleSessionInfo] | None = None


class Spdmidentity(RedfishModel):
    requester_authentication: SpdmrequesterAuth | None = None
    responder_authentication: SpdmresponderAuth | None = None


class Spdminfo(RedfishModel):
    component_communication: Spdmcommunication | None = None
    identity_authentication: Spdmidentity | None = None
    measurement_set: SpdmmeasurementSet | None = None
    requester: IdRef


class SpdmmeasurementSet(RedfishModel):
    measurement_specification: MeasurementSpecification | None = None
    measurement_summary: str | None = None
    measurement_summary_hash_algorithm: str | None = None
    measurement_summary_type: SpdmmeasurementSummaryType | None = None
    measurements: list[SpdmsingleMeasurement] | None = None
    oem: dict[str, Any] | None = None


class SpdmmeasurementSummaryType(StrEnum):
    TCB = "TCB"
    ALL = "All"


class SpdmrequesterAuth(RedfishModel):
    provided_certificate: IdRef | None = None


class SpdmresponderAuth(RedfishModel):
    component_certificate: IdRef | None = None
    verification_status: VerificationStatus | None = None


class SpdmsingleMeasurement(RedfishModel):
    last_updated: str | None = None
    measurement: str | None = None
    measurement_hash_algorithm: str | None = None
    measurement_index: int | None = None
    measurement_type: DmtfmeasurementTypes | None = None
    oem: dict[str, Any] | None = None
    partof_summary_hash: bool | None = None
    security_version_number: str | None = None


class SecureSessionType(StrEnum):
    PLAIN = "Plain"
    ENCRYPTED_AUTHENTICATED = "EncryptedAuthenticated"
    AUTHENTICATED_ONLY = "AuthenticatedOnly"


class SingleSessionInfo(RedfishModel):
    session_id: int | None = None
    session_type: SecureSessionType | None = None


class TpmgetSignedMeasurements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Tpmauth(RedfishModel):
    component_certificate: IdRef | None = None
    verification_status: VerificationStatus | None = None


class Tpmcommunication(RedfishModel):
    sessions: list[SingleSessionInfo] | None = None


class Tpminfo(RedfishModel):
    component_communication: Tpmcommunication | None = None
    identity_authentication: Tpmauth | None = None
    measurement_set: TpmmeasurementSet | None = None
    nonce_size_bytes_maximum: int | None = None


class TpmmeasurementSet(RedfishModel):
    measurements: list[TpmsingleMeasurement] | None = None


class TpmsingleMeasurement(RedfishModel):
    last_updated: str | None = None
    measurement: str | None = None
    measurement_hash_algorithm: str | None = None
    pcr: int | None = Field(alias="PCR", default=None)


class VerificationStatus(StrEnum):
    SUCCESS = "Success"
    FAILED = "Failed"
