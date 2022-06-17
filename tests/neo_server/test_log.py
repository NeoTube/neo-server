#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: test_log.py

import logging

import pytest

import neo_server.log as log


@pytest.fixture()
def log_instance() -> log:
    """Return Instance of whole file"""
    return log


@pytest.fixture()
def get_logger(log_instance: log) -> log:
    """Return log instance : get_logger."""

    return log_instance.get_logger()


@pytest.mark.usefixtures()
class TestLog:
    """Test logging levels."""

    def test_get_logger(self, get_logger: log) -> None:
        """Test handler and get_logger at the same time."""
        get_logger.info("test")
        assert len(get_logger.handlers) == 4

        def capture_hander(handler: log) -> None:
            handler.buffer = []
            handler.buffer.append('test append')
            return handler

        handle = capture_hander(get_logger.handlers[0])
        get_logger.info("test append")
        assert handle.buffer == ['test append']

    def test_get_logger_with_handler(self, get_logger: log) -> None:
        """Test get_logger handlers. They just need to be called once."""
        get_logger.info("info")
        get_logger.debug("debug")
        get_logger.error("error")
        get_logger.critical("critical")
        get_logger.warn("warn")
        assert len(get_logger.handlers) == 4

        get_logger.setLevel(logging.DEBUG)
        assert get_logger.level == logging.DEBUG

    def test_custom_logger_instances(self, log_instance: log_instance) -> None:
        """Test custom logger instances. Directly from Custom Logger"""
        log = log_instance.CustomLogger(logging.Logger)
        assert isinstance(log, logging.Logger)
        log.setLevel(logging.INFO)
        assert log.level == logging.INFO
        log.trace("trace")
        log.level = log_instance.TRACE_LEVEL

        assert log.level == 5

        log.warn("warn")
        log.error("error")
        log.critical("critical")
        log.info("info")
        log.critical("critical")
        log.exception("")
