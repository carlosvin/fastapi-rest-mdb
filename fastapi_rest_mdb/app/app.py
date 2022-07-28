
from importlib.metadata import version as get_version
from logging import Logger, getLogger
from unicodedata import name

from fastapi import FastAPI
from fastapi_rest_mdb.app.logger import config_logger

from fastapi_rest_mdb.app.settings import Settings

class App:

    def __init__(self, settings: Settings) -> None:
        """
        it initializes a fastAPI app
        """
        self._logger = getLogger(self.package())
        config_logger(self._logger, settings.loglevel)
        self._app = FastAPI(
            debug=settings.is_debug,
            name=self.package())

    @classmethod
    def version(cls) -> str:
        """returns app version as defined in toml config"""
        return get_version(cls.package())
    
    @classmethod
    def package(cls) -> str:
        """returns main package name"""
        return __name__.split('.', maxsplit=1)[0]
