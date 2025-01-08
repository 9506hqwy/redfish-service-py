from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_domain import NvmeDomain, NvmeDomainOnCreate
from ...model.swordfish.nvme_domain_collection import NvmeDomainCollection
from ...service import Service, ServiceCollection, find_service, find_service_collection

router = APIRouter()


@router.get("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
@router.head("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
async def get1(request: Request, response: Response) -> NvmeDomainCollection:
    s: Service = find_service(NvmeDomainCollection)
    b: dict[str, Any] = {"request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(NvmeDomainCollection, s.get(**b))


@router.post("/redfish/v1/NVMeDomains", response_model_exclude_none=True)
@router.post("/redfish/v1/NVMeDomains/Members", response_model_exclude_none=True)
@authenticate
async def post1(request: Request, response: Response, body: NvmeDomainOnCreate) -> NvmeDomain:
    s: ServiceCollection = find_service_collection(NvmeDomainCollection)
    b: dict[str, Any] = {"request": request, "response": response, "body": body}

    response.headers["OData-Version"] = "4.0"

    return cast(NvmeDomain, s.post(**b))
