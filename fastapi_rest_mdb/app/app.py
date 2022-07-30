
from importlib.metadata import version as get_version
from logging import Logger, getLogger

from fastapi import FastAPI, Depends
from fastapi_rest_mdb import api_v1
from fastapi_rest_mdb.api_v1 import exception_handlers
from fastapi_rest_mdb.api_v1.middlewares import register_middlewares
from fastapi_rest_mdb.app.logger import config_logger, config_uvicorn_loggers, new_logger

from fastapi_rest_mdb.app.settings import Settings

class App:
    """
    it initializes the FastAPI app, routes, middlewares, logging...
    """

    def __init__(self, settings: Settings) -> None:
        """
        it initializes a fastAPI app
        """
        self._settings = settings
        self._logger = new_logger(self.package(), settings.loglevel)
        config_uvicorn_loggers(settings.loglevel)

        self._app = FastAPI(
            debug=settings.is_debug,
            name=self.package(),
            version=self.version(), 
        )
        self._app.include_router(api_v1.router)
        register_middlewares(self._app)
        exception_handlers.register(self._app, self._logger)

    def _init_logger(self) -> Logger:
        logger = getLogger(self.package())
        config_logger(logger, self._settings.loglevel)
        logger.info("initialized!", extra={'props': {'yay': 'yes'}})
        return logger



    

    @property
    def app(self) -> FastAPI:
        return self._app

    @classmethod
    def version(cls) -> str:
        """returns app version as defined in toml config"""
        return get_version(cls.package())
    
    @classmethod
    def package(cls) -> str:
        """returns main package name"""
        return __name__.split('.', maxsplit=1)[0]
