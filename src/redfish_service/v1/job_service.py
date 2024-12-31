from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class JobService(RedfishResource):
    actions: Actions | None = None
    date_time: str | None = None
    description: str | None = None
    jobs: IdRef | None = None
    log: IdRef | None = None
    oem: dict[str, Any] | None = None
    service_capabilities: JobServiceCapabilities | None = None
    service_enabled: str | None = None
    status: Status | None = None


class JobServiceCapabilities(RedfishModel):
    max_jobs: str | None = None
    max_steps: str | None = None
    scheduling: str | None = None


class OemActions(RedfishModel):
    pass
