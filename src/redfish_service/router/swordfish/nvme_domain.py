from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_domain import NvmeDomain
from ...service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
@authenticate
async def get1(nvme_domain_id: str, request: Request, response: Response) -> NvmeDomain:
    s: Service = find_service(NvmeDomain)
    b: dict[str, Any] = {
        "nvme_domain_id": nvme_domain_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NvmeDomain, s.get(**b))
