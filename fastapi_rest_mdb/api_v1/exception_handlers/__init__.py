
from logging import Logger
from fastapi import FastAPI

def register(app: FastAPI, logger: Logger) -> None:

    from fastapi.exception_handlers import (
        request_validation_exception_handler,
    )
    from fastapi.exceptions import RequestValidationError


    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc):
        logger.debug(f"OMG! The client sent invalid data!: {exc}")
        return await request_validation_exception_handler(request, exc)

