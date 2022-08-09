


from pydantic import AnyUrl, BaseSettings
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class DbSettings(BaseSettings):

    mongodb_uri: Optional[AnyUrl]
    mongodb_name: Optional[str] = 'test'

    @property
    def db(self) -> AsyncIOMotorDatabase:
        return AsyncIOMotorClient(self.mongodb_uri)[self.mongodb_name]
