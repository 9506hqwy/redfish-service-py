from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_domain import NvmeDomain, NvmeDomainOnUpdate
from ...service import Service
from ...util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
@authenticate
async def delete1(nvme_domain_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(NvmeDomain, request)
    b: dict[str, Any] = {
        "nvme_domain_id": nvme_domain_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
async def get1(nvme_domain_id: str, request: Request, response: Response) -> NvmeDomain:
    s: Service = get_service(NvmeDomain, request)
    b: dict[str, Any] = {
        "nvme_domain_id": nvme_domain_id,
        "request": request,
        "response": response,
    }
    m = cast(NvmeDomain, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/NVMeDomains/{nvme_domain_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    nvme_domain_id: str, request: Request, response: Response, body: NvmeDomainOnUpdate
) -> NvmeDomain:
    s: Service = get_service(NvmeDomain, request)
    b: dict[str, Any] = {
        "nvme_domain_id": nvme_domain_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(NvmeDomain, s.patch(**b))
