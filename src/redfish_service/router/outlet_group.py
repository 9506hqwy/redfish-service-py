from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outlet_group import OutletGroup
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = find_service(OutletGroup)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OutletGroup, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = find_service(OutletGroup)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OutletGroup, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = find_service(OutletGroup)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OutletGroup, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = find_service(OutletGroup)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(OutletGroup, s.get(**b))
