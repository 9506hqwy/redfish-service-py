import logging
import os
from argparse import ArgumentParser, Namespace

import uvicorn
from fastapi_profiler import PyInstrumentProfilerMiddleware  # type: ignore

from .repository import init_instances
from .server import app


def parse_args() -> Namespace:
    bind = os.environ.get("BIND") or "0.0.0.0"  # noqa: S104
    port = os.environ.get("PORT") or "8000"

    parser = ArgumentParser()
    parser.add_argument("-b", "--bind", default=bind)
    parser.add_argument("-p", "--port", default=int(port), type=int)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("--profile", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_level = logging.DEBUG if args.debug else logging.INFO
    if args.profile:
        app.add_middleware(
            PyInstrumentProfilerMiddleware,
            server_app=app,
            profiler_output_type="html",
            is_print_each_request=False,
            html_file_name="profile.html",
        )

    init_instances()
    uvicorn.run(app, host=args.bind, port=args.port, log_level=log_level)


if __name__ == "__main__":  # pragma: no cover
    main()
