from http import HTTPStatus
from typing import Any, cast

from fastapi import Response

from ..exception import ResourceNotFoundError
from ..model.session import Session
from ..model.session_collection import SessionCollection
from ..repository import instances
from ..service import Service
from ..util import create_etag


class SessionService(Service[Session]):
    def respond(self, ty: type) -> bool:
        return ty == Session

    def delete(self, **kwargs: dict[str, Any]) -> None:
        session_id = cast(str, kwargs.get("session_id"))
        res: Response = cast(Response, kwargs["response"])

        collection = self._get_collection()

        etag = create_etag()
        s = self._get_by_id(session_id)

        instances.remove(s)
        collection.odata_etag = etag

        res.status_code = HTTPStatus.NO_CONTENT

    def get(self, **kwargs: dict[str, Any]) -> Session:
        session_id = cast(str, kwargs.get("session_id"))
        return self._get_by_id(session_id)

    def _get_by_id(self, id: str) -> Session:
        s = next((s for s in instances.enum_by_type(Session) if s.id == id), None)
        if s is None:
            raise ResourceNotFoundError("Session", id)

        return s

    def _get_collection(self) -> SessionCollection:
        i = instances.find_by_type(SessionCollection)
        if i is None:
            raise ResourceNotFoundError("SessionCollection", "SessionCollection")

        return i
