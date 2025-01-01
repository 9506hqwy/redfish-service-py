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
    correctable_fecerrors: str | None = Field(alias="CorrectableFECErrors", default=None)
    invalid_crcs: str | None = Field(alias="InvalidCRCs", default=None)
    invalid_txwords: str | None = Field(alias="InvalidTXWords", default=None)
    link_failures: str | None = None
    losses_of_signal: str | None = None
    losses_of_sync: str | None = None
    rxbbcredit_zero: str | None = Field(alias="RXBBCreditZero", default=None)
    rxexchanges: str | None = Field(alias="RXExchanges", default=None)
    rxsequences: str | None = Field(alias="RXSequences", default=None)
    txbbcredit_zero: str | None = Field(alias="TXBBCreditZero", default=None)
    txbbcredit_zero_duration_milliseconds: str | None = Field(
        alias="TXBBCreditZeroDurationMilliseconds", default=None
    )
    txbbcredits: str | None = Field(alias="TXBBCredits", default=None)
    txexchanges: str | None = Field(alias="TXExchanges", default=None)
    txsequences: str | None = Field(alias="TXSequences", default=None)
    uncorrectable_fecerrors: str | None = Field(alias="UncorrectableFECErrors", default=None)


class GenZ(RedfishModel):
    access_key_violations: str | None = None
    end_to_end_crcerrors: str | None = Field(alias="EndToEndCRCErrors", default=None)
    llrrecovery: str | None = Field(alias="LLRRecovery", default=None)
    link_nte: str | None = Field(alias="LinkNTE", default=None)
    marked_ecn: str | None = Field(alias="MarkedECN", default=None)
    non_crctransient_errors: str | None = Field(alias="NonCRCTransientErrors", default=None)
    packet_crcerrors: str | None = Field(alias="PacketCRCErrors", default=None)
    packet_deadline_discards: str | None = None
    rxstomped_ecrc: str | None = Field(alias="RXStompedECRC", default=None)
    received_ecn: str | None = Field(alias="ReceivedECN", default=None)
    txstomped_ecrc: str | None = Field(alias="TXStompedECRC", default=None)


class Networking(RedfishModel):
    rdmaprotection_errors: str | None = Field(alias="RDMAProtectionErrors", default=None)
    rdmaprotocol_errors: str | None = Field(alias="RDMAProtocolErrors", default=None)
    rdmarxbytes: str | None = Field(alias="RDMARXBytes", default=None)
    rdmarxrequests: str | None = Field(alias="RDMARXRequests", default=None)
    rdmatxbytes: str | None = Field(alias="RDMATXBytes", default=None)
    rdmatxread_requests: str | None = Field(alias="RDMATXReadRequests", default=None)
    rdmatxrequests: str | None = Field(alias="RDMATXRequests", default=None)
    rdmatxsend_requests: str | None = Field(alias="RDMATXSendRequests", default=None)
    rdmatxwrite_requests: str | None = Field(alias="RDMATXWriteRequests", default=None)
    rxbroadcast_frames: str | None = Field(alias="RXBroadcastFrames", default=None)
    rxdiscards: str | None = Field(alias="RXDiscards", default=None)
    rxfcserrors: str | None = Field(alias="RXFCSErrors", default=None)
    rxfalse_carrier_errors: str | None = Field(alias="RXFalseCarrierErrors", default=None)
    rxframe_alignment_errors: str | None = Field(alias="RXFrameAlignmentErrors", default=None)
    rxframes: str | None = Field(alias="RXFrames", default=None)
    rxmulticast_frames: str | None = Field(alias="RXMulticastFrames", default=None)
    rxoversize_frames: str | None = Field(alias="RXOversizeFrames", default=None)
    rxpfcframes: str | None = Field(alias="RXPFCFrames", default=None)
    rxpause_xoffframes: str | None = Field(alias="RXPauseXOFFFrames", default=None)
    rxpause_xonframes: str | None = Field(alias="RXPauseXONFrames", default=None)
    rxundersize_frames: str | None = Field(alias="RXUndersizeFrames", default=None)
    rxunicast_frames: str | None = Field(alias="RXUnicastFrames", default=None)
    txbroadcast_frames: str | None = Field(alias="TXBroadcastFrames", default=None)
    txdiscards: str | None = Field(alias="TXDiscards", default=None)
    txexcessive_collisions: str | None = Field(alias="TXExcessiveCollisions", default=None)
    txframes: str | None = Field(alias="TXFrames", default=None)
    txlate_collisions: str | None = Field(alias="TXLateCollisions", default=None)
    txmulticast_frames: str | None = Field(alias="TXMulticastFrames", default=None)
    txmultiple_collisions: str | None = Field(alias="TXMultipleCollisions", default=None)
    txpfcframes: str | None = Field(alias="TXPFCFrames", default=None)
    txpause_xoffframes: str | None = Field(alias="TXPauseXOFFFrames", default=None)
    txpause_xonframes: str | None = Field(alias="TXPauseXONFrames", default=None)
    txsingle_collisions: str | None = Field(alias="TXSingleCollisions", default=None)
    txunicast_frames: str | None = Field(alias="TXUnicastFrames", default=None)


class PortMetrics(RedfishResource):
    actions: Actions | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    description: str | None = None
    fibre_channel: FibreChannel | None = None
    gen_z: GenZ | None = None
    networking: Networking | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(alias="PCIeErrors", default=None)
    rxbytes: str | None = Field(alias="RXBytes", default=None)
    rxerrors: str | None = Field(alias="RXErrors", default=None)
    sas: list[Sas] | None = Field(alias="SAS", default=None)
    txbytes: str | None = Field(alias="TXBytes", default=None)
    txerrors: str | None = Field(alias="TXErrors", default=None)
    transceivers: list[Transceiver] | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Sas(RedfishModel):
    invalid_dword_count: str | None = None
    loss_of_dword_synchronization_count: str | None = None
    phy_reset_problem_count: str | None = None
    running_disparity_error_count: str | None = None


class Transceiver(RedfishModel):
    rxinput_power_milli_watts: str | None = Field(alias="RXInputPowerMilliWatts", default=None)
    supply_voltage: str | None = None
    txbias_current_milli_amps: str | None = Field(alias="TXBiasCurrentMilliAmps", default=None)
    txoutput_power_milli_watts: str | None = Field(alias="TXOutputPowerMilliWatts", default=None)
    wavelength_nanometers: str | None = None
