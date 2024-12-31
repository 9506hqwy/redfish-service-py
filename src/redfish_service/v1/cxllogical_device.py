from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Identifier, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


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
    qo_stelemetry_capabilities: QoStelemetryCapabilities | None = None
    semantics_supported: list[Cxlsemantic] | None = None
    status: Status | None = None


class Cxlsemantic(StrEnum):
    CXLIO = "CXLio"
    CXLCACHE = "CXLcache"
    CXLMEM = "CXLmem"


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    memory_chunks: list[IdRef] | None = None
    memory_domains: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class QoS(RedfishModel):
    allocated_bandwidth: str | None = None
    limit_percent: str | None = None


class QoStelemetryCapabilities(RedfishModel):
    egress_port_backpressure_supported: str | None = None
    temporary_throughput_reduction_supported: str | None = None
