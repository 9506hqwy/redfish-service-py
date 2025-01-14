from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#PortMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    backpressure_average_percentage: int | None = None


class FibreChannel(RedfishModel):
    correctable_fec_errors: int | None = Field(
        serialization_alias="CorrectableFECErrors", default=None
    )
    invalid_crcs: int | None = Field(serialization_alias="InvalidCRCs", default=None)
    invalid_tx_words: int | None = Field(serialization_alias="InvalidTXWords", default=None)
    link_failures: int | None = None
    losses_of_signal: int | None = None
    losses_of_sync: int | None = None
    rxbb_credit_zero: int | None = Field(serialization_alias="RXBBCreditZero", default=None)
    rx_exchanges: int | None = Field(serialization_alias="RXExchanges", default=None)
    rx_sequences: int | None = Field(serialization_alias="RXSequences", default=None)
    txbb_credit_zero: int | None = Field(serialization_alias="TXBBCreditZero", default=None)
    txbb_credit_zero_duration_milliseconds: int | None = Field(
        serialization_alias="TXBBCreditZeroDurationMilliseconds", default=None
    )
    txbb_credits: int | None = Field(serialization_alias="TXBBCredits", default=None)
    tx_exchanges: int | None = Field(serialization_alias="TXExchanges", default=None)
    tx_sequences: int | None = Field(serialization_alias="TXSequences", default=None)
    uncorrectable_fec_errors: int | None = Field(
        serialization_alias="UncorrectableFECErrors", default=None
    )


class GenZ(RedfishModel):
    access_key_violations: int | None = None
    end_to_end_crc_errors: int | None = Field(
        serialization_alias="EndToEndCRCErrors", default=None
    )
    llr_recovery: int | None = Field(serialization_alias="LLRRecovery", default=None)
    link_nte: int | None = Field(serialization_alias="LinkNTE", default=None)
    marked_ecn: int | None = Field(serialization_alias="MarkedECN", default=None)
    non_crc_transient_errors: int | None = Field(
        serialization_alias="NonCRCTransientErrors", default=None
    )
    packet_crc_errors: int | None = Field(serialization_alias="PacketCRCErrors", default=None)
    packet_deadline_discards: int | None = None
    rx_stomped_ecrc: int | None = Field(serialization_alias="RXStompedECRC", default=None)
    received_ecn: int | None = Field(serialization_alias="ReceivedECN", default=None)
    tx_stomped_ecrc: int | None = Field(serialization_alias="TXStompedECRC", default=None)


class Networking(RedfishModel):
    rdma_protection_errors: int | None = Field(
        serialization_alias="RDMAProtectionErrors", default=None
    )
    rdma_protocol_errors: int | None = Field(
        serialization_alias="RDMAProtocolErrors", default=None
    )
    rdmarx_bytes: int | None = Field(serialization_alias="RDMARXBytes", default=None)
    rdmarx_requests: int | None = Field(serialization_alias="RDMARXRequests", default=None)
    rdmatx_bytes: int | None = Field(serialization_alias="RDMATXBytes", default=None)
    rdmatx_read_requests: int | None = Field(
        serialization_alias="RDMATXReadRequests", default=None
    )
    rdmatx_requests: int | None = Field(serialization_alias="RDMATXRequests", default=None)
    rdmatx_send_requests: int | None = Field(
        serialization_alias="RDMATXSendRequests", default=None
    )
    rdmatx_write_requests: int | None = Field(
        serialization_alias="RDMATXWriteRequests", default=None
    )
    rx_broadcast_frames: int | None = Field(serialization_alias="RXBroadcastFrames", default=None)
    rx_discards: int | None = Field(serialization_alias="RXDiscards", default=None)
    rxfcs_errors: int | None = Field(serialization_alias="RXFCSErrors", default=None)
    rx_false_carrier_errors: int | None = Field(
        serialization_alias="RXFalseCarrierErrors", default=None
    )
    rx_frame_alignment_errors: int | None = Field(
        serialization_alias="RXFrameAlignmentErrors", default=None
    )
    rx_frames: int | None = Field(serialization_alias="RXFrames", default=None)
    rx_multicast_frames: int | None = Field(serialization_alias="RXMulticastFrames", default=None)
    rx_oversize_frames: int | None = Field(serialization_alias="RXOversizeFrames", default=None)
    rxpfc_frames: int | None = Field(serialization_alias="RXPFCFrames", default=None)
    rx_pause_xoff_frames: int | None = Field(serialization_alias="RXPauseXOFFFrames", default=None)
    rx_pause_xon_frames: int | None = Field(serialization_alias="RXPauseXONFrames", default=None)
    rx_undersize_frames: int | None = Field(serialization_alias="RXUndersizeFrames", default=None)
    rx_unicast_frames: int | None = Field(serialization_alias="RXUnicastFrames", default=None)
    tx_broadcast_frames: int | None = Field(serialization_alias="TXBroadcastFrames", default=None)
    tx_discards: int | None = Field(serialization_alias="TXDiscards", default=None)
    tx_excessive_collisions: int | None = Field(
        serialization_alias="TXExcessiveCollisions", default=None
    )
    tx_frames: int | None = Field(serialization_alias="TXFrames", default=None)
    tx_late_collisions: int | None = Field(serialization_alias="TXLateCollisions", default=None)
    tx_multicast_frames: int | None = Field(serialization_alias="TXMulticastFrames", default=None)
    tx_multiple_collisions: int | None = Field(
        serialization_alias="TXMultipleCollisions", default=None
    )
    txpfc_frames: int | None = Field(serialization_alias="TXPFCFrames", default=None)
    tx_pause_xoff_frames: int | None = Field(serialization_alias="TXPauseXOFFFrames", default=None)
    tx_pause_xon_frames: int | None = Field(serialization_alias="TXPauseXONFrames", default=None)
    tx_single_collisions: int | None = Field(
        serialization_alias="TXSingleCollisions", default=None
    )
    tx_unicast_frames: int | None = Field(serialization_alias="TXUnicastFrames", default=None)


class PortMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PortMetrics.v1_7_0.PortMetrics"
    )
    actions: Actions | None = None
    cxl: Cxl | None = Field(serialization_alias="CXL", default=None)
    description: str | None = None
    fibre_channel: FibreChannel | None = None
    gen_z: GenZ | None = None
    id: str
    name: str
    networking: Networking | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(serialization_alias="PCIeErrors", default=None)
    rx_bytes: int | None = Field(serialization_alias="RXBytes", default=None)
    rx_errors: int | None = Field(serialization_alias="RXErrors", default=None)
    sas: list[Sas] | None = Field(serialization_alias="SAS", default=None)
    tx_bytes: int | None = Field(serialization_alias="TXBytes", default=None)
    tx_errors: int | None = Field(serialization_alias="TXErrors", default=None)
    transceivers: list[Transceiver] | None = None


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Sas(RedfishModel):
    invalid_dword_count: int | None = None
    loss_of_dword_synchronization_count: int | None = None
    phy_reset_problem_count: int | None = None
    running_disparity_error_count: int | None = None


class Transceiver(RedfishModel):
    rx_input_power_milli_watts: float | None = Field(
        serialization_alias="RXInputPowerMilliWatts", default=None
    )
    supply_voltage: float | None = None
    tx_bias_current_milli_amps: float | None = Field(
        serialization_alias="TXBiasCurrentMilliAmps", default=None
    )
    tx_output_power_milli_watts: float | None = Field(
        serialization_alias="TXOutputPowerMilliWatts", default=None
    )
    wavelength_nanometers: str | None = None
