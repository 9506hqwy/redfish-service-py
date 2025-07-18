from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .key import EcdsaCurveType, SshKeyType
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    activate: Activate | None = Field(serialization_alias="#UpdateService.Activate", default=None)
    generate_ssh_identity_key_pair: GenerateSshIdentityKeyPair | None = Field(
        serialization_alias="#UpdateService.GenerateSSHIdentityKeyPair", default=None
    )
    remove_ssh_identity_key_pair: RemoveSshIdentityKeyPair | None = Field(
        serialization_alias="#UpdateService.RemoveSSHIdentityKeyPair", default=None
    )
    simple_update: SimpleUpdate | None = Field(
        serialization_alias="#UpdateService.SimpleUpdate", default=None
    )
    start_update: StartUpdate | None = Field(
        serialization_alias="#UpdateService.StartUpdate", default=None
    )
    oem: dict[str, Any] | None = None


class Activate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ActivateRequest(RedfishModel):
    targets: list[IdRef]


class ApplyTime(StrEnum):
    IMMEDIATE = "Immediate"
    ON_RESET = "OnReset"
    AT_MAINTENANCE_WINDOW_START = "AtMaintenanceWindowStart"
    IN_MAINTENANCE_WINDOW_ON_RESET = "InMaintenanceWindowOnReset"
    ON_START_UPDATE_REQUEST = "OnStartUpdateRequest"
    ON_TARGET_RESET = "OnTargetReset"


class GenerateSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class GenerateSshIdentityKeyPairRequest(RedfishModel):
    curve: EcdsaCurveType | None = None
    key_length: int | None = None
    key_type: SshKeyType


class HttpPushUriApplyTime(RedfishModel):
    apply_time: ApplyTime | None = None
    maintenance_window_duration_in_seconds: int | None = None
    maintenance_window_start_time: str | None = None


class HttpPushUriOptions(RedfishModel):
    force_update: bool | None = None
    http_push_uri_apply_time: HttpPushUriApplyTime | None = None


class RemoveSshIdentityKeyPair(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SimpleUpdate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SimpleUpdateRequest(RedfishModel):
    force_update: bool | None = None
    image_uri: str = Field(serialization_alias="ImageURI")
    password: str | None = None
    stage: bool | None = None
    targets: list[str] | None = None
    transfer_protocol: TransferProtocolType | None = None
    username: str | None = None


class StartUpdate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SupportedUpdateImageFormatType(StrEnum):
    PLDM_V1_0 = "PLDMv1_0"
    PLDM_V1_1 = "PLDMv1_1"
    PLDM_V1_2 = "PLDMv1_2"
    PLDM_V1_3 = "PLDMv1_3"
    UEFI_CAPSULE = "UEFICapsule"
    VENDOR_DEFINED = "VendorDefined"


class TransferProtocolType(StrEnum):
    CIFS = "CIFS"
    FTP = "FTP"
    SFTP = "SFTP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    NSF = "NSF"
    SCP = "SCP"
    TFTP = "TFTP"
    OEM = "OEM"
    NFS = "NFS"


class UpdateParameters(RedfishModel):
    force_update: bool | None = None
    oem: dict[str, Any] | None = None
    stage: bool | None = None
    targets: list[str] | None = None


class UpdateService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#UpdateService.v1_16_0.UpdateService"
    )
    actions: Actions | None = None
    client_certificates: IdRef | None = None
    description: str | None = None
    firmware_inventory: IdRef | None = None
    http_push_uri: str | None = None
    http_push_uri_options: HttpPushUriOptions | None = None
    http_push_uri_options_busy: bool | None = None
    http_push_uri_targets: list[str] | None = None
    http_push_uri_targets_busy: bool | None = None
    id: str
    max_image_size_bytes: int | None = None
    multipart_http_push_uri: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    public_identity_ssh_key: IdRef | None = Field(
        serialization_alias="PublicIdentitySSHKey", default=None
    )
    remote_server_certificates: IdRef | None = None
    remote_server_ssh_keys: IdRef | None = Field(
        serialization_alias="RemoteServerSSHKeys", default=None
    )
    service_enabled: bool | None = None
    software_inventory: IdRef | None = None
    status: Status | None = None
    supported_update_image_formats: list[SupportedUpdateImageFormatType] | None = None
    update_service_capabilities: IdRef | None = None
    verify_remote_server_certificate: bool | None = None
    verify_remote_server_ssh_key: bool | None = Field(
        serialization_alias="VerifyRemoteServerSSHKey", default=None
    )


class UpdateServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    http_push_uri_options: HttpPushUriOptions | None = None
    http_push_uri_options_busy: bool | None = None
    http_push_uri_targets: list[str] | None = None
    http_push_uri_targets_busy: bool | None = None
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None
    verify_remote_server_certificate: bool | None = None
    verify_remote_server_ssh_key: bool | None = Field(
        serialization_alias="VerifyRemoteServerSSHKey", default=None
    )
