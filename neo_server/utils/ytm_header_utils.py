import os

from ytmusicapi import YTMusic

from neo_server import constants
from neo_server.log import get_logger

log = get_logger(__name__)


def exists() -> bool:
    """Check if the file exists."""
    return os.path.exists(constants.HEADER_JSON)


def empty() -> bool:
    """ Check if file is empty. """
    #  TODO(vsedov) (17:33:30 - 19/06/22): Check if it contains valid Content.
    return os.stat(constants.HEADER_JSON).st_size == 0


def check_header_json() -> None:
    """ Check if file exists , if not create it and check if it contains default values."""
    if not exists():
        log.warn("file does not exist : ")
        os.mknod(constants.HEADER_JSON)

    if empty():
        log.warn("file is empty : ")
        YTMusic.setup(filepath=constants.HEADER_JSON)


def remove_header_json() -> None:
    """ deletes all the contents of the header json file. """
    if exists():
        with open(constants.HEADER_JSON, "r+") as f:
            f.seek(0)
            f.truncate()
    else:
        log.warn(f"file does not exist : {constants.HEADER_JSON}")


def setup() -> YTMusic:
    """Return YTM instance."""
    check_header_json()
    return YTMusic(constants.HEADER_JSON)
