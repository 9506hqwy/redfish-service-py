from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Identifier, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CxllogicalDevice(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifiers: list[Identifier] | None = None
    links: Links | None = None
    log: IdRef | None = None
    memory_regions: IdRef | None = None
    memory_size_mi_b: int | None = None
    oem: dict[str, Any] | None = None
    qo_s: QoS | None = None
    qo_stelemetry_capabilities: QoStelemetryCapabilities | None = Field(
        alias="QoSTelemetryCapabilities", default=None
    )
    semantics_supported: list[Cxlsemantic] | None = None
    status: Status | None = None


class Cxlsemantic(StrEnum):
    CXLIO = "CXLio"
    CXLCACHE = "CXLcache"
    CXLMEM = "CXLmem"


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    memory_chunks: list[IdRef] | None = None
    memory_chunks_odata_count: int | None = Field(alias="MemoryChunks@odata.count", default=None)
    memory_domains: list[IdRef] | None = None
    memory_domains_odata_count: int | None = Field(alias="MemoryDomains@odata.count", default=None)
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(alias="PCIeFunctions@odata.count", default=None)


class QoS(RedfishModel):
    allocated_bandwidth: str | None = None
    limit_percent: str | None = None


class QoStelemetryCapabilities(RedfishModel):
    egress_port_backpressure_supported: str | None = None
    temporary_throughput_reduction_supported: str | None = None
