from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef


class HostedStorageServices(RedfishResource):
    description: str | None = None
    members: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
