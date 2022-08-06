from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware


def register(app: FastAPI) -> None:
    app.add_middleware(GZipMiddleware, minimum_size=1000)
