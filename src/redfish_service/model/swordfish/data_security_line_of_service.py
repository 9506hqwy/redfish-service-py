from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..swordfish.data_security_los_capabilities import (
    AntiVirusScanTrigger,
    AuthenticationType,
    DataSanitizationPolicy,
    KeySize,
    SecureChannelProtocol,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataSecurityLineOfService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#DataSecurityLineOfService.v1_1_1.DataSecurityLineOfService",
    )
    actions: Actions | None = None
    antivirus_engine_provider: str | None = None
    antivirus_scan_policies: list[AntiVirusScanTrigger] | None = None
    channel_encryption_strength: KeySize | None = None
    data_sanitization_policy: DataSanitizationPolicy | None = None
    description: str | None = None
    host_authentication_type: AuthenticationType | None = None
    id: str
    media_encryption_strength: KeySize | None = None
    name: str
    oem: dict[str, Any] | None = None
    secure_channel_protocol: SecureChannelProtocol | None = None
    user_authentication_type: AuthenticationType | None = None


class DataSecurityLineOfServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    antivirus_engine_provider: str | None = None
    antivirus_scan_policies: list[AntiVirusScanTrigger] | None = None
    channel_encryption_strength: KeySize | None = None
    data_sanitization_policy: DataSanitizationPolicy | None = None
    host_authentication_type: AuthenticationType | None = None
    media_encryption_strength: KeySize | None = None
    oem: dict[str, Any] | None = None
    secure_channel_protocol: SecureChannelProtocol | None = None
    user_authentication_type: AuthenticationType | None = None
