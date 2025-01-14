from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    network_adapter: IdRef | None = None
    oem: dict[str, Any] | None = None


class NetworkInterface(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#NetworkInterface.v1_2_2.NetworkInterface"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    network_device_functions: IdRef | None = None
    network_ports: IdRef | None = None
    oem: dict[str, Any] | None = None
    ports: IdRef | None = None
    status: Status | None = None
