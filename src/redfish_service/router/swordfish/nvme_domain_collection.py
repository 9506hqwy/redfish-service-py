from typing import Any, cast

from fastapi import APIRouter

from ...authenticate import authenticate
from ...model.swordfish.nvme_domain_collection import NvmeDomainCollection
from ...service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
@authenticate
async def get1() -> NvmeDomainCollection:
    s: Service = find_service(NvmeDomainCollection)
    b: dict[str, Any] = {}
    return cast(NvmeDomainCollection, s.get(**b))
