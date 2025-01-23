from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.sensor_collection import SensorCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/Sensors", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/Sensors", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
async def get5(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/Sensors",
    response_model_exclude_none=True,
)
async def get6(
    power_distribution_id: str, request: Request, response: Response
) -> SensorCollection:
    s: Service = get_service(SensorCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(SensorCollection, s.get(**b))
    set_link_header(m, response)
    return m
