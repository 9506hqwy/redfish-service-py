from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.sensor_collection import SensorCollection
from ..service import Service, find_service

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Sensors", response_model_exclude_none=True)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@authenticate
async def get5(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@authenticate
async def get6(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = find_service(SensorCollection)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(SensorCollection, s.get(**b))
