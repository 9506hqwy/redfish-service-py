from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.address_pool import AddressPool, AddressPoolOnCreate
from ..model.address_pool_collection import AddressPoolCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection

router = APIRouter()


@router.get("/redfish/v1/Fabrics/{fabric_id}/AddressPools", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/AddressPools", response_model_exclude_none=True)
async def get1(fabric_id: str, request: Request, response: Response) -> AddressPoolCollection:
    s: Service = get_service(AddressPoolCollection, request)
    b: dict[str, Any] = {"fabric_id": fabric_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(AddressPoolCollection, s.get(**b))


@router.post("/redfish/v1/Fabrics/{fabric_id}/AddressPools", response_model_exclude_none=True)
@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/AddressPools/Members", response_model_exclude_none=True
)
@authenticate
async def post1(
    fabric_id: str, request: Request, response: Response, body: AddressPoolOnCreate
) -> AddressPool:
    s: ServiceCollection = get_service_collection(AddressPoolCollection, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(AddressPool, s.post(**b))
