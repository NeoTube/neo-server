from typing import Type

from fastapi import FastAPI
from pydantic import BaseModel


class AppBase(BaseModel):
    """Basic BaseModel to check if app is FastAPI Instance"""
    app: Type[FastAPI]
