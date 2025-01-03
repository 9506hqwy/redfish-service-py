from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..protocol import Protocol
from ..resource import Identifier


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoConnectivityLosCapabilities(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    identifier: Identifier | None = None
    max_supported_bytes_per_second: int | None = None
    max_supported_iops: int | None = Field(alias="MaxSupportedIOPS", default=None)
    name: str
    oem: dict[str, Any] | None = None
    supported_access_protocols: list[Protocol] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )
