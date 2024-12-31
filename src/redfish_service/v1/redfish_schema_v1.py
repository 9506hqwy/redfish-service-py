from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum

from .base import RedfishResource


class ActionResponse(RedfishResource):
    pass


class EnumDeprecated(RedfishResource):
    pass


class EnumDescriptions(RedfishResource):
    pass


class EnumLongDescriptions(RedfishResource):
    pass


class EnumTranslations(RedfishResource):
    pass


class EnumVersionAdded(RedfishResource):
    pass


class EnumVersionDeprecated(RedfishResource):
    pass


class ReleaseStatus(StrEnum):
    STANDARD = "Standard"
    INFORMATIONAL = "Informational"
    WORK_IN_PROGRESS = "WorkInProgress"
    IN_DEVELOPMENT = "InDevelopment"
