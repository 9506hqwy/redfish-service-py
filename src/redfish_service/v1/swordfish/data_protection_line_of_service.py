from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Location
from ..schedule import Schedule


class Actions(RedfishModel):
    create_replicas: CreateReplicas | None = Field(
        alias="#DataProtectionLineOfService.CreateReplicas", default=None
    )
    oem: dict[str, Any] | None = None


class CreateReplicas(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class DataProtectionLineOfService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    is_isolated: str | None = None
    min_lifetime: str | None = None
    oem: dict[str, Any] | None = None
    recovery_geographic_objective: str | None = None
    recovery_point_objective_time: str | None = None
    recovery_time_objective: str | None = None
    replica_access_location: Location | None = None
    replica_class_of_service: IdRef | None = None
    replica_type: str | None = None
    schedule: Schedule | None = None
