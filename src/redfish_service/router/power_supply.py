from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_supply import PowerSupply, PowerSupplyOnUpdate, ResetRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, power_supply_id: str, request: Request, response: Response
) -> PowerSupply:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    return cast(PowerSupply, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: PowerSupplyOnUpdate,
) -> PowerSupply:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerSupply, s.patch(**b))


@router.post(
    "/redfish/v1/Chassis/{chassis_id}/PowerSubsystem/PowerSupplies/{power_supply_id}/Actions/PowerSupply.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset1(
    chassis_id: str, power_supply_id: str, request: Request, response: Response, body: ResetRequest
) -> RedfishError:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, power_supply_id: str, request: Request, response: Response
) -> PowerSupply:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
    }
    return cast(PowerSupply, s.get(**b))


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    power_distribution_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: PowerSupplyOnUpdate,
) -> PowerSupply:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerSupply, s.patch(**b))


@router.post(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/PowerSupplies/{power_supply_id}/Actions/PowerSupply.Reset",
    response_model_exclude_none=True,
)
@authenticate
async def reset2(
    power_distribution_id: str,
    power_supply_id: str,
    request: Request,
    response: Response,
    body: ResetRequest,
) -> RedfishError:
    s: Service = get_service(PowerSupply, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "power_supply_id": power_supply_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "Reset",
    }
    return s.action(**b)
