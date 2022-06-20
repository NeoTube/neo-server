import importlib

from fastapi import FastAPI

from neo_server.log import get_logger

log = get_logger("norg")


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
        log.info("Instance has been created")
        return app
