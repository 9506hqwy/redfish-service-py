from __future__ import annotations  # PEP563 Forward References

from .base import RedfishResource


class Schedule(RedfishResource):
    enabled_days_of_month: list[str] | None = None
    enabled_days_of_week: list[str] | None = None
    enabled_intervals: list[str] | None = None
    enabled_months_of_year: list[str] | None = None
    initial_start_time: str | None = None
    lifetime: str | None = None
    max_occurrences: str | None = None
    recurrence_interval: str | None = None
