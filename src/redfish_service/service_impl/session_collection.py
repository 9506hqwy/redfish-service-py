from typing import Any, cast

from fastapi import Request

from ..exception import ResourceNotFoundError
from ..model.session_collection import SessionCollection
from ..repository import instances
from ..service import Service


class SessionCollectionService(Service[SessionCollection]):
    def respond(self, ty: type) -> bool:
        return ty == SessionCollection

    def get(self, **kwargs: dict[str, Any]) -> SessionCollection:
        i = instances.find_by_type(SessionCollection)
        if i is None:
            raise ResourceNotFoundError("SessionCollection", "SessionCollection")

        req: Request = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        return i
