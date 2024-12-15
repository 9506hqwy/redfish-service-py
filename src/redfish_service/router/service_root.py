from fastapi import APIRouter

from ..v1 import ServiceRoot
from . import PATH_SERVICE_ROOT, PATH_SESSION_COLLECTION, authenticate

root_info = {
    "odata_id": f"{PATH_SERVICE_ROOT}/",
    "odata_type": "#ServiceRoot.v1_17_0.ServiceRoot",
    "id": "ServiceRoot",
    "name": "Service Root",
    "links": {
        "sessions": {
            "odata_id": PATH_SESSION_COLLECTION,
        },
    },
}

router = APIRouter()


@router.get("/", response_model_exclude_none=True)
@authenticate
async def root() -> ServiceRoot:
    return ServiceRoot.model_validate(root_info)
