from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum


class PrivilegeType(StrEnum):
    LOGIN = "Login"
    CONFIGURE_MANAGER = "ConfigureManager"
    CONFIGURE_USERS = "ConfigureUsers"
    CONFIGURE_SELF = "ConfigureSelf"
    CONFIGURE_COMPONENTS = "ConfigureComponents"
    NO_AUTH = "NoAuth"
    CONFIGURE_COMPOSITION_INFRASTRUCTURE = "ConfigureCompositionInfrastructure"
    ADMINISTRATE_SYSTEMS = "AdministrateSystems"
    OPERATE_SYSTEMS = "OperateSystems"
    ADMINISTRATE_STORAGE = "AdministrateStorage"
    OPERATE_STORAGE_BACKUP = "OperateStorageBackup"
