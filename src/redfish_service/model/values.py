from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum


class AccountTypes(StrEnum):
    REDFISH = "Redfish"
    SNMP = "SNMP"
    OEM = "OEM"
    HOST_CONSOLE = "HostConsole"
    MANAGER_CONSOLE = "ManagerConsole"
    IPMI = "IPMI"
    KVMIP = "KVMIP"
    VIRTUAL_MEDIA = "VirtualMedia"
    WEB_UI = "WebUI"
