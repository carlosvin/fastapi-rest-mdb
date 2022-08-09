from importlib.metadata import version as get_version
from logging import Logger, getLogger

from fastapi import FastAPI
from fastapi_rest_mdb import api_v1
from fastapi_rest_mdb.app import exception_handlers, middlewares
from fastapi_rest_mdb.app.logger import config_loggers
from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi_rest_mdb.app.settings import AppSettings

class App:
    """
    it initializes the FastAPI app, routes, middlewares, logging...
    """

    def __init__(self, settings: AppSettings, db: AsyncIOMotorDatabase) -> None:
        """
        it initializes a fastAPI app
        """
        self._settings = settings
        self._app = FastAPI(
            debug=settings.is_debug,
            name=self.package(),
            version=self.version(),
        )
        self._app.state.logger = getLogger(self.package())
        self._app.state.db = db
        config_loggers(
            settings.loglevel,
            self.package(),
            "uvicorn.access",
            "uvicorn.error",
            "fastapi",
        )
        api_v1.register(self._app)
        middlewares.register(self._app)
        exception_handlers.register(self._app)


    @property
    def app(self) -> FastAPI:
        return self._app

    @property
    def logger(self) -> Logger:
        return self._app.state.logger

    @classmethod
    def version(cls) -> str:
        """returns app version as defined in toml config"""
        return get_version(cls.package())

    @classmethod
    def package(cls) -> str:
        """returns main package name"""
        return __name__.split(".", maxsplit=1)[0]
