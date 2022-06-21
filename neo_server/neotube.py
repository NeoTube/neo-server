import asyncio
import importlib

from fastapi import FastAPI
from uvicorn import Config, Server

from neo_server.log import get_logger

log = get_logger(__name__)


class StartupError(Exception):
    """Exception class for startup errors."""

    def __init__(self, base: Exception):
        super().__init__()
        self.exception = base


class NeoTube(FastAPI):
    """FastApi Custom instance for NeoTube"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_routers(self) -> None:
        """Load routers : from ext module"""

        from neo_server.utils.extensions import EXTENSIONS
        for i in EXTENSIONS:
            log.info(f"loading {i}")
            self.load_extension(i)

    def load_extension(self, name: str) -> None:
        """Import the extensions : i.e import setup"""
        imported = importlib.import_module(name)
        imported.setup(self)

    @classmethod
    def create(cls) -> "NeoTube":
        """Create an NeoTube/FastAPI Instance"""
        app = cls()
        app.load_routers()
        # https://github.com/encode/uvicorn/issues/706
        loop = asyncio.get_event_loop()
        config = Config(app=app, loop=loop)
        server = Server(config)
        loop.run_until_complete(server.serve())
