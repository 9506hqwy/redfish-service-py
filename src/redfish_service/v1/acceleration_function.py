from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class AccelerationFunction(RedfishResource):
    acceleration_function_type: str | None = None
    actions: Actions | None = None
    description: str | None = None
    fpga_reconfiguration_slots: list[str] | None = None
    links: Links | None = None
    manufacturer: str | None = None
    oem: dict[str, Any] | None = None
    power_watts: int | None = None
    status: Status | None = None
    uuid: str | None = None
    version: str | None = None


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass
