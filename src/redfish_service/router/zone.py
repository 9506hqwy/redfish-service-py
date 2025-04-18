from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.redfish_error import RedfishError
from ..model.zone import AddEndpointRequest, RemoveEndpointRequest, Zone, ZoneOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
@authenticate
async def delete1(fabric_id: str, zone_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
async def get1(fabric_id: str, zone_id: str, request: Request, response: Response) -> Zone:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
    }
    m = cast(Zone, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}", response_model_exclude_none=True)
@authenticate
async def patch1(
    fabric_id: str, zone_id: str, request: Request, response: Response, body: ZoneOnUpdate
) -> Zone:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Zone, s.patch(**b))


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}/Actions/Zone.AddEndpoint",
    response_model_exclude_none=True,
)
@authenticate
async def add_endpoint1(
    fabric_id: str, zone_id: str, request: Request, response: Response, body: AddEndpointRequest
) -> RedfishError:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddEndpoint",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/Fabrics/{fabric_id}/Zones/{zone_id}/Actions/Zone.RemoveEndpoint",
    response_model_exclude_none=True,
)
@authenticate
async def remove_endpoint1(
    fabric_id: str, zone_id: str, request: Request, response: Response, body: RemoveEndpointRequest
) -> RedfishError:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "fabric_id": fabric_id,
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveEndpoint",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
@authenticate
async def delete2(zone_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {"zone_id": zone_id, "request": request, "response": response}
    return s.delete(**b)


@router.get(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
async def get2(zone_id: str, request: Request, response: Response) -> Zone:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {"zone_id": zone_id, "request": request, "response": response}
    m = cast(Zone, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}", response_model_exclude_none=True
)
@authenticate
async def patch2(zone_id: str, request: Request, response: Response, body: ZoneOnUpdate) -> Zone:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Zone, s.patch(**b))


@router.post(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}/Actions/Zone.AddEndpoint",
    response_model_exclude_none=True,
)
@authenticate
async def add_endpoint2(
    zone_id: str, request: Request, response: Response, body: AddEndpointRequest
) -> RedfishError:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "AddEndpoint",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/CompositionService/ResourceZones/{zone_id}/Actions/Zone.RemoveEndpoint",
    response_model_exclude_none=True,
)
@authenticate
async def remove_endpoint2(
    zone_id: str, request: Request, response: Response, body: RemoveEndpointRequest
) -> RedfishError:
    s: Service = get_service(Zone, request)
    b: dict[str, Any] = {
        "zone_id": zone_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "RemoveEndpoint",
    }
    return s.action(**b)
