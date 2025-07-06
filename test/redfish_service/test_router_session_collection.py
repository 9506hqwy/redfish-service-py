from http import HTTPStatus

from fastapi.testclient import TestClient

from redfish_service.server import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/redfish/v1/SessionService/Sessions")
    assert response.status_code == HTTPStatus.OK
