from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_supply_collection import PowerSupplyCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> PowerSupplyCollection:
    s: Service = find_service(PowerSupplyCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(PowerSupplyCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> PowerSupplyCollection:
    s: Service = find_service(PowerSupplyCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(PowerSupplyCollection, s.get(**b))
