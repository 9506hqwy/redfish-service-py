from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_domain import NvmeDomain, NvmeDomainOnCreate
from ...model.swordfish.nvme_domain_collection import NvmeDomainCollection
from ...service import Service, ServiceCollection
from ...util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
@router.head("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> NvmeDomainCollection:
    s: Service = get_service(NvmeDomainCollection, request)
    b: dict[str, Any] = {"request": request, "response": response}
    m = cast(NvmeDomainCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
@router.post("/redfish/v1/NVMeDomains/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: NvmeDomainOnCreate) -> NvmeDomain:
    s: ServiceCollection = get_service_collection(NvmeDomainCollection, request)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}
    return cast(NvmeDomain, s.post(**b))
