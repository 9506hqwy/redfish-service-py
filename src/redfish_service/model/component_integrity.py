from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    spdm_get_signed_measurements: SpdmGetSignedMeasurements | None = Field(
        serialization_alias="#ComponentIntegrity.SPDMGetSignedMeasurements", default=None
    )
    tpm_get_signed_measurements: TpmGetSignedMeasurements | None = Field(
        serialization_alias="#ComponentIntegrity.TPMGetSignedMeasurements", default=None
    )
    oem: dict[str, Any] | None = None


class ComponentIntegrity(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ComponentIntegrity.v1_3_0.ComponentIntegrity"
    )
    actions: Actions | None = None
    component_integrity_enabled: bool | None = None
    component_integrity_type: ComponentIntegrityType
    component_integrity_type_version: str
    description: str | None = None
    id: str
    last_updated: str | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    spdm: SpdMinfo | None = Field(serialization_alias="SPDM", default=None)
    status: Status | None = None
    tpm: TpMinfo | None = Field(serialization_alias="TPM", default=None)
    target_component_uri: str = Field(serialization_alias="TargetComponentURI")


class ComponentIntegrityOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    component_integrity_enabled: bool | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    spdm: SpdMinfo | None = Field(serialization_alias="SPDM", default=None)
    status: Status | None = None
    tpm: TpMinfo | None = Field(serialization_alias="TPM", default=None)


class ComponentIntegrityType(StrEnum):
    SPDM = "SPDM"
    TPM = "TPM"
    TCM = "TCM"
    TPCM = "TPCM"
    OEM = "OEM"


class DmtFmeasurementTypes(StrEnum):
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
        serialization_alias="ComponentsProtected@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MeasurementSpecification(StrEnum):
    DMTF = "DMTF"


class SpdmGetSignedMeasurements(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SpdMcommunication(RedfishModel):
    sessions: list[SingleSessionInfo] | None = None


class SpdMidentity(RedfishModel):
    requester_authentication: SpdMrequesterAuth | None = None
    responder_authentication: SpdMresponderAuth | None = None


class SpdMinfo(RedfishModel):
    component_communication: SpdMcommunication | None = None
    identity_authentication: SpdMidentity | None = None
    measurement_set: SpdMmeasurementSet | None = None
    requester: IdRef


class SpdMmeasurementSet(RedfishModel):
    measurement_specification: MeasurementSpecification | None = None
    measurement_summary: str | None = None
    measurement_summary_hash_algorithm: str | None = None
    measurement_summary_type: SpdMmeasurementSummaryType | None = None
    measurements: list[SpdMsingleMeasurement] | None = None
    oem: dict[str, Any] | None = None


class SpdMmeasurementSummaryType(StrEnum):
    TCB = "TCB"
    ALL = "All"


class SpdMrequesterAuth(RedfishModel):
    provided_certificate: IdRef | None = None


class SpdMresponderAuth(RedfishModel):
    component_certificate: IdRef | None = None
    verification_status: VerificationStatus | None = None


class SpdMsingleMeasurement(RedfishModel):
    last_updated: str | None = None
    measurement: str | None = None
    measurement_hash_algorithm: str | None = None
    measurement_index: int | None = None
    measurement_type: DmtFmeasurementTypes | None = None
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


class SpdmGetSignedMeasurementsRequest(RedfishModel):
    measurement_indices: list[int] | None = None
    nonce: str | None = None
    slot_id: int | None = None


class TpmGetSignedMeasurements(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class TpMauth(RedfishModel):
    component_certificate: IdRef | None = None
    verification_status: VerificationStatus | None = None


class TpMcommunication(RedfishModel):
    sessions: list[SingleSessionInfo] | None = None


class TpMinfo(RedfishModel):
    component_communication: TpMcommunication | None = None
    identity_authentication: TpMauth | None = None
    measurement_set: TpMmeasurementSet | None = None
    nonce_size_bytes_maximum: int | None = None


class TpMmeasurementSet(RedfishModel):
    measurements: list[TpMsingleMeasurement] | None = None


class TpMsingleMeasurement(RedfishModel):
    last_updated: str | None = None
    measurement: str | None = None
    measurement_hash_algorithm: str | None = None
    pcr: int | None = Field(serialization_alias="PCR", default=None)


class TpmGetSignedMeasurementsRequest(RedfishModel):
    certificate: IdRef
    nonce: str | None = None
    pcr_selection: str = Field(serialization_alias="PCRSelection")
    scheme: str


class VerificationStatus(StrEnum):
    SUCCESS = "Success"
    FAILED = "Failed"
