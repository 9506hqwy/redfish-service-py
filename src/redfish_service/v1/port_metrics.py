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
    correctable_fec_errors: int | None = Field(alias="CorrectableFECErrors", default=None)
    invalid_crcs: int | None = Field(alias="InvalidCRCs", default=None)
    invalid_tx_words: int | None = Field(alias="InvalidTXWords", default=None)
    link_failures: int | None = None
    losses_of_signal: int | None = None
    losses_of_sync: int | None = None
    rxbb_credit_zero: int | None = Field(alias="RXBBCreditZero", default=None)
    rx_exchanges: int | None = Field(alias="RXExchanges", default=None)
    rx_sequences: int | None = Field(alias="RXSequences", default=None)
    txbb_credit_zero: int | None = Field(alias="TXBBCreditZero", default=None)
    txbb_credit_zero_duration_milliseconds: int | None = Field(
        alias="TXBBCreditZeroDurationMilliseconds", default=None
    )
    txbb_credits: int | None = Field(alias="TXBBCredits", default=None)
    tx_exchanges: int | None = Field(alias="TXExchanges", default=None)
    tx_sequences: int | None = Field(alias="TXSequences", default=None)
    uncorrectable_fec_errors: int | None = Field(alias="UncorrectableFECErrors", default=None)


class GenZ(RedfishModel):
    access_key_violations: int | None = None
    end_to_end_crc_errors: int | None = Field(alias="EndToEndCRCErrors", default=None)
    llr_recovery: int | None = Field(alias="LLRRecovery", default=None)
    link_nte: int | None = Field(alias="LinkNTE", default=None)
    marked_ecn: int | None = Field(alias="MarkedECN", default=None)
    non_crc_transient_errors: int | None = Field(alias="NonCRCTransientErrors", default=None)
    packet_crc_errors: int | None = Field(alias="PacketCRCErrors", default=None)
    packet_deadline_discards: int | None = None
    rx_stomped_ecrc: int | None = Field(alias="RXStompedECRC", default=None)
    received_ecn: int | None = Field(alias="ReceivedECN", default=None)
    tx_stomped_ecrc: int | None = Field(alias="TXStompedECRC", default=None)


class Networking(RedfishModel):
    rdma_protection_errors: int | None = Field(alias="RDMAProtectionErrors", default=None)
    rdma_protocol_errors: int | None = Field(alias="RDMAProtocolErrors", default=None)
    rdmarx_bytes: int | None = Field(alias="RDMARXBytes", default=None)
    rdmarx_requests: int | None = Field(alias="RDMARXRequests", default=None)
    rdmatx_bytes: int | None = Field(alias="RDMATXBytes", default=None)
    rdmatx_read_requests: int | None = Field(alias="RDMATXReadRequests", default=None)
    rdmatx_requests: int | None = Field(alias="RDMATXRequests", default=None)
    rdmatx_send_requests: int | None = Field(alias="RDMATXSendRequests", default=None)
    rdmatx_write_requests: int | None = Field(alias="RDMATXWriteRequests", default=None)
    rx_broadcast_frames: int | None = Field(alias="RXBroadcastFrames", default=None)
    rx_discards: int | None = Field(alias="RXDiscards", default=None)
    rxfcs_errors: int | None = Field(alias="RXFCSErrors", default=None)
    rx_false_carrier_errors: int | None = Field(alias="RXFalseCarrierErrors", default=None)
    rx_frame_alignment_errors: int | None = Field(alias="RXFrameAlignmentErrors", default=None)
    rx_frames: int | None = Field(alias="RXFrames", default=None)
    rx_multicast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rx_oversize_frames: int | None = Field(alias="RXOversizeFrames", default=None)
    rxpfc_frames: int | None = Field(alias="RXPFCFrames", default=None)
    rx_pause_xoff_frames: int | None = Field(alias="RXPauseXOFFFrames", default=None)
    rx_pause_xon_frames: int | None = Field(alias="RXPauseXONFrames", default=None)
    rx_undersize_frames: int | None = Field(alias="RXUndersizeFrames", default=None)
    rx_unicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    tx_broadcast_frames: int | None = Field(alias="TXBroadcastFrames", default=None)
    tx_discards: int | None = Field(alias="TXDiscards", default=None)
    tx_excessive_collisions: int | None = Field(alias="TXExcessiveCollisions", default=None)
    tx_frames: int | None = Field(alias="TXFrames", default=None)
    tx_late_collisions: int | None = Field(alias="TXLateCollisions", default=None)
    tx_multicast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    tx_multiple_collisions: int | None = Field(alias="TXMultipleCollisions", default=None)
    txpfc_frames: int | None = Field(alias="TXPFCFrames", default=None)
    tx_pause_xoff_frames: int | None = Field(alias="TXPauseXOFFFrames", default=None)
    tx_pause_xon_frames: int | None = Field(alias="TXPauseXONFrames", default=None)
    tx_single_collisions: int | None = Field(alias="TXSingleCollisions", default=None)
    tx_unicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class PortMetrics(RedfishResource):
    actions: Actions | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    description: str | None = None
    fibre_channel: FibreChannel | None = None
    gen_z: GenZ | None = None
    networking: Networking | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(alias="PCIeErrors", default=None)
    rx_bytes: int | None = Field(alias="RXBytes", default=None)
    rx_errors: int | None = Field(alias="RXErrors", default=None)
    sas: list[Sas] | None = Field(alias="SAS", default=None)
    tx_bytes: int | None = Field(alias="TXBytes", default=None)
    tx_errors: int | None = Field(alias="TXErrors", default=None)
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
    rx_input_power_milli_watts: float | None = Field(alias="RXInputPowerMilliWatts", default=None)
    supply_voltage: float | None = None
    tx_bias_current_milli_amps: float | None = Field(alias="TXBiasCurrentMilliAmps", default=None)
    tx_output_power_milli_watts: float | None = Field(
        alias="TXOutputPowerMilliWatts", default=None
    )
    wavelength_nanometers: str | None = None
