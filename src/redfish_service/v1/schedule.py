from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum

from . import RedfishModel


class DayOfWeek(StrEnum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    EVERY = "Every"


class MonthOfYear(StrEnum):
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"
    EVERY = "Every"


class Schedule(RedfishModel):
    enabled_days_of_month: list[int] | None = None
    enabled_days_of_week: list[DayOfWeek] | None = None
    enabled_intervals: list[str] | None = None
    enabled_months_of_year: list[MonthOfYear] | None = None
    initial_start_time: str | None = None
    lifetime: str | None = None
    max_occurrences: int | None = None
    name: str | None = None
    recurrence_interval: str | None = None
