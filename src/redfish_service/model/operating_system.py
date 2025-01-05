from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .container_image import ImageTypes
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ContainerEngine(RedfishModel):
    management_ur_is: list[str] | None = Field(alias="ManagementURIs", default=None)
    supported_image_types: list[ImageTypes] | None = None
    type: ContainerEngineTypes | None = None
    version: str | None = None


class ContainerEngineTypes(StrEnum):
    DOCKER = "Docker"
    CONTAINERD = "containerd"
    CRIO = "CRIO"


class Kernel(RedfishModel):
    machine: str | None = None
    name: str | None = None
    release: str | None = None
    version: str | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None


class OperatingSystem(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#OperatingSystem.v1_0_2.OperatingSystem")
    actions: Actions | None = None
    applications: IdRef | None = None
    container_engines: list[ContainerEngine] | None = None
    container_images: IdRef | None = None
    containers: IdRef | None = None
    description: str | None = None
    id: str
    kernel: Kernel | None = None
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    type: OperatingSystemTypes | None = None
    uptime_seconds: int | None = None
    virtual_machine_engines: list[VirtualMachineEngine] | None = None


class OperatingSystemTypes(StrEnum):
    LINUX = "Linux"
    WINDOWS = "Windows"
    SOLARIS = "Solaris"
    HPUX = "HPUX"
    AIX = "AIX"
    BSD = "BSD"
    MACOS = "macOS"
    IB_MI = "IBMi"
    HYPERVISOR = "Hypervisor"


class VirtualMachineEngine(RedfishModel):
    management_ur_is: list[str] | None = Field(alias="ManagementURIs", default=None)
    supported_image_types: list[VirtualMachineImageTypes] | None = None
    type: VirtualMachineEngineTypes | None = None
    version: str | None = None


class VirtualMachineEngineTypes(StrEnum):
    V_MWARE_ESX = "VMwareESX"
    HYPER_V = "HyperV"
    XEN = "Xen"
    KVM = "KVM"
    QEMU = "QEMU"
    VIRTUAL_BOX = "VirtualBox"
    POWER_VM = "PowerVM"


class VirtualMachineImageTypes(StrEnum):
    RAW = "Raw"
    OVF = "OVF"
    OVA = "OVA"
    VHD = "VHD"
    VMDK = "VMDK"
    VDI = "VDI"
    QCOW = "QCOW"
    QCOW2 = "QCOW2"
