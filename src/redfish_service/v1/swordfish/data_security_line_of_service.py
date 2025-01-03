from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
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
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
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
