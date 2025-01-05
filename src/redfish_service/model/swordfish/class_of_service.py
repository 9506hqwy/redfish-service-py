from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..resource import Identifier


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ClassOfService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#ClassOfService.v1_2_0.ClassOfService")
    actions: Actions | None = None
    class_of_service_version: str | None = None
    data_protection_lines_of_service: list[IdRef] | None = None
    data_protection_lines_of_service_odata_count: int | None = Field(
        alias="DataProtectionLinesOfService@odata.count", default=None
    )
    data_security_lines_of_service: list[IdRef] | None = None
    data_security_lines_of_service_odata_count: int | None = Field(
        alias="DataSecurityLinesOfService@odata.count", default=None
    )
    data_storage_lines_of_service: list[IdRef] | None = None
    data_storage_lines_of_service_odata_count: int | None = Field(
        alias="DataStorageLinesOfService@odata.count", default=None
    )
    description: str | None = None
    io_connectivity_lines_of_service: list[IdRef] | None = Field(
        alias="IOConnectivityLinesOfService", default=None
    )
    io_connectivity_lines_of_service_odata_count: int | None = Field(
        alias="IOConnectivityLinesOfService@odata.count", default=None
    )
    io_performance_lines_of_service: list[IdRef] | None = Field(
        alias="IOPerformanceLinesOfService", default=None
    )
    io_performance_lines_of_service_odata_count: int | None = Field(
        alias="IOPerformanceLinesOfService@odata.count", default=None
    )
    id: str
    identifier: Identifier | None = None
    name: str
    oem: dict[str, Any] | None = None
