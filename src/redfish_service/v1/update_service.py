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
    generate_sshidentity_key_pair: GenerateSshidentityKeyPair | None = Field(
        alias="#UpdateService.GenerateSSHIdentityKeyPair", default=None
    )
    remove_sshidentity_key_pair: RemoveSshidentityKeyPair | None = Field(
        alias="#UpdateService.RemoveSSHIdentityKeyPair", default=None
    )
    simple_update: SimpleUpdate | None = Field(alias="#UpdateService.SimpleUpdate", default=None)
    start_update: StartUpdate | None = Field(alias="#UpdateService.StartUpdate", default=None)
    oem: dict[str, Any] | None = None


class ApplyTime(StrEnum):
    IMMEDIATE = "Immediate"
    ON_RESET = "OnReset"
    AT_MAINTENANCE_WINDOW_START = "AtMaintenanceWindowStart"
    IN_MAINTENANCE_WINDOW_ON_RESET = "InMaintenanceWindowOnReset"
    ON_START_UPDATE_REQUEST = "OnStartUpdateRequest"
    ON_TARGET_RESET = "OnTargetReset"


class GenerateSshidentityKeyPair(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class HttpPushUriApplyTime(RedfishModel):
    apply_time: ApplyTime | None = None
    maintenance_window_duration_in_seconds: int | None = None
    maintenance_window_start_time: str | None = None


class HttpPushUriOptions(RedfishModel):
    force_update: bool | None = None
    http_push_uri_apply_time: HttpPushUriApplyTime | None = None


class RemoveSshidentityKeyPair(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SimpleUpdate(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class StartUpdate(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class UpdateParameters(RedfishModel):
    force_update: bool | None = None
    oem: dict[str, Any] | None = None
    targets: list[str] | None = None


class UpdateService(RedfishResource):
    actions: Actions | None = None
    client_certificates: IdRef | None = None
    description: str | None = None
    firmware_inventory: IdRef | None = None
    http_push_uri: str | None = None
    http_push_uri_options: HttpPushUriOptions | None = None
    http_push_uri_options_busy: str | None = None
    http_push_uri_targets: list[str] | None = None
    http_push_uri_targets_busy: str | None = None
    max_image_size_bytes: str | None = None
    multipart_http_push_uri: str | None = None
    oem: dict[str, Any] | None = None
    public_identity_sshkey: IdRef | None = Field(alias="PublicIdentitySSHKey", default=None)
    remote_server_certificates: IdRef | None = None
    remote_server_sshkeys: IdRef | None = Field(alias="RemoteServerSSHKeys", default=None)
    service_enabled: str | None = None
    software_inventory: IdRef | None = None
    status: Status | None = None
    supported_update_image_formats: list[str] | None = None
    verify_remote_server_certificate: str | None = None
    verify_remote_server_sshkey: str | None = Field(alias="VerifyRemoteServerSSHKey", default=None)
