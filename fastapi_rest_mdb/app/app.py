
from importlib.metadata import version as get_version
from logging import Logger, getLogger

from fastapi import FastAPI
from fastapi_rest_mdb.app.logger import config_logger, new_logger

from fastapi_rest_mdb.app.settings import Settings

class App:

    def __init__(self, settings: Settings) -> None:
        """
        it initializes a fastAPI app
        """
        self._settings = settings
        self._logger = new_logger(self.package(), settings.loglevel)
        self._app = FastAPI(
            debug=settings.is_debug,
            name=self.package())

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
