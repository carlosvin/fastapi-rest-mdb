
from typing import Optional
from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):

    loglevel: str = 'DEBUG'
    is_debug: bool = False
    mongodb_uri: Optional[AnyUrl]
    mongodb_name: Optional[str]
