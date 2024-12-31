from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum


class LogicalContext(StrEnum):
    CAPACITY = "Capacity"
    ENVIRONMENT = "Environment"
    NETWORK = "Network"
    PERFORMANCE = "Performance"
    SECURITY = "Security"
    STORAGE = "Storage"


class PhysicalContext(StrEnum):
    ROOM = "Room"
    INTAKE = "Intake"
    EXHAUST = "Exhaust"
    LIQUID_INLET = "LiquidInlet"
    LIQUID_OUTLET = "LiquidOutlet"
    FRONT = "Front"
    BACK = "Back"
    UPPER = "Upper"
    LOWER = "Lower"
    CPU = "CPU"
    CPUSUBSYSTEM = "CPUSubsystem"
    GPU = "GPU"
    GPUSUBSYSTEM = "GPUSubsystem"
    FPGA = "FPGA"
    ACCELERATOR = "Accelerator"
    ASIC = "ASIC"
    BACKPLANE = "Backplane"
    SYSTEM_BOARD = "SystemBoard"
    POWER_SUPPLY = "PowerSupply"
    POWER_SUBSYSTEM = "PowerSubsystem"
    VOLTAGE_REGULATOR = "VoltageRegulator"
    RECTIFIER = "Rectifier"
    STORAGE_DEVICE = "StorageDevice"
    STORAGE_SUBSYSTEM = "StorageSubsystem"
    NETWORKING_DEVICE = "NetworkingDevice"
    EXPANSION_SUBSYSTEM = "ExpansionSubsystem"
    COMPUTE_BAY = "ComputeBay"
    STORAGE_BAY = "StorageBay"
    NETWORK_BAY = "NetworkBay"
    EXPANSION_BAY = "ExpansionBay"
    POWER_SUPPLY_BAY = "PowerSupplyBay"
    MEMORY = "Memory"
    MEMORY_SUBSYSTEM = "MemorySubsystem"
    CHASSIS = "Chassis"
    FAN = "Fan"
    COOLING_SUBSYSTEM = "CoolingSubsystem"
    MOTOR = "Motor"
    TRANSFORMER = "Transformer"
    ACUTILITY_INPUT = "ACUtilityInput"
    ACSTATIC_BYPASS_INPUT = "ACStaticBypassInput"
    ACMAINTENANCE_BYPASS_INPUT = "ACMaintenanceBypassInput"
    DCBUS = "DCBus"
    ACOUTPUT = "ACOutput"
    ACINPUT = "ACInput"
    POWER_OUTLET = "PowerOutlet"
    TRUSTED_MODULE = "TrustedModule"
    BOARD = "Board"
    TRANSCEIVER = "Transceiver"
    BATTERY = "Battery"
    PUMP = "Pump"
    FILTER = "Filter"
    RESERVOIR = "Reservoir"
    SWITCH = "Switch"
    MANAGER = "Manager"


class PhysicalSubContext(StrEnum):
    INPUT = "Input"
    OUTPUT = "Output"
