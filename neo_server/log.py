#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# File Name: log.py
import logging
from typing import Optional, cast

from icecream import ic
from rich.logging import RichHandler

from neo_server import constants

ic.configureOutput(includeContext=True)
TRACE_LEVEL = 5


class CustomLogger(logging.Logger):
    """Custom Logger, initialized with rich handler"""

    def __init__(self, name: Optional[str], level: logging = logging.NOTSET):
        super().__init__(name, level)
        self.addHandler(RichHandler())

    def trace(self, msg: Optional[str], *args, **kwargs) -> None:
        """Trace Level message Custom for this logger"""
        if self.isEnabledFor(TRACE_LEVEL):
            super().log(TRACE_LEVEL, ic.format(msg), *args, **kwargs)

    def warn(self, msg: Optional[str], *args, **kwargs) -> None:
        """Warn Level message Custom for this logger"""
        super().warning(ic.format(msg), *args, **kwargs)

    def info(self, msg: Optional[str], *args, **kwargs) -> None:
        """Info Level message Custom for this logger"""
        super().info(ic.format(msg), *args, **kwargs)

    def error(self, msg: Optional[str], *args, **kwargs) -> None:
        """Error Level message Custom for this logger"""
        super().error(ic.format(msg), *args, **kwargs)

    def critical(self, msg: Optional[str], *args, **kwargs) -> None:
        """Critical Level message Custom for this logger"""
        super().critical(ic.format(msg), *args, **kwargs)

    def exception(self, msg: Optional[str], *args, **kwargs) -> None:
        """Exception Level message Custom for this logger"""
        super().exception(ic.format(msg), *args, **kwargs)


def get_logger(name: Optional[str] = None) -> CustomLogger:
    """Return a logger with the given name. Which tends to be done by
    get_logger(__name__) in most cases.
    Parameters
    ----------
    name : Optional[str]
        Name of instance / module
    Returns
    -------
    CustomLoggerLogger
        CustomerLoger
    """
    return cast(CustomLogger, logging.getLogger(name))


def setup() -> None:
    """ setup file for logger - initialises level, format  and its own trace """
    logging.TRACE = TRACE_LEVEL
    logging.addLevelName(TRACE_LEVEL, "TRACE")
    logging.setLoggerClass(CustomLogger)

    root_log = get_logger()
    format_string = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    logging.Formatter(format_string)
    root_log.setLevel(logging.INFO)
    _set_trace_loggers()


def _set_trace_loggers() -> None:
    """
    Set loggers to the trace level according to the value from the BOT_TRACE_LOGGERS env var.
    Options is we have a  list[str] where str starts with either ! or * to indicate logger
    if ! then we set the logger to the trace so
    test = ["!", "... "] will all be set to trace
    test = ["*", "..."] will all be set to debug
    """
    trace_loggers = constants.TRACE_LOGGERS

    for logger_name in trace_loggers:
        if logger_name.startswith("!"):  # pragma: no cover
            logger_name = logger_name.lstrip("!")
            get_logger(logger_name).setLevel(TRACE_LEVEL)
        get_logger(logger_name).trace(get_logger(logger_name).level)
