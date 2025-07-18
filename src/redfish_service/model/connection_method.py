from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ConnectionMethod(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ConnectionMethod.v1_2_0.ConnectionMethod"
    )
    actions: Actions | None = None
    connection_method_type: ConnectionMethodType | None = None
    connection_method_variant: str | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    tunneling_protocol: TunnelingProtocolType | None = None


class ConnectionMethodOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#ConnectionMethod.v1_2_0.ConnectionMethod"
    )
    actions: Actions | None = None
    connection_method_type: ConnectionMethodType | None = None
    connection_method_variant: str | None = None
    description: str | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    tunneling_protocol: TunnelingProtocolType | None = None


class ConnectionMethodType(StrEnum):
    REDFISH = "Redfish"
    SNMP = "SNMP"
    IPMI15 = "IPMI15"
    IPMI20 = "IPMI20"
    NETCONF = "NETCONF"
    OEM = "OEM"
    MODBUS_SERIAL = "ModbusSerial"
    MODBUS_TCP = "ModbusTCP"


class Links(RedfishModel):
    aggregation_sources: list[IdRef] | None = None
    aggregation_sources_odata_count: int | None = Field(
        serialization_alias="AggregationSources@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    serial_interface: IdRef | None = None


class TunnelingProtocolType(StrEnum):
    SSH = "SSH"
    OEM = "OEM"
