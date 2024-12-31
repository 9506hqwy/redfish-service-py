from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    data_protection_lo_scapabilities: IdRef | None = None
    data_security_lo_scapabilities: IdRef | None = None
    data_storage_lo_scapabilities: IdRef | None = None
    default_class_of_service: IdRef | None = None
    hosting_system: IdRef | None = None
    ioconnectivity_lo_scapabilities: IdRef | None = None
    ioperformance_lo_scapabilities: IdRef | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass


class SetEncryptionKey(RedfishModel):
    target: str | None = None
    title: str | None = None


class StorageService(RedfishResource):
    actions: Actions | None = None
    classes_of_service: IdRef | None = None
    client_endpoint_groups: IdRef | None = None
    connections: IdRef | None = None
    consistency_groups: IdRef | None = None
    data_protection_lo_scapabilities: IdRef | None = None
    data_security_lo_scapabilities: IdRef | None = None
    data_storage_lo_scapabilities: IdRef | None = None
    default_class_of_service: IdRef | None = None
    description: str | None = None
    drives: IdRef | None = None
    endpoint_groups: IdRef | None = None
    endpoints: IdRef | None = None
    file_systems: IdRef | None = None
    ioconnectivity_lo_scapabilities: IdRef | None = None
    ioperformance_lo_scapabilities: IdRef | None = None
    iostatistics: Iostatistics | None = None
    identifier: Identifier | None = None
    lines_of_service: list[IdRef] | None = None
    links: Links | None = None
    metrics: str | None = None
    oem: dict[str, Any] | None = None
    redundancy: list[IdRef] | None = None
    server_endpoint_groups: IdRef | None = None
    spare_resource_sets: list[IdRef] | None = None
    status: Status | None = None
    storage_groups: IdRef | None = None
    storage_pools: IdRef | None = None
    storage_subsystems: list[IdRef] | None = None
    volumes: IdRef | None = None
