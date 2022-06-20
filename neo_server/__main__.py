#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: __main__.py

from neo_server.log import get_logger
from neo_server.neotube import StartupError
from neo_server.utils.ytm_header_utils import check_header_json

log = get_logger(__name__)

try:
    check_header_json()

    # neotube.instance = NeoTube.create()
    # uvicorn.run(neotube.instance, host="127.0.0.1")

except StartupError as e:
    message = "Unknown Startup Error Occurred."
    if e.args:
        message = e.args[0]
    log.fatal("", exc_info=e.exception)
    log.fatal(message)

    exit(69)
