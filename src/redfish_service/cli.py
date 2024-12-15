import logging
import os
from argparse import ArgumentParser, Namespace

import uvicorn

from .service import app


def parse_args() -> Namespace:
    bind = os.environ.get("BIND") or "0.0.0.0"  # noqa: S104
    port = os.environ.get("PORT") or "8000"

    parser = ArgumentParser()
    parser.add_argument("-b", "--bind", default=bind)
    parser.add_argument("-p", "--port", default=int(port), type=int)
    parser.add_argument("-d", "--debug", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_level = logging.DEBUG if args.debug else logging.INFO
    uvicorn.run(app, host=args.bind, port=args.port, log_level=log_level)


if __name__ == "__main__":  # pragma: no cover
    main()
