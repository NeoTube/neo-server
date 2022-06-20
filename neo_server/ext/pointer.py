from __future__ import annotations

from typing import Type

from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from neo_server.models.app_base import AppBase


def api_test() -> int:
    """Test"""
    return 10


router = InferringRouter()


@cbv(router)
class TestRouter:
    """Test Router"""

    def __init__(self) -> None:
        self.x: int = Depends(api_test)

    @router.get("/test")
    def test(self) -> int:
        return self.x

    @router.post("/test")
    def test_post(self, item: int) -> dict:
        return {
            "message": {
                "test": item
            }
        }


def setup(app: Type[AppBase]) -> None:
    """Setup - adds router to NeoTube FastAPi Instance."""
    app.include_router(router)
