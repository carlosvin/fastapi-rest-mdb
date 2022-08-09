from pydantic import BaseSettings

DEBUG_LEVEL = "DEBUG"


class AppSettings(BaseSettings):

    loglevel: str = DEBUG_LEVEL

    @property
    def is_debug(self) -> bool:
        return self.loglevel == DEBUG_LEVEL
