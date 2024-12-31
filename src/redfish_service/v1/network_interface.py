from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    network_adapter: IdRef | None = None
    oem: dict[str, Any] | None = None


class NetworkInterface(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    links: Links | None = None
    network_device_functions: IdRef | None = None
    network_ports: IdRef | None = None
    oem: dict[str, Any] | None = None
    ports: IdRef | None = None
    status: Status | None = None


class OemActions(RedfishResource):
    pass
