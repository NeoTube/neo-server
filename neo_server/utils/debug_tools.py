import json
from typing import Dict

from neo_server import constants
from neo_server.log import get_logger

log = get_logger(__name__)
log.info("Debug tools loaded")


def write_to_file(dict_container: Dict, file_name: str) -> None:
    """Write to file in json format to debug youtube search results.

    Parameters
    ----------
    dict_container : Dict
        dictionary full of data
    file_name : str
        file_name you want to write to
    """
    with open(constants.DEBUG_PATH + file_name + ".json", "w") as f:
        try:
            json_doc = json.dumps(dict_container, indent=4)
        except Exception as e:
            log.exception(e)
            json_doc = json.dumps(dict_container, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        f.write(json_doc)
