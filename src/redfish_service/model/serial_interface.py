from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class BitRate(StrEnum):
    N1200 = "1200"
    N2400 = "2400"
    N4800 = "4800"
    N9600 = "9600"
    N19200 = "19200"
    N38400 = "38400"
    N57600 = "57600"
    N115200 = "115200"
    N230400 = "230400"


class ConnectorType(StrEnum):
    RJ45 = "RJ45"
    RJ11 = "RJ11"
    D_B9_FEMALE = "DB9 Female"
    D_B9_MALE = "DB9 Male"
    D_B25_FEMALE = "DB25 Female"
    D_B25_MALE = "DB25 Male"
    USB = "USB"
    MUSB = "mUSB"
    UUSB = "uUSB"


class DataBits(StrEnum):
    N5 = "5"
    N6 = "6"
    N7 = "7"
    N8 = "8"


class FlowControl(StrEnum):
    NONE = "None"
    SOFTWARE = "Software"
    HARDWARE = "Hardware"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class Modbus(RedfishModel):
    read_only: bool | None = None
    role: Role | None = None
    server_id: int | None = None


class Parity(StrEnum):
    NONE = "None"
    EVEN = "Even"
    ODD = "Odd"
    MARK = "Mark"
    SPACE = "Space"


class PinOut(StrEnum):
    CISCO = "Cisco"
    CYCLADES = "Cyclades"
    DIGI = "Digi"
    MODBUS2_WIRE = "Modbus2Wire"
    MODBUS4_WIRE = "Modbus4Wire"
    MODBUS_RS232 = "ModbusRs232"


class Role(StrEnum):
    CLIENT = "Client"
    SERVER = "Server"


class SerialInterface(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SerialInterface.v1_3_0.SerialInterface"
    )
    actions: Actions | None = None
    bit_rate: BitRate | None = None
    connector_type: ConnectorType | None = None
    data_bits: DataBits | None = None
    description: str | None = None
    flow_control: FlowControl | None = None
    id: str
    interface_enabled: bool | None = None
    links: Links | None = None
    modbus: Modbus | None = None
    name: str
    oem: dict[str, Any] | None = None
    parity: Parity | None = None
    pin_out: PinOut | None = None
    signal_type: SignalType | None = None
    stop_bits: StopBits | None = None


class SerialInterfaceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    bit_rate: BitRate | None = None
    data_bits: DataBits | None = None
    flow_control: FlowControl | None = None
    interface_enabled: bool | None = None
    links: Links | None = None
    modbus: Modbus | None = None
    oem: dict[str, Any] | None = None
    parity: Parity | None = None
    stop_bits: StopBits | None = None


class SignalType(StrEnum):
    RS232 = "Rs232"
    RS485 = "Rs485"


class StopBits(StrEnum):
    N1 = "1"
    N2 = "2"
