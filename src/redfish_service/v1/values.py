from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum


class EventType(StrEnum):
    STATUS_CHANGE = "StatusChange"
    RESOURCE_UPDATED = "ResourceUpdated"
    RESOURCE_ADDED = "ResourceAdded"
    RESOURCE_REMOVED = "ResourceRemoved"
    ALERT = "Alert"
    METRIC_REPORT = "MetricReport"
    OTHER = "Other"
