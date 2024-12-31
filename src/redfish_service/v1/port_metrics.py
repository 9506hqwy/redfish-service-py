from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    backpressure_average_percentage: int | None = None


class FibreChannel(RedfishModel):
    correctable_fecerrors: str | None = None
    invalid_crcs: str | None = None
    invalid_txwords: str | None = None
    link_failures: str | None = None
    losses_of_signal: str | None = None
    losses_of_sync: str | None = None
    rxbbcredit_zero: str | None = None
    rxexchanges: str | None = None
    rxsequences: str | None = None
    txbbcredit_zero: str | None = None
    txbbcredit_zero_duration_milliseconds: str | None = None
    txbbcredits: str | None = None
    txexchanges: str | None = None
    txsequences: str | None = None
    uncorrectable_fecerrors: str | None = None


class GenZ(RedfishModel):
    access_key_violations: str | None = None
    end_to_end_crcerrors: str | None = None
    llrrecovery: str | None = None
    link_nte: str | None = None
    marked_ecn: str | None = None
    non_crctransient_errors: str | None = None
    packet_crcerrors: str | None = None
    packet_deadline_discards: str | None = None
    rxstomped_ecrc: str | None = None
    received_ecn: str | None = None
    txstomped_ecrc: str | None = None


class Networking(RedfishModel):
    rdmaprotection_errors: str | None = None
    rdmaprotocol_errors: str | None = None
    rdmarxbytes: str | None = None
    rdmarxrequests: str | None = None
    rdmatxbytes: str | None = None
    rdmatxread_requests: str | None = None
    rdmatxrequests: str | None = None
    rdmatxsend_requests: str | None = None
    rdmatxwrite_requests: str | None = None
    rxbroadcast_frames: str | None = None
    rxdiscards: str | None = None
    rxfcserrors: str | None = None
    rxfalse_carrier_errors: str | None = None
    rxframe_alignment_errors: str | None = None
    rxframes: str | None = None
    rxmulticast_frames: str | None = None
    rxoversize_frames: str | None = None
    rxpfcframes: str | None = None
    rxpause_xoffframes: str | None = None
    rxpause_xonframes: str | None = None
    rxundersize_frames: str | None = None
    rxunicast_frames: str | None = None
    txbroadcast_frames: str | None = None
    txdiscards: str | None = None
    txexcessive_collisions: str | None = None
    txframes: str | None = None
    txlate_collisions: str | None = None
    txmulticast_frames: str | None = None
    txmultiple_collisions: str | None = None
    txpfcframes: str | None = None
    txpause_xoffframes: str | None = None
    txpause_xonframes: str | None = None
    txsingle_collisions: str | None = None
    txunicast_frames: str | None = None


class PortMetrics(RedfishResource):
    actions: Actions | None = None
    cxl: Cxl | None = None
    description: str | None = None
    fibre_channel: FibreChannel | None = None
    gen_z: GenZ | None = None
    networking: Networking | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = None
    rxbytes: str | None = None
    rxerrors: str | None = None
    sas: list[Sas] | None = None
    txbytes: str | None = None
    txerrors: str | None = None
    transceivers: list[Transceiver] | None = None


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None


class Sas(RedfishModel):
    invalid_dword_count: str | None = None
    loss_of_dword_synchronization_count: str | None = None
    phy_reset_problem_count: str | None = None
    running_disparity_error_count: str | None = None


class Transceiver(RedfishModel):
    rxinput_power_milli_watts: str | None = None
    supply_voltage: str | None = None
    txbias_current_milli_amps: str | None = None
    txoutput_power_milli_watts: str | None = None
    wavelength_nanometers: str | None = None
