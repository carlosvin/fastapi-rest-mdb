from fastapi import FastAPI
from fastapi.exception_handlers import (
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError


async def _validation_exception_handler(request, exc):
    request.app.state.logger.error(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)

def register(app: FastAPI) -> None:
    app.add_exception_handler(RequestValidationError, _validation_exception_handler)
    