from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(alias="#PortMetrics.ResetMetrics", default=None)
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    backpressure_average_percentage: int | None = None


class FibreChannel(RedfishModel):
    correctable_fecerrors: int | None = Field(alias="CorrectableFECErrors", default=None)
    invalid_crcs: int | None = Field(alias="InvalidCRCs", default=None)
    invalid_txwords: int | None = Field(alias="InvalidTXWords", default=None)
    link_failures: int | None = None
    losses_of_signal: int | None = None
    losses_of_sync: int | None = None
    rxbbcredit_zero: int | None = Field(alias="RXBBCreditZero", default=None)
    rxexchanges: int | None = Field(alias="RXExchanges", default=None)
    rxsequences: int | None = Field(alias="RXSequences", default=None)
    txbbcredit_zero: int | None = Field(alias="TXBBCreditZero", default=None)
    txbbcredit_zero_duration_milliseconds: int | None = Field(
        alias="TXBBCreditZeroDurationMilliseconds", default=None
    )
    txbbcredits: int | None = Field(alias="TXBBCredits", default=None)
    txexchanges: int | None = Field(alias="TXExchanges", default=None)
    txsequences: int | None = Field(alias="TXSequences", default=None)
    uncorrectable_fecerrors: int | None = Field(alias="UncorrectableFECErrors", default=None)


class GenZ(RedfishModel):
    access_key_violations: int | None = None
    end_to_end_crcerrors: int | None = Field(alias="EndToEndCRCErrors", default=None)
    llrrecovery: int | None = Field(alias="LLRRecovery", default=None)
    link_nte: int | None = Field(alias="LinkNTE", default=None)
    marked_ecn: int | None = Field(alias="MarkedECN", default=None)
    non_crctransient_errors: int | None = Field(alias="NonCRCTransientErrors", default=None)
    packet_crcerrors: int | None = Field(alias="PacketCRCErrors", default=None)
    packet_deadline_discards: int | None = None
    rxstomped_ecrc: int | None = Field(alias="RXStompedECRC", default=None)
    received_ecn: int | None = Field(alias="ReceivedECN", default=None)
    txstomped_ecrc: int | None = Field(alias="TXStompedECRC", default=None)


class Networking(RedfishModel):
    rdmaprotection_errors: int | None = Field(alias="RDMAProtectionErrors", default=None)
    rdmaprotocol_errors: int | None = Field(alias="RDMAProtocolErrors", default=None)
    rdmarxbytes: int | None = Field(alias="RDMARXBytes", default=None)
    rdmarxrequests: int | None = Field(alias="RDMARXRequests", default=None)
    rdmatxbytes: int | None = Field(alias="RDMATXBytes", default=None)
    rdmatxread_requests: int | None = Field(alias="RDMATXReadRequests", default=None)
    rdmatxrequests: int | None = Field(alias="RDMATXRequests", default=None)
    rdmatxsend_requests: int | None = Field(alias="RDMATXSendRequests", default=None)
    rdmatxwrite_requests: int | None = Field(alias="RDMATXWriteRequests", default=None)
    rxbroadcast_frames: int | None = Field(alias="RXBroadcastFrames", default=None)
    rxdiscards: int | None = Field(alias="RXDiscards", default=None)
    rxfcserrors: int | None = Field(alias="RXFCSErrors", default=None)
    rxfalse_carrier_errors: int | None = Field(alias="RXFalseCarrierErrors", default=None)
    rxframe_alignment_errors: int | None = Field(alias="RXFrameAlignmentErrors", default=None)
    rxframes: int | None = Field(alias="RXFrames", default=None)
    rxmulticast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rxoversize_frames: int | None = Field(alias="RXOversizeFrames", default=None)
    rxpfcframes: int | None = Field(alias="RXPFCFrames", default=None)
    rxpause_xoffframes: int | None = Field(alias="RXPauseXOFFFrames", default=None)
    rxpause_xonframes: int | None = Field(alias="RXPauseXONFrames", default=None)
    rxundersize_frames: int | None = Field(alias="RXUndersizeFrames", default=None)
    rxunicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    txbroadcast_frames: int | None = Field(alias="TXBroadcastFrames", default=None)
    txdiscards: int | None = Field(alias="TXDiscards", default=None)
    txexcessive_collisions: int | None = Field(alias="TXExcessiveCollisions", default=None)
    txframes: int | None = Field(alias="TXFrames", default=None)
    txlate_collisions: int | None = Field(alias="TXLateCollisions", default=None)
    txmulticast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    txmultiple_collisions: int | None = Field(alias="TXMultipleCollisions", default=None)
    txpfcframes: int | None = Field(alias="TXPFCFrames", default=None)
    txpause_xoffframes: int | None = Field(alias="TXPauseXOFFFrames", default=None)
    txpause_xonframes: int | None = Field(alias="TXPauseXONFrames", default=None)
    txsingle_collisions: int | None = Field(alias="TXSingleCollisions", default=None)
    txunicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class PortMetrics(RedfishResource):
    actions: Actions | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    description: str | None = None
    fibre_channel: FibreChannel | None = None
    gen_z: GenZ | None = None
    networking: Networking | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(alias="PCIeErrors", default=None)
    rxbytes: int | None = Field(alias="RXBytes", default=None)
    rxerrors: int | None = Field(alias="RXErrors", default=None)
    sas: list[Sas] | None = Field(alias="SAS", default=None)
    txbytes: int | None = Field(alias="TXBytes", default=None)
    txerrors: int | None = Field(alias="TXErrors", default=None)
    transceivers: list[Transceiver] | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Sas(RedfishModel):
    invalid_dword_count: int | None = None
    loss_of_dword_synchronization_count: int | None = None
    phy_reset_problem_count: int | None = None
    running_disparity_error_count: int | None = None


class Transceiver(RedfishModel):
    rxinput_power_milli_watts: float | None = Field(alias="RXInputPowerMilliWatts", default=None)
    supply_voltage: float | None = None
    txbias_current_milli_amps: float | None = Field(alias="TXBiasCurrentMilliAmps", default=None)
    txoutput_power_milli_watts: float | None = Field(alias="TXOutputPowerMilliWatts", default=None)
    wavelength_nanometers: str | None = None
