import logging
from typing import Optional
from pydantic import AnyUrl, BaseSettings

DEBUG_LEVEL = "DEBUG"


class Settings(BaseSettings):

    loglevel: str = DEBUG_LEVEL
    mongodb_uri: Optional[AnyUrl]
    mongodb_name: Optional[str]

    @property
    def is_debug(self) -> bool:
        return self.loglevel == DEBUG_LEVEL
