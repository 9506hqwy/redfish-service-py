from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum

from .base import (
    RedfishModel,
)


class ActionResponse(RedfishModel):
    pass


class EnumDeprecated(RedfishModel):
    pass


class EnumDescriptions(RedfishModel):
    pass


class EnumLongDescriptions(RedfishModel):
    pass


class EnumTranslations(RedfishModel):
    pass


class EnumVersionAdded(RedfishModel):
    pass


class EnumVersionDeprecated(RedfishModel):
    pass


class ReleaseStatus(StrEnum):
    STANDARD = "Standard"
    INFORMATIONAL = "Informational"
    WORK_IN_PROGRESS = "WorkInProgress"
    IN_DEVELOPMENT = "InDevelopment"
