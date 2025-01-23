from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.power_distribution import PowerDistribution, PowerDistributionOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}", response_model_exclude_none=True
)
async def get1(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/FloorPDUs/{power_distribution_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}",
    response_model_exclude_none=True,
)
async def get5(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/Switchgear/{power_distribution_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}",
    response_model_exclude_none=True,
)
async def get6(
    power_distribution_id: str, request: Request, response: Response
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(PowerDistribution, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    power_distribution_id: str,
    request: Request,
    response: Response,
    body: PowerDistributionOnUpdate,
) -> PowerDistribution:
    s: Service = get_service(PowerDistribution, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(PowerDistribution, s.patch(**b))
