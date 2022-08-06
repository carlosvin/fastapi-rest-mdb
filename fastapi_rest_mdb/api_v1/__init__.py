from fastapi import APIRouter, FastAPI
from . import users


def register(app: FastAPI):
    """register the api v1 routes"""
    router = APIRouter(prefix="/v1")
    router.include_router(users.router)
    app.include_router(router)
