from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum


class ReleaseStatus(StrEnum):
    STANDARD = "Standard"
    INFORMATIONAL = "Informational"
    WORK_IN_PROGRESS = "WorkInProgress"
    IN_DEVELOPMENT = "InDevelopment"
