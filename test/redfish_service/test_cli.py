import logging
from unittest import mock

import uvicorn

from redfish_service import cli
from redfish_service.server import app


def test_default() -> None:
    with mock.patch("sys.argv", ["python"]):
        with mock.patch.object(uvicorn, "run") as uvicorn_run:
            cli.main()

    uvicorn_run.assert_called_once_with(app, host="0.0.0.0", port=8000, log_level=logging.INFO)  # noqa: S104
