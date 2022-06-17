#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: __main__.py

import os

from ytmusicapi import YTMusic

from neo_server import constants
from neo_server.log import get_logger

log = get_logger(__name__)
if not os.path.exists(constants.HEADER_JSON):
    log.warn("file does not exist : ")
    os.mknod(constants.HEADER_JSON)

if os.stat(constants.HEADER_JSON).st_size == 0:
    log.warn("file is empty : ")
    YTMusic.setup(filepath=constants.HEADER_JSON)
