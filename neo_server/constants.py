import os

TRACE_LOGGERS: list[str] = [f"!{__name__}"]

MAIN_DIR = os.path.dirname(__file__)

HEADER_JSON = os.path.join(MAIN_DIR, "utils/storage/headers_auth.json")

DEBUG = True
DEBUG_PATH = os.path.join(MAIN_DIR, "utils/storage/debug/") if DEBUG else None
