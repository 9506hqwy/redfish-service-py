from ..model.service_root import ServiceRoot
from ..model.session_collection import SessionCollection
from .instance import instances

PATH_SESSION_COLLECTION = "/redfish/v1/SessionService/Sessions"


def init_instances() -> None:
    service_root = ServiceRoot.model_validate(
        {
            "odata_id": "",
            "id": "ServiceRoot",
            "name": "Service Root",
            "links": {
                "sessions": {
                    "odata_id": PATH_SESSION_COLLECTION,
                },
            },
        }
    )
    instances.add(service_root)

    session_collection = SessionCollection.model_validate(
        {
            "odata_id": "",
            "members": [],
            "members_odata_count": 0,
            "name": "Session Collection",
        }
    )
    instances.add(session_collection)
